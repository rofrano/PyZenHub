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
ZenHub Workspace

Based on ZenHub API @ https://github.com/ZenHubIO/API
"""

import json
from .board import Board

class Workspace:
    """ ZenHub Workspace for a repository

    Example JSON:
    [
        {
            "name": null,
            "description": null,
            "id": "57e2f42c86e6ae285942419d",
            "repositories": [
                68837948
            ]
        }
    ]

    """

    def __init__(self, data, repo):
        self.data = data
        self.repo = repo

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.repo.id)

    def __str__(self):
        return '<%s %r>\n' % (type(self).__name__, self.repo.id) + json.dumps(self.data, indent=4)

    @property
    def name(self):
        """
        :type: string
        """
        try:
            return self.data['name']
        except KeyError:
            return None

    @property
    def description(self):
        """
        :type: string
        """
        try:
            return self.data['description']
        except KeyError:
            return None

    @property
    def id(self):
        """
        :type: int
        """
        try:
            return self.data['id']
        except KeyError:
            return None

    @property
    def repositories(self):
        """
        :type: list
        """
        try:
            return self.data['repositories']
        except KeyError:
            return []

    def board(self):
        """
        Get ZenHub Board data for a repository (repo_id) within the Workspace (workspace_id)

        :calls: `GET /p2/workspaces/:workspace_id/repositories/:repo_id/board
                <https://github.com/ZenHubIO/API#get-a-zenhub-board-for-a-repository>`_

        :return: :class:`Board <Board>` object
        :rtype: :class:`zenhub.Board`

        """
        data = self.repo.zenhub.get(f'/p2/workspaces/{self.id}/repositories/{self.repo.id}/board')
        if data:
            return Board(data, self.repo)
        return None
