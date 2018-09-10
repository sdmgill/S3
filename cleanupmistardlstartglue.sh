#!/bin/bash
PATH=/usr/bin:/usr/local/bin
aws s3 rm s3://data-lake-us-west-2-062519970039/parquet/mistar --recursive
aws lambda invoke --function-name start-glue-jobs-mistar outfile.txt
