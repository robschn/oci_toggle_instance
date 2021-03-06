import sys
import logging
import oci


def toggle_instance(state, key, value):
    """Toggle the instance base on tags set in OCI

    Args:
        state: the desired state of the instance
        key: the tag key set in OCI
        value: the value of the tag key that you want selected

    Returns:
        log file with the instance names and their new state

    """
    logging.basicConfig(filename='instance_log.txt',
                        filemode='a',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)

    config = oci.config.from_file()
    base_compute = oci.core.ComputeClient(config)

    instance_list = base_compute.list_instances(config['compartment_id']).data
    for instance in instance_list:
        try:
            if instance.freeform_tags[key] == value:
                base_compute.instance_action(instance.id, state)
                logging.info(
                    f' {instance.display_name.upper()} set to {state.upper()}')
        except KeyError:
            pass


def main():

    if len(sys.argv) < 2:
        instance_state = 'stop'
    else:
        instance_state = sys.argv[1]

    toggle_instance(instance_state, 'Test', 'Shutdown')


if __name__ == "__main__":
    main()
