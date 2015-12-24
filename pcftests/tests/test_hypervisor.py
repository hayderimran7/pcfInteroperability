# Copyright 2013 IBM Corporation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.api.compute import base
from tempest import test


class HypervisorAdminTestJSON(base.BaseV2ComputeAdminTest):
    """Tests Hypervisors API that require admin privileges"""

    @classmethod
    def setup_clients(cls):
        super(HypervisorAdminTestJSON, cls).setup_clients()
        cls.client = cls.os_adm.hypervisor_client

    def test_get_hypervisor_type(self):
        # Verify that all hypervisors are KVM-based
        hypers = self.client.list_hypervisors()['hypervisors']
        for hyper in hypers:
            details = (self.client.show_hypervisor(hypers[0]['id'])
                       ['hypervisor'])
            self.assertEqual('KVM', details['hypervisor_type'])
