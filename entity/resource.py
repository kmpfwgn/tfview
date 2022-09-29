class Resource:

    def __init__(self, json):
        self.json = json
        self.address = json['address']
        self.actions = json['change']['actions']

        self.fields_to_update = []
        if "update" in self.actions:
            change_before = json['change']['before']
            change_after = json['change']['after']

            for key in change_before:
                if change_before[key] != change_after[key]:
                    self.fields_to_update.append(key)

    def get_old_field_value(self, field):
        return self.json['change']['before'][field]

    def get_new_field_value(self, field):
        return self.json['change']['after'][field]
