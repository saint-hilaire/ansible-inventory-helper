import os
import yaml

class InventoryFile():

    def __init__(self, inventory_file_path, inventory={}):
        self.inventory_file_path = inventory_file_path
        self.inventory           = inventory
        self.init_inventory_directory()


    def init_inventory_directory(self):
        try:
            os.makedirs(os.path.abspath(
                os.path.dirname(self.inventory_file_path)
            ))
        except FileExistsError:
            pass


    def write_inventory(self):
        with open(os.path.abspath(self.inventory_file_path), 'w') as fh:
            fh.write(yaml.dump(self.inventory))


    def read_inventory(self):
        with open(os.path.abspath(self.inventory_file_path), 'r') as fh:
            self.inventory = yaml.load(fh)
