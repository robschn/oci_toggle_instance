import sys
import oci

def toggle_instance(state):
   
    # load config
    config = oci.config.from_file()
    # set compute resource
    base_compute = oci.core.ComputeClient(config)
    # get instance list
    instance_list = base_compute.list_instances(config['compartment_id']).data

    for instance in instance_list:
        # filter out any non Test Server types
        try:
            if instance.freeform_tags['Test'] == 'Shutdown':
                # send command passed through
                base_compute.instance_action(instance.id, state)
                print(f'Sending {state.upper()} command to {instance.display_name}...')
        except KeyError:
            pass

def main():

    if len(sys.argv) < 2:
        instance_state = 'start'
    else:
        instance_state = sys.argv[1]

    toggle_instance(instance_state)

if __name__ == "__main__":
    main()
