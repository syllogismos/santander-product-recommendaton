
import datetime
import os
import zipfile
from subprocess import call

import boto
import boto.s3
from boto.s3.key import Key

import scripts.kaggle.aws_config as aws_config


def make_submission(file_path, bucket_name='bosch-submissions',
                    description='submission description', upload_to_s3=False,
                    submit=False, compress=True):
    """
    Given a file compresses the file, and based on flags upload_to_s3 and
    submit it uploads the submission to s3 and or makes a submission to
    kaggle with given description.

    For submit flag to work, make sure you have kaggle-cli python package 
    installed.
    https://github.com/floydwch/kaggle-cli
    you also have to make sure you have kaggle-cli configured with right 
    username password and competition name by doing
    kg config -u username -p password -c competition_name

    and aws_config should be containing you aws secret key for s3 to work.
    """
    file_name = os.path.basename(file_path)
    if compress:
        compression = zipfile.ZIP_DEFLATED
        zip_file_name = file_path + '.zip'
        zf = zipfile.ZipFile(zip_file_name, mode='w')
        print "Compressing file"
        zf.write(file_path, arcname=file_name, compress_type=compression)
        print "Compression done"
        zf.close()
    else:
        zip_file_name = file_path

    if upload_to_s3:
        conn = boto.connect_s3(aws_config.AWS_ACCESS_KEY,
                               aws_config.AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(bucket_name)
        print "Uploading file to s3 %s" % (zip_file_name)

        k = Key(bucket)
        k.key = str(datetime.datetime.now())[
            :-7] + ' ' + os.path.basename(zip_file_name)
        k.set_contents_from_filename(zip_file_name)
        print "uploading to s3 done"

    description = description + '\n' + str(datetime.datetime.now())[:-7]

    if submit:
        print "Uploading submission", zip_file_name
        call(['kg', 'submit', zip_file_name, '-m', description])
        print "Upload done"
