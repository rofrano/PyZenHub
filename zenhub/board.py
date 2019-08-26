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
ZenHub Kanban Board

A Board consists of multiple Pipelines and each Pipeline contains a collection
of Issues that are currently in that Pipeline.

Implements the following ZenHub REST calls:

    Get Board Data for a Repository
        ``GET  /p1/repositories/:repo_id/board``

Based on ZenHub API @ https://github.com/ZenHubIO/API
"""

import json
from .pipeline import Pipeline

class Board:
    """ Represents a Kanban Board in ZenHub """

    def __init__(self, data, repo):
        self.data = data
        self.repo = repo

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.repo.id)

    def __str__(self):
        return '<%s %r>\n' % (type(self).__name__, self.repo.id) + json.dumps(self.data, indent=4)

    @staticmethod
    def find(repo):
        """ Constructs and returns a :class:`Board <Board>`.

        :type: :class:`zenhub.Repo`
        :param repo: The ``Repo`` class for this board

        :calls: `GET /p1/repositories/:repo_id/board <https://github.com/ZenHubIO/API#get-epic-data>`_

        :return: The Board class that represents the kanban board
        :rtype: :class:`zenhub.Board`

        """
        data = repo.zenhub.get(f"/p1/repositories/{repo.id}/board")
        if data:
            return Board(data, repo)
        return None

    def pipelines(self):
        """ Returns the Pipelines that are in this Board or an empty list

        :return: A list of Pipeline objects
        :rtype: list

        """
        return [Pipeline(pipeline, self.repo) for pipeline in self.data['pipelines']]

    def pipeline(self, name):
        """ Returns a single Pipelines by name or ``None`` if not found

        :type name: string
        :param name: The name of the Pipeline you want to return

        :return: The Pipeline with that name or ``None`` if not found
        :rtype: :class:`zenhub.Pipeline` or ``None``

        """
        next((pipeline for pipeline in self.pipelines() if pipeline.name == name), None)
