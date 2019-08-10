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
ZenHub API library for Python.

This is a Python binding for the ZenHub API as described at https://github.com/ZenHubIO/API.
It includes the following classes

- ZenHub
- Repository
- Board
- Pipeline
- Epic
- Issue
- Workspace

"""

from .zenhub import ZenHub
from .repository import Repository
from .board import Board
from .pipeline import Pipeline
from .epic import Epic
from .issue import Issue
from .workspace import Workspace
