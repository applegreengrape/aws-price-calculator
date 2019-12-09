import boto3
import json
import pprint

pricing = boto3.client('pricing')

print("All Services")
print("============")
response = pricing.describe_services()
for service in response['Services']:
    print(service['ServiceCode'])
print()