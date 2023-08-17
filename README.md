# Models

A collection of musculoskeletal principal component models, used by the GIAS3 Python package.

## Usage

    import musculoskeletal.models as mm
    # Get a list of available models.
    model_listing = mm.list_models()
    # Print out a list of available models to stdout.
    mm.list_models(True)
    # Get the absolute path to a model.
    model_path = mm.get_model_path("shape_models/LLP26_rigid.pc")
