# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 John J. Rofrano <rofrano@gmail.com>
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
ZenHub Pipeline

This class represents a single Pipeline on the ZenHub Kanban Board.

"""
# Sample data:
#     {
#         "id": "57e2f42c86e6ae28594241a3",
#         "name": "New Issues",
#         "issues": [
#             {
#                 "issue_number": 4,
#                 "is_epic": false,
#                 "position": 0
#             }
#         ]
#     }

import json

class Pipeline:
    """ Represents a Pipeline in a ZenHub Board """

    def __init__(self, data, repo):
        self.data = data
        self.repo = repo
        self.id = data['id']
        self.name = data['name']
        self.issues = data['issues']

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.id)

    def __str__(self):
        return '<%s %r>\n' % (type(self).__name__, self.id) + json.dumps(self.data, indent=4)
