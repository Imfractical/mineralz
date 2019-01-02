"""mineral_catalog custom context processors

Make sure to add these to settings.py
"""


def mineral_groups(request):
    return {
        'groups': {
            'silicates': 'Silicates',
            'oxides': 'Oxides',
            'sulfates': 'Sulfates',
            'sulfides': 'Sulfides',
            'carbonates': 'Carbonates',
            'halides': 'Halides',
            'sulfosalts': 'Sulfosalts',
            'phosphates': 'Phosphates',
            'borates': 'Borates',
            'organic_minerals': 'Organic Minerals',
            'arsenates': 'Arsenates',
            'native_elements': 'Native Elements',
            'other': 'Other',
        }
    }
