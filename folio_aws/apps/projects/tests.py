
from django.test import TestCase


from .models import Project

from django.urls import reverse


def create_project(title, description, image_path, repo):
    return Project.objects.create(title=title, description=description,
                                  image_path=image_path, repo=repo)


class QuestionIndexViewTests(TestCase):
    def test_no_projects(self):
        """
        Response to no projects existing potentially as a subset.
        """
        response = self.client.get(reverse('projects:project_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")
        self.assertQuerysetEqual(response.context['project_list'], [])


class ProjectDataTests(TestCase):

    def test_repo_valid(self):
        sample_project = create_project("Test Project",
                                        "A project to test functionality",
                                        "/arbitrary/link/",
                                        "http://github.com/EazyEgan/FYP")

        self.assertTrue(sample_project.valid_repo())

    def test_repo_invalid_mitigate(self):
        sample_project = create_project(
            "Test Project", "A project to test functionality",
            "/arbitrary/link/",
            "http://github.com/EazyEgan/non-existant-repo")

        self.assertTrue(sample_project.valid_repo())
        self.assertEqual(sample_project.repo,
                         "https://github.com/EazyEgan/FYP")

    def test_repo_language_retreival(self):
        """
        Check that language data is retreived correctly.
        """
        sample_project = create_project("Test Project",
                                        "A project to test functionality",
                                        "/arbitrary/link/",
                                        "http://github.com/EazyEgan/FYP")

        self.assertTrue(type(sample_project.project_languages()) is str)
        # or self.assertIs(sample_project.project_languages(), str)
        self.assertNotEqual(sample_project.project_languages(),
                            "No data available")

    def test_repo_failed_language_retreival(self):
        """
        Respond to failed language retreival.
        """
        sample_project = create_project(
            "Test Project", "A project to test functionality",
            "/arbitrary/link/", "http://github.com/EazyEgan/non-existant-repo")

        self.assertTrue(type(sample_project.project_languages()) is str)
        # or self.assertIs(sample_project.project_languages(), str)
        self.assertEqual(sample_project.project_languages(),
                         "No data available")

    def test_image_path_copied(self):
        """
        Image path did not copy to image filepath.
        """
        sample_project = create_project("Test Project",
                                        "A project to test functionality",
                                        "projects/images/Screenshot_48.png",
                                        "http://github.com/EazyEgan/FYP")
        self.assertTrue(type(sample_project.image) is str)
        self.assertTrue(type(sample_project.image_path) is str)
        self.assertEqual(sample_project.image, sample_project.image_path)

    def test_image_path_invalid(self):
        """
        Invalid image file path supplied.
        """
        sample_project = create_project(
            "Test Project", "A project to test functionality",
            "projects/images/non-existant-pic.png",
            "http://github.com/EazyEgan/non-existant-repo")

        self.assertTrue(type(sample_project.image) is str)
        self.assertTrue(type(sample_project.image_path) is str)
        self.assertEqual(sample_project.image, "projects/images/not_found.png")
