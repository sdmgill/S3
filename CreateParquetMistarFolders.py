import boto3

s3 = boto3.client('s3')

flagdescription = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/flagdescription/'
        )

fuel = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/fuel/'
        )

impact = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/impact/'
        )

latch = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/latch/'
        )

latchtype = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/latchtype/'
        )

mapdata = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/mapdata/'
        )

maptype = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/maptype/'
        )

position = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/position/'
        )

roverdetails = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/roverdetails/'
        )


tire = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/tire/'
        )

utctimezoneoffsets = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/utctimezoneoffsets/'
        )

vehicletype = s3.put_object(
        Bucket='data-lake-us-west-2-062519970039',
        Body='',
        Key='parquet/mistar/vehicletype/'
        )