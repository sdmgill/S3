import boto3
import string
import re

s3 = boto3.resource("s3")

my_bucket = s3.Bucket("pa-bi")
object_list = []

for object in my_bucket.objects.all():
    clean_obj=str(object).replace("s3.ObjectSummary(bucket_name='pa-bi', key=","")
    clean_obj2=str(clean_obj).replace("'","")
    clean_obj3 = str(clean_obj2).replace(")", "")
    object_list.append(clean_obj3)

#print(object_list)
sub = 'mijack/latchpythontest/Incremental/latch'
for text in object_list:
    if sub in text:
        print(text)
