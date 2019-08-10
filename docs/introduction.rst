Introduction
============

PyZenHub is a Python 3 library for `ZenHub <http://zenhub.com>`__.
It uses the `ZenHub API <https://github.com/ZenHubIO/API>`__.
With it, you can manage your ZenHub Kanban board
(pipelines, epics, issues, etc.) from Python scripts.

Should you have any question, any remark, or if you find a bug,
or if there is something you can do with the API but not with PyZenHub,
please `open an issue <https://github.com/rofrano/PyZenHub/issues>`__.

Download and install
--------------------

.. code-block:: sh

    pip install pyzenhub

This package is in the `Python Package Index
<http://pypi.python.org/pypi/PyZenHub>`__, so ``pip install PyZenHub`` should
be enough.  You can also clone it on `Github
<http://github.com/rofrano/PyZenHub>`__.

Generate a ZenHub Token
-----------------------

The ZenHub API requires access tokens for authentication so you must create an
access token before you can use the API and this before you can use PyZenHub as
well.

For Public ZenHub you can generate an api token here:

  https://api.zenhub.io/app/dashboard/tokens

For Enterprise ZenHub you can generate an api token here:

  https://<zenhub_enterprise_host>/app/dashboard/tokens

Licensing
---------

PyZenHub is licensed under the Apache License, Version 2.0 (the "License");
you may not use this code except in compliance with the License.
You may obtain a copy of the License at:

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
