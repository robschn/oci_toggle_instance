import sys
import oci
import creds

# make sure user is providing instance action
# if len(sys.argv) < 2:
#     print("No instance action provided. Please add 'start' or 'stop' after the script.")
#     exit()

config = oci.config.from_file()

# set compute resource
base_compute = oci.core.ComputeClient(config)

# get instance list
instance_list = base_compute.list_instances(creds.compartment_id).data


for instance in instance_list:
    # filter out any non Test Server types
    try:
        if instance.freeform_tags['Test'] == 'Shutdown':
            print(instance.display_name, instance.freeform_tags)
            # send command passed through
            # base_compute.instance_action(instance.id, f'{sys.argv[1]}')
            # print(f'Sending {sys.argv[1]} command to {instance.display_name}...')

    except KeyError:
        pass
