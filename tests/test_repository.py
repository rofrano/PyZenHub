"""
Test cases for ZenHub class
"""
import json
import logging
from unittest import TestCase, mock
from zenhub import ZenHub, Repository, Board, Issue, Epic

BOARD_DATA = {}

######################################################################
#  T E S T   C A S E S
######################################################################
class TestRepository(TestCase):
    """ Test Cases for Repository class """

    @classmethod
    def setUpClass(cls):
        global BOARD_DATA
        with open('tests/fixtures/board_no_issues.json') as json_data:
            BOARD_DATA = json.load(json_data)

    def setUp(self):
        self.zenhub = ZenHub('ZENHUB_TOKEN')
        self.repo = Repository(12345, self.zenhub)

    def test_contructor(self):
        """ Create / Constructor """
        self.assertEqual(self.repo.id, 12345)
        self.assertEqual(self.repo.zenhub, self.zenhub)

    @mock.patch('zenhub.Board.find')
    def test_get_board(self, mock_board):
        """ Test Get Board """
        mock_board.return_value = Board(BOARD_DATA, self.repo)
        board = self.repo.board()
        logging.error(board)
        self.assertIsInstance(board, Board)
        self.assertEqual(board.data, BOARD_DATA)
        self.assertEqual(board.repo, self.repo)

    @mock.patch('zenhub.Board.find')
    def test_get_board_not_found(self, mock_board):
        """ Test Get Board Not Found """
        mock_board.return_value = None
        board = self.repo.board()
        logging.error(board)
        self.assertIsNone(board)

    @mock.patch('zenhub.Issue.find')
    def test_get_issue(self, mock_issue):
        """ Test Get an Issue """
        with open('tests/fixtures/issue.json') as json_data:
            ISSUE_DATA = json.load(json_data)
        mock_issue.return_value = Issue(ISSUE_DATA, 3, self.repo)
        issue = self.repo.issue(3)
        logging.error(issue)
        self.assertIsInstance(issue, Issue)
        self.assertEqual(issue.data, ISSUE_DATA)
        self.assertEqual(issue.repo, self.repo)
        self.assertEqual(issue.number, 3)
        self.assertEqual(issue.pipeline, ISSUE_DATA['pipeline'])
        self.assertEqual(issue.is_epic, ISSUE_DATA['is_epic'])
        self.assertEqual(issue.estimate, ISSUE_DATA['estimate']['value'])

    @mock.patch('zenhub.Issue.find')
    def test_get_issue_not_found(self, mock_issue):
        """ Test Get Issue Not Found """
        mock_issue.return_value = None
        issue = self.repo.issue(3)
        logging.error(issue)
        self.assertIsNone(issue)

    @mock.patch('zenhub.ZenHub.get')
    def test_get_epics(self, mock_get):
        """ Test Get Epics """
        with open('tests/fixtures/epic_issues.json') as json_data:
            EPIC_DATA = json.load(json_data)
        mock_get.return_value = EPIC_DATA
        epics = self.repo.epics()
        logging.error(epics)
        self.assertIsInstance(epics, list)
        self.assertEqual(len(epics), 2)
        self.assertIsInstance(epics[0], Epic)
        self.assertEqual(epics[0].id, 3953)

    @mock.patch('zenhub.ZenHub.get')
    def test_get_an_epics(self, mock_get):
        """ Test Get an Epic """
        with open('tests/fixtures/epic_data.json') as json_data:
            EPIC_DATA = json.load(json_data)
        mock_get.return_value = EPIC_DATA
        epic = self.repo.epic(1)
        logging.error(epic)
        self.assertIsInstance(epic, Epic)
        self.assertEqual(epic.id, 1)
        self.assertEqual(len(epic.pipelines), 2)
