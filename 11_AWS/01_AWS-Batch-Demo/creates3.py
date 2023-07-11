import boto3 
s3 = boto3.resource('s3')
response = s3.create_bucket(
    Bucket='batch-test-kk-bucket-ap-1',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-northeast-1'
    }
)
print(response)