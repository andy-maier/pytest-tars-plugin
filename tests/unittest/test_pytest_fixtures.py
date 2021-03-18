# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test the _pytest_fixtures.py module.
"""

from __future__ import absolute_import, print_function
from client_end2end_tester import ServerDefinition
# pylint: disable=unused-import
from client_end2end_tester import server_definition  # noqa: F401


# pylint: disable=redefined-outer-name
def test_ptf_sample1(server_definition):
    """
    Test using the server_definition fixture.

    Parameters:
      server_definition (ServerDefinition): A server definition
    """
    assert isinstance(server_definition, ServerDefinition)

    # This test uses the default server definition file, so we expect the
    # default servers defined in that file:
    exp_nicks = ['myserver1', 'myserver2']

    assert server_definition.nickname in exp_nicks