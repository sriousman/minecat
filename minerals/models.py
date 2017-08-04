from django.db import models

import json


class Mineral(models.Model):
    name = models.CharField(max_length=255, null=True)
    image_filename = models.CharField(max_length=255, null=True)
    image_caption = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    formula = models.CharField(max_length=255, null=True)
    strunz_classification = models.CharField(max_length=255, null=True)
    crystal_system = models.CharField(max_length=255, null=True)
    unit_cell = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=255, null=True)
    crystal_symmetry = models.CharField(max_length=255, null=True)
    cleavage = models.CharField(max_length=255, null=True)
    mohs_scale_hardness = models.CharField(max_length=255, null=True)
    luster = models.CharField(max_length=255, null=True)
    streak = models.CharField(max_length=255, null=True)
    diaphaneity = models.CharField(max_length=255, null=True)
    optical_properties = models.CharField(max_length=255, null=True)
    refractive_index = models.CharField(max_length=255, null=True)
    crystal_habit = models.CharField(max_length=255, null=True)
    specific_gravity = models.CharField(max_length=255, null=True)
    group = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        excluded_fields = ('id', 'status', 'workshop', 'user', 'complete', 'name', 'image',
                           'image_filename', 'image_caption')
        for f in self._meta.fields:

            fname = f.name
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_' + fname + '_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in excluded_fields:
                fields.append(
                    {
                        'label': f.verbose_name.title(),
                        'name': f.name,
                        'value': value,
                    }
                )
        return fields



def JSONReader(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return clean(data)


def clean(data):
    cdat = []
    for d in data:
        cd = {}
        for k,v in d.items():
                new_k = k.replace(" ", '_')
                if new_k == 'image_filename':
                    cd['image_filename'] = 'images/{}.jpg'.format(d['name'])
                else:
                    cd[new_k] = v

        cdat.append(cd)
    return cdat


def save_images():
    minerals = Mineral.objects.all()
    for m in minerals:
        m.image = m.image_filename
        m.save()


def initialize():
    try:
        minerals = JSONReader('minerals/static/data/minerals.json')
        for mineral in minerals:
            Mineral.objects.create(**mineral)
    except ValueError:
        pass

