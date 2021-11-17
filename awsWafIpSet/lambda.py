#!../venv/bin/python3
import os
import json
from caQuery import caQuery
import requests
import boto3


def lambdaHandler(event, context):
    # Read in Env Variables
    aws_access_key = os.environ['access'].encode("utf-8").decode("utf-8")
    aws_secret_key = os.environ['secret'].encode("utf-8").decode("utf-8")
    region = os.environ['AWS_DEFAULT_REGION'].encode("utf-8").decode("utf-8")
    #print(aws_secret_key, region)
    # Appears to be needed for SAM, as requests come in Unicode
    #data = event['body'].encode("utf-8").decode("utf-8")
    #jsonData = json.loads(data)
    #print(jsonData)
    # Retrieve Google Analytics IP Address and returns in a list
    ipv4List = caQuery.gstaticIpRanges()
    print(ipv4List)
    # Take the List and sends it to create and AWS WAF IP Set list
    try:
        response = caQuery.awsRegionalWafIpSet(ipv4List, aws_access_key, aws_secret_key, region)
        print(response)
    except:
        pass
    # Returns the response from creating IP Set List
    try:
        if int(response['ResponseMetadata']['HTTPStatusCode']) == 200:
            return{
            'statusCode': 200,
            'body': json.dumps(response)
            }
    except:
        return{
        'statusCode': 400,
        'body': json.dumps(response)
        }        



