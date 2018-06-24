def retrieve_arguments(arguments):
    if len(arguments) == 3:
        params = {"KEYWORD": arguments[1],
                  "NUMBER_OF_PICTURES": arguments[2]}
        return params

    else:
        return None
