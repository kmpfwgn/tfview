import os
import sys

from entity import *
from terraform import *
from web import *

if __name__ == '__main__':
    print("execute from main")
    tfplan_file_name = Terraform.get_plan_file_name()
    json = Terraform.generate_json_from_plan(tfplan_file_name)

    resources = []
    for entry in json['resource_changes']:
        resources.append(Resource(entry))

    page = Page(resources)
    page.generate()
    print(page.html)
