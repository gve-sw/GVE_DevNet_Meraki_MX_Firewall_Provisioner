""" Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import meraki
import json
import config

dashboard = meraki.DashboardAPI(config.api_key,single_request_timeout=999999)

orgs = dashboard.organizations.getOrganizations()

for org in orgs:
    print("Organization name: " + str(org["name"]) + " | " + "ID: " + str(org["id"]))

org_id = input("Select an organization id: ")

networks = dashboard.organizations.getOrganizationNetworks(organizationId=org_id)

for network in networks:
    print("Network name: " + str(network["name"]) + " | " + "ID: " + str(network["id"]))

print("-------------------------------------")
breaker = "1"
networks_to_provision = []

while breaker == "1":
    net_id = input("Continue to add network IDs that you want to provision the MX (both l3 and l7), enter 0 when finished\n")

    if net_id == "0":
        breaker = "0"
        break

    networks_to_provision.append(net_id)

confirmation = input("press y to proceed all policy changes, BE SURE TO VERIFY JSON CONFIG FILES ")


for network in networks_to_provision:
  with open('firewall_rules/l7_rules.json') as f:
    new_l7_rules = json.load(f)
    update_l7_response = dashboard.appliance.updateNetworkApplianceFirewallL7FirewallRules(networkId=network,rules=new_l7_rules)

  with open('firewall_rules/l3_rules.json') as f:
    new_l3_rules = json.load(f)
    update_l3_response = dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(networkId=network,rules=new_l3_rules)
