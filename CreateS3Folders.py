
import boto3

client = boto3.client('s3')

response = client.put_object(
        Bucket='pa-dms-staging',
        Body='',
        Key='n4/pnct/combined/vsl_vessels/'
        )

response2 = client.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/n4/vsl_vessels/'
        )