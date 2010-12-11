from django.test import TestCase

from filtertest import models as fm

class FilterTest(TestCase):
    def test_basic_assumption(self):
		company = fm.Company.objects.create(name="ACME")

		fm.Location.objects.create(company=company,name="West Location",zip_code="90210",open_days="WEEK")
		fm.Location.objects.create(company=company,name="East Location",zip_code="32801",open_days="WEEKEND")

		"""
		Fail if our filtering for a WEEKEND company in 90210 finds our company above
		"""
		self.failUnlessEqual(fm.Company.objects.filter(locations__zip_code="90210").filter(locations__open_days="WEEKEND").count(),0)
