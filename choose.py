from kubernetes import config
from helpers.objectize import objectize
import os


def choose_k8s_context() -> None:
    '''
    Function to show all kubernetes context in the ~/.kube/config and loaded it
    '''

    context_list, _ = objectize(config.list_kube_config_contexts())

    n = 0

    list_context = []

    for settings in context_list:
        contexts = settings.context.cluster
        list_context.append(contexts)

        print(f"{n}-{contexts}")

        n = n + 1

    try:
        choosed_context = int(input("Choose one context to load according to the number.: "))

        os.system(f"kubectl config use-context {list_context[choosed_context]}")
        print(f"Context loaded: {list_context[choosed_context]}")
    except KeyboardInterrupt:
        print("\nExecution interrupted by keyboard user!")
