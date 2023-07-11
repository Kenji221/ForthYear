#!/usr/bin/python3
import os
import boto3
import csv 
from datetime import datetime, timezone

s3_resource = boto3.resource('s3')
print('os environ:', os.environ)
bucket_name = os.environ['bucket_name']
key = os.environ['key']
csv_file = s3_resource.Object(bucket_name, key)
items = csv_file.get()['Body'].read().decode('utf-8-sig').splitlines()
reader = csv.reader(items)
header = next(reader)
current_date = datetime.now(timezone.utc).isoformat()[:-6] + 'Z'


for row in reader:
    # print(row[header.index('id')])
    print(row)

print('records imported successfully')