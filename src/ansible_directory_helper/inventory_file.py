import os
import yaml
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager

class InventoryFile():

    # def __init__(self, inventory_path, inventory={}):
    def __init__(self, file_path):
        self.file_path = file_path
        self.inventory_manager = InventoryManager(
            loader=DataLoader(),
            parse=False
        )
        self.init_file_handle()


    def init_file_handle(self):
        try:
            os.makedirs(os.path.abspath(
                os.path.dirname(self.file_path)
            ))
        except FileExistsError:
            pass

        self.file_handle = open(self.file_path, 'w')


    def write_inventory(self):
        # with open(os.path.abspath(self.inventory_file_path), 'w') as fh:
        #     fh.write(yaml.dump(self.inventory))
        # import pdb; pdb.set_trace()
        # !!
        groups = self.inventory_manager.get_groups_dict()
        for group in groups.keys():
            # TODO??
            if group in ['all', 'ungrouped']:
                continue
            hosts = self.inventory_manager.get_hosts(group)
            for host in hosts:
                import pdb; pdb.set_trace()
                # Like this?
                host_data = host.__dict__
                # Should be something like this now
                # {'_uuid': 'asdf-123',
                #     'address': 'example.com',
                #     'groups': [web_servers, database_servers],
                #     'implicit': False,
                #     'name': 'example.com',
                #     'vars': {'ansible_user': 'root',
                #              'inventory_dir': None,
                #              'inventory_file': None}}
                from pprint import pprint
                # This works :D
                pprint(host.address)
                pprint(host.vars)


        self.file_handle.write(yaml.dump({'foo': 'bar'}))


    def read_inventory(self):
        # with open(os.path.abspath(self.inventory_file_path), 'r') as fh:
        #     self.inventory = yaml.load(fh)
        self.inventory = yaml.load(self.file_handle)


    def add_groups(self, groups):
        if isinstance(groups, str):
            groups = [groups]

        for group in groups:
            self.inventory_manager.add_group(group)


    def add_host(self, host, group=None, port=None):
        self.inventory_manager.add_host(host, group, port)


    # TODO: Not working?
    def set_variable(self, host, varname, value):
        import pdb; pdb.set_trace()
        self.inventory_manager._inventory.set_variable(host, varname, value)

    def set_ansible_user(self, host, username):
        self.set_variable(host, 'ansible_user', username)
