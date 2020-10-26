# Automating AWS with Python

Respository for the ACloud Guru course *Automation scripts in python for working with AWS*

## 01-webdeploy

webdeploy is a script yhat will sync a local directory to an s3 bucket, and optionally configure Route53 and cloudfront as well.

### Features

- List all buckets
- List content of a bucket
- Create and configure S3 Bucket
- Sync directory tree to bucket
- Set AWS profile with --profile=<profileName>
- Configure route 53 domain