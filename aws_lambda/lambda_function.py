import boto3


def get_ec2_instance_name(tag_list):
    for tag in tag_list:
        if tag["Key"] == "Name":
            return tag["Value"]
    return ""


def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('ec2')
    ec2_data = client.describe_instances()
    for ec2_reservation in ec2_data['Reservations']:
        for ec2_instance in ec2_reservation['Instances']:

            ec2_instance_id = ec2_instance['InstanceId']
            ec2_instance_name = get_ec2_instance_name(ec2_instance['Tags'])
            ec2_instance_state = ec2_instance['State']['Name']

            if ec2_instance_state == 'running':
                # get ec2 info
                print("running ec2:" + ec2_instance_name
                      + "(" + ec2_instance_id + ")")

                # ec2 stop
                client.stop_instances(InstanceIds=[ec2_instance_id])
    return {
        'statusCode': 200,
    }
