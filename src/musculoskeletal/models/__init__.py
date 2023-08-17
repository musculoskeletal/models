import os
from pathlib import Path

_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

_MODEL_DIRECTORIES = ['shape_models']
_MODEL_TYPES = ['.pc']


def get_model_path(model_path):
    """
    Get the absolute path to a model from the given sub-path.
    Returns None if no model exists at the given path.

    :param model_path: Path-like object which is a sub-path to a model.
    :return: Absolute Path-like object to model, or None.
    """
    path = Path(os.path.join(_ROOT_PATH, model_path))
    return path if os.path.isfile(path) else None


def list_models(stdout=False):
    """
    Return a list of all available models, if not printing to stdout.
    If *stdout* is *True* then the list with be printed to stdout and None returned.

    :param stdout: Flag to print to stdout if True.
    :return: List of available models by sub-path, if stdout is False. Otherwise, None is returned.
    """
    model_paths = []
    for directory in _MODEL_DIRECTORIES:
        directory_path = os.path.join(_ROOT_PATH, directory)
        for dir_file in os.listdir(directory_path):
            is_file = os.path.isfile(os.path.join(directory_path, dir_file))
            is_model = any(model_type in dir_file for model_type in _MODEL_TYPES)
            if is_file and is_model:
                model_paths.append(Path(os.path.join(directory, dir_file)))

    if stdout:
        for model_path in model_paths:
            print(f"\t{model_path}")
    else:
        return model_paths
