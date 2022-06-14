from django.test import TestCase
import unittest
from .models import Project

# Create your tests here.
class TestProject(unittest.TestCase):
    """
    Class to test the behaviours of the Project model.
    """

    def setUp(self):
        self.new_project = Project('Instaclone', 'Home of nice work', 'http://aif')

    def tearDown(self):
        Project.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project, Project))

