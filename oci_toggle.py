import oci
import creds

config = oci.config.from_file()

# set compute and region
base_compute = oci.core.compute_client.ComputeClient(config)
base_compute.base_client.set_region(config["region"])

# get instance list
instance_list = base_compute.list_instances(creds.compartment_id).data

print(instance_list)

# get instance_id of all instances with "Nightly/Weekend Shutdown" tag

    # shutdown the instance state

        # if RUNNING in lifecycle_state