import os


CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
DATA_PATH = os.path.join(CURRENT_PATH, '..', '..', 'data')

MODEL_DIRECTORIES = ['shape_models']
MODEL_TYPES = ['.pc']


def get_model_path(model_path):
    return os.path.join(DATA_PATH, model_path)


def list_models():
    model_paths = []
    for directory in MODEL_DIRECTORIES:
        directory_path = os.path.join(DATA_PATH, directory)
        for file in os.listdir(directory_path):
            is_file = os.path.isfile(os.path.join(directory_path, file))
            is_model = any(model_type in file for model_type in MODEL_TYPES)
            if is_file and is_model:
                model_paths.append(os.path.join(directory, file))
                
    for model_path in model_paths:
        print("\t" + model_path)
