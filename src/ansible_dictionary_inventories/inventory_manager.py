import os
import yaml

class InventoryManager():

    def __init__(self, inventory_file_path, inventory_dict={}):
        self.inventory_file_path = inventory_file_path
        self.inventory_dict = inventory_dict
    

    def set_inventory(self, inventory):
        self.inventory = inventory


    def write_inventory(self):
        with open(os.path.abspath(self.inventory_file_path), 'w') as fh:
            fh.write(yaml.dump(self.inventory_dict))


    def read_inventory(self):
        with open(os.path.abspath(self.inventory_file_path), 'r') as fh:
            self.inventory_dict = yaml.load(fh)
