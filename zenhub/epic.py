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
Epic

A Epic is a collection of Issues that implement functionality that is
larger than a single User Story

This class implements the following ZenHub REST calls:

    Get Epics for a Repository
        GET    /p1/repositories/:repo_id/epics
    Get Epic Data
        GET    /p1/repositories/:repo_id/epics/:epic_id
    Convert an Epic to an Issue
        POST   /p1/repositories/:repo_id/epics/:issue_number/convert_to_issue
    Convert an Issue to Epic
        POST   /p1/repositories/:repo_id/issues/:issue_number/convert_to_epic
    Add or Remove Issues from an Epic
        POST   /p1/repositories/:repo_id/epics/:issue_number/update_issues

Based on ZenHub API @ https://github.com/ZenHubIO/API

"""
import json
from .issue import Issue

class Epic:
    """
    A Epic is a collection of Issues that implement functionality that is
    larger than a single User Story
    """

    def __init__(self, epic_data, epic_id, repo):
        self.repo = repo
        self.id = epic_id
        self.data = epic_data

    def __repr__(self):
        return '<%s %r>' % (type(self).__name__, self.id)

    def __str__(self):
        return '<%s %r>\n' % (type(self).__name__, self.id) + json.dumps(self.data, indent=4)

    @property
    def estimate(self):
        """ the Estimate of the Epic """
        try:
            return self.data['estimate']['value']
        except KeyError:
            return 0

    @property
    def total_epic_estimates(self):
        """
        the total Epic Estimate value (the sum of all the Estimates of Issues contained
        within the Epic, as well as the Estimate of the Epic itself)
        """
        try:
            return self.data['total_epic_estimates']['value']
        except KeyError:
            return 0

    @property
    def pipeline(self):
        try:
            return self.data['pipeline']
        except KeyError:
            return None

    @property
    def pipelines(self):
        try:
            return self.data['pipelines']
        except KeyError:
            return []

    @property
    def issues(self):
        try:
            return self.data['issues']
        except KeyError:
            return []


    @staticmethod
    def find(epic_id, repo):
        """ Finds an Epic given it's ID

        :type epic_id: int
        :param epic_id: The ID of the Epic you want to retrieve
        :type repo: :class:`zenhub.Repository`
        :param repo: The repository the Epic is in

        :calls: `GET /p1/repositories/:repo_id/epics/:epic_id <https://github.com/ZenHubIO/API#get-epic-data>`_

        :return: An instance of an Epic or ``None`` if not found
        :rtype: :class:`zenhub.Epic` or ``None``

        """
        data = repo.zenhub.get(f'/p1/repositories/{repo.id}/epics/{epic_id}')
        if data:
            return Epic(data, epic_id, repo)
        return None


    # def issues(self):
    #     return [
    #         self.repo.zenhub.repository(issue_data['repo_id']).issue(issue_data['issue_number'])
    #         for issue_data in self.issues
    #     ]
    #
    # def add_issues(self, issues):
    #     path = f'/p1/repositories/{self.repo.id}/epics/{self.id}/update_issues'
    #     body = {
    #         'add_issues': [{'repo_id': issue.repo.id, 'issue_number': issue.number} for issue in issues],
    #     }
    #     self.repo.zenhub.post(path, body)
