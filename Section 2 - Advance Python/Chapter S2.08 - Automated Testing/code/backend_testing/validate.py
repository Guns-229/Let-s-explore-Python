data = [{
    "status": "READY",
    "isCompleted": "False",
    "description": "Provision a target. Hypervisor imaging and optional Dummy cluster creation for Kvm",
    "tags": ["Imaging", "Imaging"],
    "presetId": "testing.imaging:kvm",
    "requiredHypervisors": ["kvm"],
    "userInput": [{
        "supported": "True",
        "required": "True",
        "type": "dropdown"
    }, {
        "supported": "True",
        "required": "True",
        "type": "file"
    }, {
        "supported": "True",
        "required": "True",
        "type": "textbox"
    }],
    "supportedHypervisors": ["kvm", "esx", "hyperv"],
    "percentComplete": 0.0,
    "startTime": 0,
    "duration": 2400,
    "targets": [{
        "name": "tar_1561033116",
        "uuid": "b1cb802c-66df-4fc0-967c-9ade2a8f2265"
    }],
    "target": {
        "hclJson": {
            "uuid": "test",
            "fileName": "asteast"
        },
        "isSubtarget": "False",
        "name": "tar_1561033116",
        "scvmm": {
            "username": "",
            "container": "metis-container",
            "network": "ExternalSwitch",
            "ip": "",
            "cluster": "tar_1561033116-Cluster",
            "libraryServer": "vlan0",
            "password": ""
        },
        "hypervisor": {
            "username": "ADMIN",
            "netmask": "10.2.208.1",
            "password": "ADMIN",
            "gateway": "255.255.240.0"
        },
        "notes": "",
        "uuid": "b1cb802c-66df-4fc0-967c-9ade2a8f2265",
        "virtualIp": "1.2.3.4",
        "prism": {
            "username": "admin",
            "container": "metis-container",
            "network": "vlan0",
            "ip": "1.2.3.4",
            "cluster": "tar_1561033116-Cluster",
            "password": ""
        },
        "nodes": [{
            "hypervisor": {
                "ip": "10.2.209.136"
            },
            "uuid": "",
            "svm": {
                "ip": "10.2.209.140"
            },
            "name": "1",
            "ipmi": {
                "ip": "10.2.131.1"
            }
        }, {
            "hypervisor": {
                "ip": "10.2.209.137"
            },
            "uuid": "",
            "svm": {
                "ip": "10.2.209.141"
            },
            "name": "2",
            "ipmi": {
                "ip": "10.2.131.2"
            }
        }, {
            "hypervisor": {
                "ip": "10.2.209.138"
            },
            "uuid": "",
            "svm": {
                "ip": "10.2.209.142"
            },
            "name": "3",
            "ipmi": {
                "ip": "10.2.131.3"
            }
        }],
        "ipmi": {
            "username": "ADMIN",
            "netmask": "10.2.128.1",
            "password": "ADMIN",
            "gateway": "255.255.240.0"
        },
        "isArchived": "False",
        "pdu": {
            "args": ""
        },
        "hwRevision": 0,
        "vcenter": {
            "username": "administrator@vsphere.local",
            "dataCenter": "tar_1561033116-DC",
            "container": "metis-container",
            "network": "VM Network",
            "ip": "",
            "cluster": "tar_1561033116-Cluster",
            "dataStore": "tar_1561033116-DS",
            "password": ""
        },
        "dnsServerIp": "1.2.3.4",
        "layoutModule": {
            "uuid": "",
            "fileName": ""
        },
        "revision": 0
    },
    "displayName": "Imaging to Kvm",
    "uuid": "99ab947f-f2e5-4719-a9cc-8fa0da0a0bde",
    "hypervisor": "kvm",
    "createTime": 1561053275982.417,
    "options": {},
    "mode": "imaging",
    "timeout": 10,
    "supportedOptions": [{
        "default": "True",
        "text": "Should target HW be discovered prior to imaging",
        "required": "False",
        "external": "False",
        "mutable": "False",
        "type": "bool",
        "id": "fingerprint_hw"
    }, {
        "default": "False",
        "text": "Should a cluster be created from the imaged nodes?",
        "required": "False",
        "external": "False",
        "mutable": "False",
        "type": "bool",
        "id": "create_cluster"
    }, {
        "default": "None",
        "text": "A regex for selecting the Phoenix ISO by file name",
        "required": "False",
        "external": "False",
        "mutable": "False",
        "type": "basestring",
        "id": "phoenix_iso"
    }, {
        "default": "",
        "text": "Should a cluster be created from the imaged nodes?",
        "required": "False",
        "external": "False",
        "mutable": "False",
        "type": "basestring",
        "id": "hypervisor_type"
    }, {
        "default": "None",
        "text": "The path to a custom Phoenix layout module",
        "required": "False",
        "external": "False",
        "mutable": "False",
        "type": "basestring",
        "id": "layout_module"
    }, {
        "default": "None",
        "text": "The path to a custom Phoenix HCL file",
        "required": "False",
        "external": "False",
        "mutable": "False",
        "type": "basestring",
        "id": "hcl_file"
    }, {
        "default": "None",
        "text": "The address of the testing server",
        "required": "True",
        "external": "False",
        "mutable": "False",
        "type": "basestring",
        "id": "testing_host"
    }, {
        "default": "None",
        "text": "Values to set / override in the generated imaging config. See the testing REST API doc for more info",
        "required": "False",
        "external": "False",
        "mutable": "False",
        "type": "dict",
        "id": "config_overlay"
    }, {
        "default": "None",
        "text": "A regex for selecting the hypervisor ISO by file name",
        "required": "False",
        "external": "False",
        "mutable": "False",
        "type": "basestring",
        "id": "hypervisor_iso"
    }, {
        "default": "None",
        "text": "MetisTarget to be imaged",
        "required": "False",
        "external": "False",
        "mutable": "False",
        "type": "dict",
        "id": "target"
    }, {
        "default": "None",
        "text": "A regex for selecting the NOS package by file name",
        "required": "False",
        "external": "False",
        "mutable": "False",
        "type": "basestring",
        "id": "nos_package"
    }, {
        "default": "/home/Dummy/testing",
        "text": "The dir in the testing VM that contains testing",
        "required": "True",
        "external": "False",
        "mutable": "False",
        "type": "basestring",
        "id": "testing_dir"
    }],
    "endTime": 0,
    "requires": [{
        "type": "TARGET",
        "constraint": {
            "attribute": "nodes",
            "type": "COUNT",
            "value": 2,
            "op": "GT"
        }
    }],
    "projectUuid": "8e27ea4c-c212-41c7-a60f-f445b57af118"
}]


def _validate_key(data, keys, expected_value):
    def _get_value(data, keys):
        for key in keys.split(":"):
            if isinstance(data, dict):
                data = data.get(key, None)
            elif isinstance(data, list):
                for v in data:
                    data = _get_value(v, key)
            if data is None:
                return False
        return data
    return expected_value == _get_value(data, keys)

# key = "target:hclJson:uuid"
key = "supportedOptions:text"
expected_value = "The dir in the testing VM that contains testing"
print(_validate_key(data, key, expected_value))
