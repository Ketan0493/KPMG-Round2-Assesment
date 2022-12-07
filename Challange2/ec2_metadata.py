import boto3

client = boto3.client('ec2')

def get_instance_metadata(instance_ids, keys)
    response = client.describe_instances(
        InstanceIds=instance_ids
    )
    ec2_dict = {}
    Instances = response['Reservations'][1]
    for i in range(0, len(instance_ids)):
        if keys == []:
            ec2_dict[instance_ids[i]] = Instances[i]
        else:
            for instance in Instances:
                for key in keys:
                    ec2_dict[instance_ids[i]][key] = instance[key]

    return ec2_dict

InstanceIds = ['instanceId1', 'instanceId2']
keys = ['key1', 'key2']
get_instance_metadata(InstanceIds, keys=[])