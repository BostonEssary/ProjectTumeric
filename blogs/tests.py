import datetime


from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Title




################################################################################################
#                                                                                              #
#                                                                                              #
#                                           VIEW TESTS                                         #
#                                                                                              #
################################################################################################

##### Index View #####

def create_title(title_text, days):
    """
    Create a title with the given 'title_text' and published the given number of 'days' offset to 
    now.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Title.objects.create(title_text=title_text, pub_date=time)


class TitleIndexViewTests(TestCase):
    def test_no_title(self):
        """
        If no title exist, an appropriate message is displayed.
        """

        response = self.client.get(reverse("title:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No titles are available.")
        self.assertQuerysetEqual(response.content["latest_title_list"], [])
    
    def test_past_title(self):
        """
        Titles with a pub_date in the past are displayed on the index page.
        """
        title = create_title(title_text="Past title.", days=-30)
        response = self.client.get(reverse("title:index"))
        self.assertQuerysetEqual(
            response.content["latest_title_list"],
            [title],
        )

    def test_future_title(self):
        """
        Titles with a pub_date in the future aren't displayed on the index page.
        """
        create_title(title_text="Future question.", days=30)
        response = self.client.get(reverse("blogs:index"))
        self.assertContains(response, "No titles are available")
        self.assertQuerySetEqual(response.context["latest_title_list"],[])

##### Detail Views #####

class TitleDetailViewTests(TestCase):
    def test_future_title(self):
        """
        The detail view of a title with a pub_date in the future returns a 404 not found
        """
        future_title = create_title(title_text="Future Title.", days=5)
        url = reverse("blogs:detail", args=(future_title.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_title(self):
        """
        The detail view of a question with a pub_date in the past displays the title's text.
        """

        past_title = create_title(title_text="Past Title.", days=-5)
        url = reverse("blogs:detail", args=(past_title.id,))
        response = self.client.get(url)
        self.assertContains(response, past_title.title_text)















################################################################################################
#                                                                                              #
#                                                                                              #
#                                           MODEL TESTS                                        #
#                                                                                              #
################################################################################################


class TitleModelTests(TestCase):
    def test_was_published_recently_with_future_title(self):
        """
        was_published_recently() returns false for title whose pub_date is in the future.

        """

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Title(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_title(self):
        """
        was_published_recently() returns False for titles  whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_title = Title(pub_date=time)
        self.assertIs(old_title.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Title(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

