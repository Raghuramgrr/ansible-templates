import os

def create_folders_and_files(base_path):
    directories = [
        "group_vars",
        "host_vars",
        "inventory",
        "library",
        "module_utils",
        "playbooks",
        "roles/common/tasks",
        "roles/common/handlers",
        "roles/common/templates",
        "roles/common/files",
        "roles/common/vars",
        "roles/common/defaults",
        "roles/common/meta",
        "roles/common/tests",
        "roles/common/molecule/default",
        "roles/webserver/tasks",
        "roles/webserver/handlers",
        "roles/webserver/templates",
        "roles/webserver/files",
        "roles/webserver/vars",
        "roles/webserver/defaults",
        "roles/webserver/meta",
        "roles/webserver/tests",
        "roles/webserver/molecule/default"
    ]

    files = {
        "group_vars/all.yml": '''
# Group variables for all hosts
---
    ''',
        "host_vars/example_host.yml": '''
# Host variables for example_host
---
    ''',
        "inventory/hosts.ini": '''
# Inventory file
[webservers]
example_webserver

[dbservers]
example_dbserver
    ''',
        "playbooks/site.yml": '''
# Site playbook
---
- include: webservers.yml
- include: dbservers.yml
    ''',
        "playbooks/webservers.yml": '''
# Webservers playbook
---
- hosts: webservers
  roles:
    - webserver
    ''',
        "playbooks/dbservers.yml": '''
# DBservers playbook
---
- hosts: dbservers
  roles:
    - dbserver
    ''',
        "roles/common/tasks/main.yml": '''
# Tasks for common role
---
    ''',
        "roles/common/handlers/main.yml": '''
# Handlers for common role
---
    ''',
        "roles/common/templates/ntp.conf.j2": '''
# NTP configuration template
# Example template content
    ''',
        "roles/common/files/example.file": '''
# Example file for common role
    ''',
        "roles/common/vars/main.yml": '''
# Variables for common role
---
    ''',
        "roles/common/defaults/main.yml": '''
# Default variables for common role
---
    ''',
        "roles/common/meta/main.yml": '''
# Metadata for common role
---
    ''',
        "roles/common/tests/inventory": '''
# Inventory file for testing common role
    ''',
        "roles/common/tests/test.yml": '''
# Test playbook for common role
---
- hosts: localhost
  roles:
    - common
    ''',
        "roles/common/molecule/default/converge.yml": '''
# Molecule converge playbook
---
- name: Converge
  hosts: all
  roles:
    - role: common
    ''',
        "roles/common/molecule/default/molecule.yml": '''
# Molecule configuration
---
dependency:
  name: galaxy
driver:
  name: docker
platforms:
  - name: instance
    image: molecule_local/instance
    pre_build_image: true
provisioner:
  name: ansible
scenario:
  name: default
verifier:
  name: ansible
    ''',
        "roles/common/molecule/default/verify.yml": '''
# Molecule verify playbook
---
- name: Verify
  hosts: all
  tasks:
    - name: Check if file exists
      stat:
        path: /path/to/file
      register: result

    - name: Fail if file does not exist
      fail:
        msg: "File does not exist"
      when: not result.stat.exists
    ''',
        "roles/webserver/tasks/main.yml": '''
# Tasks for webserver role
---
    ''',
        "roles/webserver/handlers/main.yml": '''
# Handlers for webserver role
---
    ''',
        "roles/webserver/templates/webserver.conf.j2": '''
# Webserver configuration template
# Example template content
    ''',
        "roles/webserver/files/example.file": '''
# Example file for webserver role
    ''',
        "roles/webserver/vars/main.yml": '''
# Variables for webserver role
---
    ''',
        "roles/webserver/defaults/main.yml": '''
# Default variables for webserver role
---
    ''',
        "roles/webserver/meta/main.yml": '''
# Metadata for webserver role
---
    ''',
        "roles/webserver/tests/inventory": '''
# Inventory file for testing webserver role
    ''',
        "roles/webserver/tests/test.yml": '''
# Test playbook for webserver role
---
- hosts: localhost
  roles:
    - webserver
    ''',
        "roles/webserver/molecule/default/converge.yml": '''
# Molecule converge playbook
---
- name: Converge
  hosts: all
  roles:
    - role: webserver
    ''',
        "roles/webserver/molecule/default/molecule.yml": '''
# Molecule configuration
---
dependency:
  name: galaxy
driver:
  name: docker
platforms:
  - name: instance
    image: molecule_local/instance
    pre_build_image: true
provisioner:
  name: ansible
scenario:
  name: default
verifier:
  name: ansible
    ''',
        "roles/webserver/molecule/default/verify.yml": '''
# Molecule verify playbook
---
- name: Verify
  hosts: all
  tasks:
    - name: Check if file exists
      stat:
        path: /path/to/file
      register: result

    - name: Fail if file does not exist
      fail:
        msg: "File does not exist"
      when: not result.stat.exists
    ''',
        "ansible.cfg": '''
[defaults]
inventory = ./inventory/hosts.ini
roles_path = ./roles
library = ./library
module_utils = ./module_utils
    '''
    }

    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")

    for file_name, content in files.items():
        file_path = os.path.join(base_path, file_name)
        with open(file_path, "w") as file:
            file.write(content.strip())
            print(f"Created file: {file_path}")

if __name__ == "__main__":
    base_path = "ansible-project"
    create_folders_and_files(base_path)
    print("Ansible project structure has been created.")
