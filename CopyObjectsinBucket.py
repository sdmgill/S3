import boto3

s3 = boto3.resource("s3")
s3copy=boto3.client("s3")

searchbucket = s3.Bucket("pa-dms-staging")

sourcebucket = "pa-dms-staging"
targetbucket = "pa-processed"

# change this string based on the S3 "folder" you want to clean #
sub = 'mistar/pnct/incremental/fm/impact/'

object_list = []


for object in searchbucket.objects.all():
    clean_obj=str(object).replace("s3.ObjectSummary(bucket_name='pa-dms-staging', key=","")
    clean_obj2=str(clean_obj).replace("'","")
    clean_obj3 = str(clean_obj2).replace(")", "")
    object_list.append(clean_obj3)

#print(object_list)

# perform the copy to the pa-processed Bucket #
for text in object_list:
    if sub in text:
        copy_source = {'Bucket':sourcebucket,'Key':str(text)}
        copy_target = {'Bucket':targetbucket,'Key':str(text)}
        s3copy.copy(copy_source,copy_target['Bucket'],copy_target['Key'])
        #print(copy_source)
        #print(text)

# delete files from Staging after they have been copied to processed #
for cya in object_list:
    if sub in cya:
        s3.Object(sourcebucket, cya).delete()