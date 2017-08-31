#!/usr/bin/env python

import boto3
from pprint import pprint
from datetime import datetime

def datetime_handler(x):
    if isinstance(x, datetime):
        return x.isoformat()
    raise TypeError("Unknown Type")

def list_active_volumes(voldata):
    count = 0
    for volitem in voldata:
        if (volitem['Attachments']):
            print(50 *  "-")
            count+=1
            print(count)
            pprint(volitem['Attachments'])

def main():
    # Connecting to the ec2 client
    client = boto3.client('ec2')
    response = client.describe_volumes()
    list_active_volumes(response['Volumes'])


if __name__ == "__main__":
    main()
