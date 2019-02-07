#!/usr/bin/env python
"""Port forward into bastion host and RDP."""

import subprocess
import argparse
import os
import base64
import logging
import boto3
import rsa


def do_magic():
    """Do some magic."""
    client = boto3.client('ec2')

    parser = argparse.ArgumentParser(
        description='Port forward into bastion host and RDP')
    required_parser = parser.add_argument_group('required arguments')

    # Optional Arguments
    parser.add_argument(
        '-l', '--local_rdp_port', help='Default: 3389', default=3389)
    parser.add_argument(
        '-u', '--user', help='Default: Administrator', default='Administrator')
    parser.add_argument(
        '-p',
        '--private_key',
        help=f"Default: {os.environ['HOME']}/.ssh/id_rsa",
        default=f"Default: {os.environ['HOME']}/.ssh/id_rsa")

    # Required Arguments
    required_parser.add_argument(
        '-i', '--instance_id', help='EC2 Instance ID', required=True)
    required_parser.add_argument(
        '-b',
        '--bastion_ip_address',
        help='Bastion Host\'s Public IP Address',
        required=True)

    args = parser.parse_args()

    password_response = client.get_password_data(InstanceId=args.instance_id)
    encrypted_password = base64.b64decode(
        password_response["PasswordData"].strip())

    if encrypted_password:
        with open(args.private_key) as private_key_file:
            private_key_contents = rsa.PrivateKey.load_pkcs1(
                private_key_file.read())
            decrypted_password = rsa.decrypt(encrypted_password,
                                             private_key_contents)
    else:
        logging.error("A password cannot be retrieved for this instance.")
        exit()

    ip_response = client.describe_instances(InstanceIds=[args.instance_id])
    private_ip_address = ip_response['Reservations'][0]['Instances'][0][
        'PrivateIpAddress']

    copied_password = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    copied_password.stdin.write(decrypted_password)
    copied_password.stdin.close()
    retcode = copied_password.wait()
    if retcode != 0:
        logging.error("pbcopy failed with return code: %s", retcode)

    logging.info("Password is: %s", decrypted_password.decode())

    port_forward_command = (
        f"ssh -fNT -i {args.private_key} "
        f"-L {args.local_rdp_port}:{private_ip_address}:3389 "
        f"ec2-user@{args.bastion_ip_address} && open "
        f"'jump://?host=localhost:{args.local_rdp_port}"
        f"&username={args.user}"
        f"&IgnoreCertificateErrors=true"
        f"&MouseCursorUpdates=false"
        f"&DisplayName={args.instance_id}"
        f"&password={decrypted_password.decode()}'")

    subprocess.run(port_forward_command, shell=True)


def main():
    """Run all the magic."""
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    do_magic()


if __name__ == "__main__":
    main()
