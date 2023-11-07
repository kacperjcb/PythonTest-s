def group_files_by_extension(file_names):
    file_groups = {}

    for file_name in file_names:

        parts = file_name.split('.')
        if len(parts) == 2:
            name, extension = parts
        else:

            name = file_name
            extension = ""


        if extension in file_groups:
            file_groups[extension].append(file_name)
        else:
            file_groups[extension] = [file_name]

    return file_groups



file_names = ["plik1.jpg", "plik2.gif", "plik3.mid", "plik4.jpg"]
result = group_files_by_extension(file_names)


for extension, files in result.items():
    print(f"{extension}: {', '.join(files)}")
