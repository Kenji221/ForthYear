import boto3
client = boto3.client('batch')
response = client.submit_job(
    jobDefinition='test-kk-job-definition',
    jobName='test',
    jobQueue='test',
    containerOverrides={
        'environment': [
            {
                'name': 'table_name',
                'value': 'batch-test-table',
            },
            {
                'name': 'bucket_name',
                'value': 'batch-test-kk-bucket-ap-1',
            },
            {
                'name': 'key',
                'value': 'sample-zip.csv',
            }
        ]
    },
)
print(response)