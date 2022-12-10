#!/usr/bin/env python

import argparse
import os
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', required=True, help='The hostname or IP address of the remote computer')
    parser.add_argument('--port', default=22, help='The port number to connect to on the remote computer')
    parser.add_argument('--username', required=True, help='The username to use when connecting to the remote computer')
    parser.add_argument('--password', help='The password to use when connecting to the remote computer')
    return parser.parse_args()

def ssh_connect(host, port, username, password):
    try:
        import paramiko
    except ImportError:
        print('Failed to import the paramiko library. Please make sure it is installed on your system.')
        sys.exit(1)

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=port, username=username, password=password)
    except paramiko.AuthenticationException:
        print('Failed to authenticate with the remote computer. Please check your username and password.')
        sys.exit(1)
    except Exception as e:
        print('Failed to connect to the remote computer. Please check the hostname and port number. Error: {}'.format(e))
        sys.exit(1)

    return ssh

def main():
    args = parse_args()
    host = args.host
    port = args.port
    username = args.username
    password = args.password

    ssh = ssh_connect(host, port, username, password)
    print('Connected to {}@{} on port {}'.format(username, host, port))

    try:
        while True:
            command = input('{}@{}> '.format(username, host))
            if command == 'exit':
                break
            stdin, stdout, stderr = ssh.exec_command(command)
            print(stdout.read().decode('utf-8'))
    finally:
        ssh.close()

if __name__ == '__main__':
    main()
