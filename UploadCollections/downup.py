import requests
import json
import base64
import urllib2


class Uploader(object):
    def __init__(self):
        self.exist_users = {}

    def create_user(self, json_node):
        author = json_node["author_name"]
        if author not in self.exist_users:
            r = requests.post('http://CopyCatLoadBalancer-426137485.us-east-1.elb.amazonaws.com/api/v0/users/',
                              data=json.dumps({'name': author, 'profilePictureUrl': json_node["author_profile"]}),
                              headers={'content-type': 'application/json'})
            try:
                author_id = r.json()['_id']
                self.exist_users[author] = author_id
            except KeyError:
                print "created user failed: " + author

    def upload_photo(self, json_node):
        image_src = json_node["src"]
        response = urllib2.urlopen(image_src)
        buf = base64.b64encode(response.read())
        oid = self.exist_users.get(json_node['author_name'], "")
        r = requests.post('http://CopyCatLoadBalancer-426137485.us-east-1.elb.amazonaws.com/api/v0/photos/',
                          data=json.dumps({'data': buf, 'ownerId': oid}),
                          headers={'content-type': 'application/json', 'content-length': len(buf)})
        print r.text

    def process(self, json_node):
        self.create_user(json_node)
        self.upload_photo(json_node)
