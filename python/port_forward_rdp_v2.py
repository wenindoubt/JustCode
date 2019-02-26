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
from botocore.exceptions import ClientError


class ValidateEC2():
    """Do stuff."""

    def __init__(self, instance_id):
        """Do stuff."""
        self.client = boto3.client("ec2")
        self._instance_id = instance_id

    def __repr__(self):
        """Do stuff."""
        return f"ValidateEC2('{self.instance_id}')"

    def __str__(self):
        """Do stuff."""
        return f"Instance ID: {self.instance_id}"

    @property
    def instance_id(self):
        """Do stuff."""
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        """Do stuff."""
        try:
            self.client.describe_instances(InstanceIds=[value])
            self._instance_id = value
        except ClientError as error_message:
            print(error_message)

        return self._instance_id

    def extra_method(self):
        """Do stuff."""


class DecryptEC2(ValidateEC2):
    """Do stuff."""

    def __init__(self, instance_id, private_key):
        """Do stuff."""
        super().__init__(instance_id)
        self.client = boto3.client("ec2")
        self._instance_id = instance_id
        self.private_key = private_key

    def __repr__(self):
        """Do stuff."""
        return (
            f"DecryptEC2(instance_id='{self._instance_id}', "
            f"private_key='{self.private_key}')"
        )

    def __str__(self):
        """Do stuff."""
        return (
            f"Instance ID: {self._instance_id}\n"
            f"Private Key: {self.private_key}"
        )

    @property
    def instance_id(self):
        """Do stuff."""
        # GitHub Issue - https://github.com/PyCQA/pylint/issues/2641
        # pylint: [no-member] Method 'instance_id' has no 'fget' member [E1101]
        # return ValidateEC2.instance_id.fget(self)
        # Solution - https://stackoverflow.com/questions/1021464/how-to-call-a-property-of-the-base-class-if-this-property-is-being-overwritten-i
        return super().instance_id

    @instance_id.setter
    def instance_id(self, value):
        """Do stuff."""
        # GitHub Issue - https://github.com/PyCQA/pylint/issues/2641
        # pylint: [no-member] Method 'instance_id' has no 'fset' member [E1101]
        # return ValidateEC2.instance_id.fset(self, value)
        # Solution - https://stackoverflow.com/questions/1021464/how-to-call-a-property-of-the-base-class-if-this-property-is-being-overwritten-i
        super(DecryptEC2, self.__class__).instance_id.fset(self, value)

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


class PortForward(ValidateEC2):
    """Do stuff."""

    def __init__(self, instance_id, bastion_ip, private_key,
                 decrypted_password):
        """Do things."""
        super().__init__(instance_id)
        self.client = boto3.client('ec2')
        self._instance_id = instance_id
        self.bastion_ip = bastion_ip
        self.private_key = private_key
        self.decrypted_password = decrypted_password
        instance_response = self.client.describe_instances(
            InstanceIds=[self.instance_id])
        self.private_ip = instance_response['Reservations'][0]['Instances'][0][
            'PrivateIpAddress']

    @property
    def instance_id(self):
        """Do stuff."""
        # GitHub Issue - https://github.com/PyCQA/pylint/issues/2641
        # pylint: [no-member] Method 'instance_id' has no 'fget' member [E1101]
        # return ValidateEC2.instance_id.fset(self, value)
        # Solution - https://stackoverflow.com/questions/1021464/how-to-call-a-property-of-the-base-class-if-this-property-is-being-overwritten-i
        return super().instance_id

    @instance_id.setter
    def instance_id(self, value):
        """Do stuff."""
        # GitHub Issue - https://github.com/PyCQA/pylint/issues/2641
        # pylint: [no-member] Method 'instance_id' has no 'fset' member [E1101]
        # return ValidateEC2.instance_id.fset(self, value)
        # Solution - https://stackoverflow.com/questions/1021464/how-to-call-a-property-of-the-base-class-if-this-property-is-being-overwritten-i
        return super(PortForward, self.__class__).instance_id.fset(self, value)

    def __repr__(self):
        """Do things."""
        return (f"PortForward(instance_id='{self.instance_id}', "
                f"bastion_ip='{self.bastion_ip}', "
                f"private_key='{self.private_key}', "
                f"decrypted_password='{self.decrypted_password}'")

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
