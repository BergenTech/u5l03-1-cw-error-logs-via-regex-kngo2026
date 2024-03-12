import json, csv, re
file_path = "logs.json"
file_path2 = "error_logs.csv"
with open(file_path, 'r') as file:
    content = json.load(file)
    for i in content:
        pattern = r"ERROR"
        string = i["level"]
        match = re.findall(pattern, string, re.IGNORECASE)
    with open(file_path2, 'w') as newFile:
        header = content[0].keys()
        dictionary = {}
        for x,y in enumerate(content):
            print(f"{x}: {y}")