from src.config import parameters_config as config


def retrieve_arguments(arguments):
    params = {"KEYWORD": None,
              "NUMBER_OF_PICTURES": config["DEFAULT_NUMBER_OF_PICTURES"]}
    if len(arguments) == 3:
        params["KEYWORD"] = arguments[1]
        params["NUMBER_OF_PICTURES"] = arguments[2]
        return params

    else:
        return params
