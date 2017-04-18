#!/usr/bin/python

import sys
import subprocess
import time

#pip install boto
import boto
import boto.s3.connection
from boto.s3.connection import S3Connection
from boto.s3.key import Key

print('Number of arguments:', len(sys.argv))
print('Argument List:', str(sys.argv))

if len(sys.argv) < 5:
    print('Usage: python mysqldump.py server db user password s3_access_key s3_secret_key')
    sys.exit(1)

server = sys.argv[1]
db = sys.argv[2]
user = sys.argv[3]
passwd = sys.argv[4]
access_key = sys.argv[5]
secret_key = sys.argv[6]

dt = time.strftime("%d-%m-%Y")


proc = subprocess.Popen(['/usr/bin/mysqldump -h ' + server + ' -u' + user + ' -p' + passwd + ' ' + db + '|/bin/gzip > db_' + dt + '.sql.gz'], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

c = S3Connection(access_key, secret_key)
b = c.get_bucket('super234')
k = Key(b)
k.key = 'db_' + dt + '.sql.gz'
k.set_contents_from_filename('db_' + dt + '.sql.gz')

print(time.strftime("%d/%m/%Y"))



