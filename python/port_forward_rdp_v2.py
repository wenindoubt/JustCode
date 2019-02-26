#!/usr/bin/env python
"""Port forward into bastion host and RDP."""

import subprocess
import os
import base64
import logging
import random
import boto3
import rsa
import yaml


class DecryptEC2():
    """Do stuff."""

    def __init__(self, instance_id, private_key):
        """Do stuff."""
        self.client = boto3.client('ec2')
        self.instance_id = instance_id
        self.private_key = private_key

    def decrypt_password(self):
        """Do stuff."""
        password_response = self.client.get_password_data(
            InstanceId=self.instance_id)
        encrypted_password = base64.b64decode(
            password_response["PasswordData"].strip())
        if encrypted_password:
            with open(self.private_key) as private_key_file:
                private_key_contents = rsa.PrivateKey.load_pkcs1(
                    private_key_file.read())
                decrypted_password = rsa.decrypt(encrypted_password,
                                                 private_key_contents)
        else:
            logging.error("A password cannot be retrieved for this instance.")
            exit()

        return decrypted_password

    def extra_method(self):
        """Do stuff."""


class PortForward():
    """Do stuff."""

    def __init__(self, instance_id, bastion_ip, private_key,
                 decrypted_password):
        """Do things."""
        self.client = boto3.client('ec2')
        self.instance_id = instance_id
        self.bastion_ip = bastion_ip
        self.private_key = private_key
        self.decrypted_password = decrypted_password
        instance_response = self.client.describe_instances(
            InstanceIds=[self.instance_id])
        self.private_ip = instance_response['Reservations'][0]['Instances'][0][
            'PrivateIpAddress']

    def __repr__(self):
        """Do things."""
        return (f"PortForward(instance_id={self.instance_id}, "
                f"bastion_ip={self.bastion_ip}, "
                f"private_key={self.private_key}, "
                f"decrypted_password={self.decrypted_password}")

    def __str__(self):
        """Do things."""
        return (f"Instance ID: {self.instance_id}\n"
                f"Bastion IP: {self.bastion_ip}\n"
                f"Private Key: {self.private_key}\n"
                f"Decrypted Password: {self.decrypted_password}")

    def jump_desktop(self):
        """Do stuff."""
        random_local_port = random.randint(30000, 40000)
        port_forward_command = (
            f"ssh -fNT -i {self.private_key} "
            f"-L {random_local_port}:{self.private_ip}:3389 "
            f"ec2-user@{self.bastion_ip} && open "
            f"'jump://?host=localhost:{random_local_port}"
            f"&username=Administrator"
            f"&IgnoreCertificateErrors=true"
            f"&MouseCursorUpdates=false"
            f"&DisplayName={self.instance_id}"
            f"&password={self.decrypted_password}'")

        subprocess.run(port_forward_command, shell=True)


def main():
    """Do things."""
    logging.basicConfig(
        format='%(levelname)s:%(message)s', level=logging.WARNING)

    with open("config.yaml") as yamlfile:  # https://yaml.org/faq.html
        config_options = yaml.load(yamlfile)

    input_instance_id = input("Instance ID [none]: ") or "none"
    input_bastion_ip = config_options["bastion_ip"]
    input_private_key = os.path.expanduser(config_options["private_key"])

    instance_password = DecryptEC2(input_instance_id, input_private_key)
    print(
        f"Decrypted Password: {instance_password.decrypt_password().decode()}")

    custom_instance = PortForward(
        input_instance_id, input_bastion_ip, input_private_key,
        instance_password.decrypt_password().decode())

    custom_instance.jump_desktop()


if __name__ == "__main__":
    main()
