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

import mock
import json

from osc_lib.tests import utils

lease_availabilities = "[]"
lease_end_time = "3000-00-00T13"
lease_project_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
lease_properties = "{}"
lease_resource_type = "dummy_node"
lease_resource_uuid = "1213123123"
lease_start_time = "2010"
lease_status = "fake_status"
lease_contract_uuid = "9999999"
lease_offer_uuid = "111111111"

OFFER = {
    'availabilities': json.loads(lease_availabilities),
    'end_time': lease_end_time,
    'project_id': lease_project_id,
    'properties': json.loads(lease_properties),
    'resource_type': lease_resource_type,
    'resource_uuid': lease_resource_uuid,
    'start_time': lease_start_time,
    'status': lease_status,
    'uuid': lease_offer_uuid
}

CONTRACT = {
    'end_time': lease_end_time,
    'offer_uuid': lease_offer_uuid,
    'project_id': lease_project_id,
    'properties': json.loads(lease_properties),
    'start_time': lease_start_time,
    'status': lease_status,
    'uuid': lease_contract_uuid
}


class TestLease(utils.TestCommand):

    def setUp(self):
        super(TestLease, self).setUp()

        self.app.client_manager.auth_ref = mock.Mock(auth_token="TOKEN")
        self.app.client_manager.lease = mock.Mock()


class FakeLeaseResource(object):
    def __init__(self, manager, info):
        self.__name__ = type(self).__name__
        self.manager = manager
        self._info = info
        self._add_details(info)

    def _add_details(self, info):
        for (k, v) in info.items():
            setattr(self, k, v)
