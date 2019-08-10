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
Issue

This class represents only the additional parameters that ZenHub adds to
Github issues. It does not contain the Github information such as `title`
or `status`. You would need to combine this with a Github issue to get
all of the information.

Implements ths following ZenHub REST calls:

    Get Issue Data
        ``GET  /p1/repositories/:repo_id/issues/:issue_number``
    Get Issue Events
        ``GET  /p1/repositories/:repo_id/issues/:issue_number/events``
    Move an Issue Between Pipelines
        ``POST /p1/repositories/:repo_id/issues/:issue_number/moves``
    Set Issue Estimate
        ``PUT  /p1/repositories/:repo_id/issues/:issue_number/estimate``

Based on ZenHub API @ https://github.com/ZenHubIO/API
"""
import json

class Issue:
    """ Issue holds additional attributes that ZenHub adds to Issues """

    def __init__(self, issue_data, issue_number, repo):
        self.data = issue_data
        self._number = issue_number
        self.repo = repo
        self._estimate = issue_data.get('estimate')
        self.pipeline = issue_data['pipeline']
        self.is_epic = issue_data['is_epic']

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.number)

    def __str__(self):
        return '<%s %r>\n' % (type(self).__name__, self.number) + json.dumps(self.data, indent=4)

    @staticmethod
    def find(issue_number, repo):
        """ Creates a instance of an Issue given it's issue number

        :type issue_number: int
        :param issue_number: The number of the Issue you want to retrieve
        :type repo: :class:`zenhub.Issue`
        :param repo: The repository containing the Issue

        :calls: `GET /p1/repositories/:repo_id/issues/:issue_number <https://github.com/ZenHubIO/API#get-issue-data>`_

        :return: An instance of Issue or ``None`` if not found
        :rtype: :class:`zenhub.Issue` or ``None``

        """
        data = repo.zenhub.get(f"/p1/repositories/{repo.id}/issues/{issue_number}")
        if data:
            return Issue(data, issue_number, repo)
        return None

    @property
    def repo_id(self):
        """ Get the repositiry ID

        :return: The ID of the Github repository this Issue is in
        :rtype: int
        """
        return self.repo.id

    @property
    def number(self):
        """ Get the number for this Issue

        :return: The number of this Issue
        :rtype: int
        """
        return self._number

    @property
    def estimate(self):
        """ Returns the estimate for this Issue

        :return: The value of the estimate in story points
        :rtype: int

        """
        return self._estimate.get('value') or 0

    @estimate.setter
    def estimate(self, value):
        """ Creates or updates the estimate with the given value

        :type value: int
        :param value: the new value of the estimate in Story Points

        """
        self.repo.zenhub.put(
            f'/p1/repositories/{self.repo.id}/issues/{self.number}/estimate',
            {"estimate": value}
        )
        self._estimate = {'value': value}

    def events(self):
        """ Returns issue events, sorted by creation time, most recent first.

        :calls: `GET /p1/repositories/:repo_id/issues/:issue_number <https://github.com/ZenHubIO/API#get-issue-events>`_

        :return: Returns the events for this Issue as a dictionary
        :rtype: `dict`

        """
        return self.repo.zenhub.get(f'/p1/repositories/{self.repo.id}/issues/{self.number}/events')

    def move_to(self, pipeline_id, position='top'):
        """ Moves this Issue to another Pipeline

        :type pipeline_id: int
        :param pipeline_id: The ID of the pipeline you want to move the Issue to

        :type position: str
        :param position: The position as an int (0, 1, 2) or 'top' or 'bottom'

        """
        return self.repo.zenhub.post(
            f'/p1/repositories/{self.repo.id}/issues/{self.number}/moves',
            {
                "pipeline_id": pipeline_id,
                "position": position
            }
        )
