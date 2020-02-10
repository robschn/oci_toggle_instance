import sys
import oci

def toggle_instance(state):

    config = oci.config.from_file()
    base_compute = oci.core.ComputeClient(config)

    instance_list = base_compute.list_instances(config['compartment_id']).data
    for instance in instance_list:
        try:
            if instance.freeform_tags['Test'] == 'Shutdown':
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
