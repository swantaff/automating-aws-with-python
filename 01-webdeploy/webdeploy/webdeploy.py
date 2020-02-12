#!usr/bin/python
# -*- coding: utf-8 -*-

"""Webdeploy: Deploy websites with AWS.

Webdeploy automates the process od deploying statis websites to AWS
- Configure AWS S3 buckets
    - Create them
    - Set them up for static wesite hosting
    - Deploy local files to them
- Configure DNS with AWS Route 53
- Configure a Content Delivery Network and SSL with AWS Cloudfront
"""

import boto3
import click

from bucket import BucketManager

# Global variables
session = None
bucket_manager = None


@click.group()
@click.option('--profile', default=None,
    help="Use a given AWS profile.")
def cli(profile):
    """Webdeploy deploys websites to AWS."""
    
    #ref globals above, than when re-assigned other functions have access to them
    global session, bucket_manager

    session_cfg = {}
    if profile:
        session_cfg['profile_name'] = profile

    # Pass-in dictionary as args to function (sometimes called a glob) with ** operator
    # ** will do the right thing and uwrap or unroll key pairs to make parameters for your function
    session = boto3.Session(**session_cfg) 
    bucket_manager = BucketManager(session)
    pass



@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List the contents of a Bucket."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 Bucket."""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET."""
    print("Bucket in webdeploy is : {}".format(bucket))
    bucket_manager.sync(pathname, bucket)



if __name__ == '__main__':
    cli()
