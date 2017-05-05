from django.core.urlresolvers import reverse
from django.test import TestCase


from .models import Mineral, JSONReader

test_dict = JSONReader('minerals/static/data/test_data.json')
class MineralModelTests(TestCase):
    def setUp(self):
        for d in test_dict:
            Mineral.objects.create(**d)
        self.minerals = Mineral.objects.all()
        self.mineral = Mineral.objects.get(name='Abhurite')

    def test_mineral_string(self):
        """String version of Mineral should be Mineral's name attribute"""
        self.assertEqual(str(self.mineral), self.mineral.name)

    def test_json_model_creation(self):
        self.assertEqual(Mineral.objects.all().count(), 3)

    def test_image_filename_creation(self):
        self.assertEqual(self.mineral.image_filename, 'minerals/images/Abhurite.jpg')


class MineralViewTest(TestCase):
    def setUp(self):
        for d in test_dict:
            Mineral.objects.create(**d)
        self.mineral = Mineral.objects.all().get(name='Abhurite')

    def test_mineral_list_view(self):
        """The mineral_list view should:
           * return a 200
           * have self.mineral in the context
           * use the minerals/index.html template
        """
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')

    def test_mineral_detail_view(self):
        """The mineral_detail view should:
           * return a 200
           * have self.mineral in the context
           * use the minerals/detail.html template
        """

        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['mineral'], self.mineral)
        self.assertTemplateUsed(resp, 'minerals/detail.html')

    def test_html_parsing(self):
        pass

