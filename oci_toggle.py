import oci
import creds

config = {
    "user": creds.user_ocid,
    "key_file": creds.key_file,
    "fingerprint": creds.fingerprint,
    "tenancy": creds.tenancy,
    "pass_phrase": creds.pass_phrase,
    "region": creds.region
}

# set identity
identity = oci.identity.IdentityClient(config)

# set user
user = identity.get_user(config["user"]).data

# set base computer
base_compute = oci.core.compute_client.ComputeClient(config)

# set region
base_compute.base_client.set_region(config["region"])

# get instance list
instance_list = base_compute.list_instances(creds.compartment_id).data

print(instance_list)
