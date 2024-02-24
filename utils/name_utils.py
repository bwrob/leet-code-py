def name_to_python_file_name(name: str) -> None:
    filename = name.lower().replace(" ", "_").replace(".", "")
    return print(f"{filename}.py")


topy = name_to_python_file_name
