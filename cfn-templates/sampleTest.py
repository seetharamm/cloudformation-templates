import sys
client = boto3.client("s3")

response = client.list_objects_v2(Bucket='azdo-cfn-price-merch-dev-us-east-1', Prefix="deployment/cloudformation/dev/")
files_in_folder = response["Contents"]
files_to_delete = []
    # We will create Key array to pass to delete_objects function
for f in files_in_folder:
    files_to_delete.append({"Key": f["Key"]})
    # This will delete all files in a folder
    response = s3_client.delete_objects(
        Bucket=bucket_name, Delete={"Objects": files_to_delete}
    )
    print(response)