class Page:

    def __init__(self, resources):
        self.resources = resources
        self.html = ""

    def generate(self):
        self.html = "<table border=\"1px solid black\"><tr><th>Create</th><th>Update</th><th>Delete</th></tr>"
        for resource in self.resources:
            if "create" in resource.actions:
                self.html += "<tr><th>{}</th><th></th><th></th></tr>".format(resource.address)
            if "update" in resource.actions:
                self.html += "<tr><th></th><th>{}</th><th></th></tr>".format(resource.address)
            if "delete" in resource.actions:
                self.html += "<tr><th></th><th></th><th>{}</th></tr>".format(resource.address)
        self.html += "</table>"
