from downup import Uploader
import parse_collection as ps

collections = []

with open("collections.txt", "r") as cl:
    lines = cl.readlines()
    for line in lines:
        collections.append(line.strip())

upload = Uploader()

for collection in collections:
    url = "https://unsplash.com/collections/%s" % collection.strip()
    json_list = ps.generate_json(url)
    for node in json_list:
        upload.process(node)
