import boto3

# grab values from Lambda function Environment Variables
SOURCEBUCKET = 'data-lake-us-west-2-062519970039'  # os.environ['SOURCE_BUCKET']
# TARGETBUCKET = os.environ['TARGET_BUCKET']
FOLDER = 'parquet/mistar/'  # os.environ['S3_FOLDER']


s3 = boto3.resource("s3")
# s3copy = boto3.client("s3")

searchbucket = s3.Bucket(SOURCEBUCKET)

# change this string based on the S3 "folder" you want to clean. Determined
# via the S3_FOLDER Environment Variable #
sub = FOLDER

object_list = []

# place all S3 "folders" in a list and then clean up extraneous values. In
# the AWS world, S3 does not have any "folders". Instead they use "Buckets"
# and "Keys". You can think of a "Bucket" as the Parent Folder and the "Key"
# as the Child Folder
for object in searchbucket.objects.all():
    clean_obj = str(object).replace("s3.ObjectSummary(bucket_name='data-lake-us-west-2-062519970039', key=", "")
    clean_obj2 = str(clean_obj).replace("'", "")
    clean_obj3 = str(clean_obj2).replace(")", "")
    object_list.append(clean_obj3)

#print(object_list)
# delete files from Staging after they have been copied to processed. Again,
# we are filtering on the S3_FOLDER value#
for cya in object_list:
    if sub in cya:
        s3.Object(SOURCEBUCKET, cya).delete()
        #print(cya)
