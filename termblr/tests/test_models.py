from . import fixtures
from .helpers import GeneralTestCase
from Termblr import models
import datetime
from nose.plugins.attrib import attr


class ModelPaymentTestCase(GeneralTestCase):
    def setUp(self):
        super().setUp()
        fixtures.typical_users()

    def tearDown(self):
        super().tearDown()

    # @attr('single')
    def test_crud(self):
        'Testing Termblr.models.Payment'
        joe = models.User.find(email='joe')
        cameron = models.User.find(email='cameron')
        # import ipdb; ipdb.set_trace()

        payment = models.Payment.create(
            user_from=joe,
            user_to=cameron,
            amount=100,
            message="Thanks!",
            sent_at=datetime.datetime.now(),
        )

        self.assertEqual(payment.user_from, joe)
        self.assertEqual(payment.user_to, cameron)


class ModelUserTestCase(GeneralTestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # @attr('single')
    def test_pay(self):
        'Testing Termblr.models.User.pay'
        fixtures.typical_users()

        joe = models.User.find(email='joe')
        cameron = models.User.find(email='cameron')

        payment = joe.pay(
            user_to=cameron,
            amount=100,
            message="Work harder on that BIOS.",
        )

        self.assertEqual(payment.user_from, joe)
        self.assertEqual(payment.user_to, cameron)
        self.assertEqual(payment.message, "Work harder on that BIOS.")
        self.assertEqual(payment.amount, 100)
        # import ipdb; ipdb.set_trace()
        # assert False
