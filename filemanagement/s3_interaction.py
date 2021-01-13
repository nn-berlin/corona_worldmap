import logging
import boto3
from botocore.exceptions import ClientError

def s3_upload(ec2file, bucketname, bucketfile):
	'''
	ec2file: path included, i.e "./../rawdata/*.txt",
	bucketname: i.e. "berlincoronabucket",
	bucketfile: path included, i.e. "*.txt"
	'''
	s3_client = boto3.client('s3')
	try:
		response = s3_client.upload_file(ec2file, bucketname, bucketfile)
	except ClientError as e:
		logging.error(e)
		return False
	return True

def s3_download(bucketfile, bucketname, ec2file):
	'''
	bucketfile: path included, i.e. "*.txt",
	bucketname: i.e. "berlincoronabucket",
	ec2file: path included, i.e "./../rawdata/*.txt"
	'''
	s3_client = boto3.client('s3')
	try:
		response = s3_client.download_file(bucketfile, bucketname, ec2file)
	except ClientError as e:
		logging.error(e)
		return False
	return True