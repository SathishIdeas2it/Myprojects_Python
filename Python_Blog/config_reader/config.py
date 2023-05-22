import tomli as tomllib

def read_config(property):
    with open("static/config.toml","rb") as file:
        data = tomllib.load(file)
    return data[property]

    