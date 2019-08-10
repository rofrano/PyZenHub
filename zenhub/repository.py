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
Repository Class

The module implements the calls to retrieve information about a ZenHub repository.

You can retrieve the following items:

    - Board
    - Issue {id}
    - Epics
    - Epic {id}

"""
from .issue import Issue
from .epic import Epic
from .board import Board
from .workspace import Workspace

class Repository:
    """ Represents a GitHub repository with a ZenHub Kanban Board """

    def __init__(self, repo_id, zenhub):
        self.id = repo_id
        self.zenhub = zenhub

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.id)

    def board(self):
        """ Get the ZenHub Board associated with this repository

        :return: :class:`Board <Board>` object
        :rtype: zenhub.Board

        """
        return Board.find(self)

    def issue(self, issue_id):
        """ Get a single Issue given it's ID

        :type issue_id: int
        :param issue_id: The ID of the Issue you want returned

        :return: :class:`Issue <Issue>` object
        :rtype: zenhub.Issue

        """
        return Issue.find(issue_id, self)

    def epics(self):
        """ Get a list of Epics for this repository

        This will retrieve all of the Epics in the repository.
        If there are no Epics, it will return an empty list ``[]``

        :return: a collection of Epics in this repo or ``[]`` if none found
        :rtype: list

        """
        epics_list = []
        data = self.zenhub.get(f"/p1/repositories/{self.id}/epics")
        if data:
            epics_list = [
                Epic(epic_data, epic_data['issue_number'], self)
                for epic_data in data['epic_issues']
            ]
        return epics_list

    def epic(self, epic_id):
        """ Get a single Epic given it's ID

        :type epic_id: int
        :param epic_id: The ID of the Epic you want returned

        :return: :class:`Epic <Epic>` object
        :rtype: zenhub.Epic or None

        """
        data = self.zenhub.get(f"/p1/repositories/{self.id}/epics/{epic_id}")
        if data:
            return Epic(data, epic_id=epic_id, repo=self)
        return None

    def workspaces(self):
        """
        Gets all Workspaces containing this repositories repo_id

        :calls: `GET /p2/repositories/:repo_id/workspaces <https://github.com/ZenHubIO/API#get-zenhub-workspaces-for-a-repository>`_

        :return: A list of Workspaces
        :rtype: list

        """
        workspace_list = []
        data = self.zenhub.get(f"/p1/repositories/{self.id}/workspaces")
        if data:
            workspace_list = [Workspace(workspace_data, self) for workspace_data in data]
        return workspace_list
