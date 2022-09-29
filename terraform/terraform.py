import json
import subprocess


class Terraform:

    @staticmethod
    def get_plan_file_name():
        return "plan.tfplan"

    @staticmethod
    def generate_json_from_plan(tfplan_file_name):
        command = "terraform13 show -json {}".format(tfplan_file_name)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, err) = process.communicate()
        out_decoded = out.decode('utf-8')
        return json.loads(out_decoded)
