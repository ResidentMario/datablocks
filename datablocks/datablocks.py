import datapackage


class DataBlock:
    def __init__(self, name, local, remote, additional_fields):
        dp = datapackage.DataPackage()
        dp.descriptor['name'] = name
        dp.descriptor['resources'] = [{'name': 'test_name'}]
        self.dp = dp

    def to_json(self):
        return self.dp.to_json()
