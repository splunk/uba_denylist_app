import os
import json
from flask import Flask, request
from flask_autoindex import AutoIndex


app = Flask(__name__)

BASEDIR = os.path.abspath(os.path.dirname(__file__))
FILES_PATH = os.path.join(BASEDIR, "files")
IP_FILE = os.path.join(FILES_PATH, "ip_blacklist.txt")
DOMAIN_FILE = os.path.join(FILES_PATH, "domain_blacklist.txt")

FILES_INDEX = AutoIndex(app, FILES_PATH, add_url_rules=False)

def write_file(filename, content):
    with open(filename, "w") as f:
        # Writing data to a file
        print(f"content: {content}")
        f.write(content)
        print("done")

# Expose the ip_blacklist.txt and domain_blacklist.txt with GET method
@app.route("/denylist/")
@app.route("/denylist/<path:path>")
def autoindex(path="."):
    print(f"path: {path}")
    return FILES_INDEX.render_autoindex(path)


# Update ip_blacklist.txt
@app.route("/denylist/ip_blacklist.txt", methods=["PATCH", "PUT"])
def update_ip_blacklist():
    print(request.json)
    write_file(IP_FILE, request.json["files"]["ip_blacklist.txt"]["content"])
    return "Successfully updated ip_blacklist.txt"
    

# Update domain_blacklist.txt
@app.route("/denylist/domain_blacklist.txt", methods=["PATCH", "PUT"])
def update_domain_blacklist():
    print(request.json)
    write_file(DOMAIN_FILE, request.json["files"]["domain_blacklist.txt"]["content"])
    return "Successfully updated domain_blacklist.txt"


@app.route("/")
def hello():
    return "Hello World!"
    
def main():
    app.run()
    
if __name__ == "__main__":
    main()