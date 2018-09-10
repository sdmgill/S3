import boto3
s3=boto3.client("s3")

copy_source = {'Bucket':'pa-bi',
               'Key':'mijack/latchpythontest/Initial/latch/dbo/Latch/LOAD00000001.csv'
                }
#s3.copy(copy_source,'pa-processed','mijack/latchpythontest/Incremental/latch/dbo/Latch/20180315-004206157.csv')
s3.copy(copy_source,'pa-processed','mijack/latchpythontest/Initial/latch/dbo/Latch/LOAD00000001.csv')

