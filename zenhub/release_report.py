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
Module Release Report
"""
class ReleaseReport:
    """
    Release Reports
    ---------------
    Create a Release Report
        POST   /p1/repositories/:repo_id/reports/release
    Get a Release Report
        GET    /p1/reports/release/:release_id
    Get Release Reports for a Repository
        GET    /p1/repositories/:repo_id/reports/releases
    Edit a Release Report
        PATCH  /p1/reports/release/:release_id
    Add Workspaces to a Release Report
        POST   /p1/reports/release/:release_id/repositories/:repo_id
    Remove Workspaces from a Release Report
        DELETE /p1/reports/release/:release_id/repositories/:repo_id

    Release Report Issues
    ---------------------
    Get all the Issues in a Release Report
        GET    /p1/reports/release/:release_id/issues
    Add or Remove Issues from a Release Report
        PATCH  /p1/reports/release/:release_id/issues
    """
