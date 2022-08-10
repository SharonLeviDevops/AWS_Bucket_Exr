import boto3

# Creating S3 Resource From the Session.
s3 = boto3.resource('s3')

srcbucket = s3.Bucket('sharon.bucket1')

destbucket = s3.Bucket('sharon.bucket2')

# Iterate All Objects in Your S3 Bucket Over the for Loop
for file in srcbucket.objects.all():
    # Create a Soucre Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
    copy_source = {
        'Bucket': 'sharon.bucket1',
        'Key': file.key
    }

    destbucket.copy(copy_source, file.key)

    print(file.key + '- File Copied')