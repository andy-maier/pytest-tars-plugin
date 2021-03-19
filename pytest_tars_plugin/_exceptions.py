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
Exceptions used by the project.
"""

from __future__ import absolute_import, print_function

__all__ = ['ServerDefinitionFileException', 'ServerDefinitionFileNotFound',
           'ServerDefinitionFileFormatError']


class ServerDefinitionFileException(Exception):
    """
    Abstract base exception for errors related to server definition files.

    Derived from :exc:`py:Exception`.
    """
    pass


class ServerDefinitionFileNotFound(ServerDefinitionFileException):
    """
    Exception indicating that a server definition file was not found or cannot
    be accessed due to a permission error.

    Derived from :exc:`ServerDefinitionFileException`.
    """
    pass


class ServerDefinitionFileFormatError(ServerDefinitionFileException):
    """
    Exception indicating that an existing server definition file has some
    issue with the format of its file content.

    Derived from :exc:`ServerDefinitionFileException`.
    """
    pass