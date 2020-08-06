import boto3
import click

session = boto3.session.Session()
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('buckets', nargs=-1)
def list_bucket_objects(buckets):
    "Lists bucket objects"
    for bucket in buckets:
        print("-----Objects from bucket: ", bucket)
        print("----------------------------------")
        for obj in s3.Bucket(bucket).objects.all():
            print(obj)

    pass

if __name__ == '__main__':
    cli()
