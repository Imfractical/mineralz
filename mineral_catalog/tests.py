"""mineral_catalog tests"""
from django.template import Context, Template
from django.test import TestCase
from django.urls import reverse

from .management.commands import populate
from .models import Mineral


class MineralTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Mineral.objects.create(
            name='Adamantium',
        )
        Mineral.objects.create(
            name='Sálamander',
            color='green',
        )
        Mineral.objects.create(
            name='Sálamander',
            color='pink',
        )
        Mineral.objects.create(
            name='Aegirine',
            image_filename='250px-8336M-aegirine.jpg',
            image_caption=('Monoclinic crystal of aegirine with orthoclase, from Mount Malosa, '
                           'Zomba District, Malawi (size: 85 mm x 83 mm; 235 g)'),
            category='Silicate, Pyroxene',
            formula='<sub>231</sub>.<sub>00</sub>',
            strunz_classification='09.DA.25',
            crystal_system='Monoclinic Prismatic',
            unit_cell='a = 9.658 Å, b = 8.795 Å, c = 5.294 Å, β = 107.42°; Z=4',
            color='Dark Green, Greenish Black',
            crystal_symmetry='Monoclinic 2/m',
            cleavage='Good on \{110\}, (110) ^ (110) ≈87°; parting on \{100\}',
            mohs_scale_hardness='6',
            luster='Vitreous to slightly resinous',
            streak='Yellowish-grey',
            diaphaneity='Translucent to opaque',
            optical_properties='Biaxial (-)',
            refractive_index='nα = 1.720 - 1.778 nβ = 1.740 - 1.819 nγ = 1.757 - 1.839',
            crystal_habit=('Prismatic crystals may be in sprays of acicular crystals, '
                           'fibrous, in radial concretions'),
            specific_gravity='3.50 - 3.60',
            group='Silicates',
        )

    def test_self_str_returns_name(self):
        adamantium = Mineral.objects.get(name='Adamantium')
        salamander1 = Mineral.objects.get(color='green')
        salamander2 = Mineral.objects.get(color='pink')
        self.assertEqual(str(adamantium), 'Adamantium')
        self.assertEqual(str(salamander1), 'Sálamander')
        self.assertEqual(str(salamander2), 'Sálamander')

    def test_slugs(self):
        adamantium = Mineral.objects.get(name='Adamantium')
        salamander1 = Mineral.objects.get(color='green')
        salamander2 = Mineral.objects.get(color='pink')
        self.assertEqual(adamantium.slug, 'adamantium')
        self.assertEqual(salamander1.slug, 'salamander')
        # Test that would-be identical slugs suffix a number
        self.assertEqual(salamander2.slug, 'salamander-1')


class PopulateCommandTests(TestCase):
    def test_populate_command(self):
        populate_command = populate.Command()
        populate_command.handle(json_file='included/data/minerals.json')
        self.assertEquals(Mineral.objects.count(), 874)

        aegirine = Mineral.objects.get(name='Aegirine')
        self.assertEqual(
            aegirine.name,
            'Aegirine',
        )
        self.assertEqual(
            aegirine.image_filename,
            '250px-8336M-aegirine.jpg',
        )
        self.assertEqual(
            aegirine.image_caption,
            ('Monoclinic crystal of aegirine with orthoclase, from Mount Malosa, '
             'Zomba District, Malawi (size: 85 mm x 83 mm; 235 g)'),
        )
        self.assertEqual(
            aegirine.category,
            'Silicate, Pyroxene',
        )
        self.assertEqual(
            aegirine.formula,
            '<sub>231</sub>.<sub>00</sub>',
        )
        self.assertEqual(
            aegirine.strunz_classification,
            '09.DA.25',
        )
        self.assertEqual(
            aegirine.crystal_system,
            'Monoclinic Prismatic',
        )
        self.assertEqual(
            aegirine.unit_cell,
            'a = 9.658 Å, b = 8.795 Å, c = 5.294 Å, β = 107.42°; Z=4',
        )
        self.assertEqual(
            aegirine.color,
            'Dark Green, Greenish Black',
        )
        self.assertEqual(
            aegirine.crystal_symmetry,
            'Monoclinic 2/m',
        )
        self.assertEqual(
            aegirine.cleavage,
            'Good on {110}, (110) ^ (110) ≈87°; parting on {100}',
        )
        self.assertEqual(
            aegirine.mohs_scale_hardness,
            '6',
        )
        self.assertEqual(
            aegirine.luster,
            'Vitreous to slightly resinous',
        )
        self.assertEqual(
            aegirine.streak,
            'Yellowish-grey',
        )
        self.assertEqual(
            aegirine.diaphaneity,
            'Translucent to opaque',
        )
        self.assertEqual(
            aegirine.optical_properties,
            'Biaxial (-)',
        )
        self.assertEqual(
            aegirine.refractive_index,
            'nα = 1.720 - 1.778 nβ = 1.740 - 1.819 nγ = 1.757 - 1.839',
        )
        self.assertEqual(
            aegirine.crystal_habit,
            ('Prismatic crystals may be in sprays of acicular '
             'crystals, fibrous, in radial concretions'),
        )
        self.assertEqual(
            aegirine.specific_gravity,
            '3.50 - 3.60',
        )
        self.assertEqual(
            aegirine.group,
            'Silicates',
        )


class GetattrTagTests(TestCase):
    def setUp(self):
        Mineral.objects.create(name='Whoarock')

    def test_getattr(self):
        context = Context({'mineral': Mineral.objects.get(name='Whoarock')})
        template_to_render = Template(
            '{% load getattr %}'
            '{{ mineral|getattr:"name" }}'
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML('Whoarock', rendered_template)


class ViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        populate_command = populate.Command()
        populate_command.handle(json_file='included/data/minerals.json')

    def test_list_view_with_a(self):
        response = self.client.get(reverse('catalog:list'))
        self.assertEqual(response.status_code, 200)
        minerals = Mineral.objects.filter(name__istartswith='a')
        for mineral in minerals:
            self.assertContains(response, mineral.name)

    def test_list_view_with_m(self):
        response = self.client.get(reverse('catalog:list'))
        self.assertEqual(response.status_code, 200)
        minerals = Mineral.objects.filter(name__istartswith='m')
        for mineral in minerals:
            self.assertContains(response, mineral.name)

    def test_detail_view(self):
        mineral = Mineral.objects.get(name='Aegirine')
        response = self.client.get(reverse('catalog:detail', args=[mineral.slug]))
        self.assertContains(response, 'a = 9.658 Å, b = 8.795 Å, c = 5.294 Å, β = 107.42°; Z=4')
