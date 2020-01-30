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

identity = oci.identity.IdentityClient(config)

user = identity.get_user(config["user"]).data
print(user)