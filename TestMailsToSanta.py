import unittest
from datetime import datetime
from MailsToSanta import MailsToSanta


class TestMailsToSanta(unittest.TestCase):
    def test_business_hours(self):
        # Test for mails received during non-business hours
        # A mail received on 05.08.2021 at 5:00 should be scheduled to 8:00 on the same day.
        mail_time = datetime(2021, 8, 5, 5, 0)
        expected = datetime(2021, 8, 5, 8, 0)
        self.assertEqual(MailsToSanta.calculated_time_to_process(mail_time), expected)

        # A mail received on 15.07.2021 at 16:22 should be scheduled to 8:00 on 16.07.2021.
        mail_time = datetime(2021, 7, 15, 16, 22)
        expected = datetime(2021, 7, 16, 8, 0)
        self.assertEqual(MailsToSanta.calculated_time_to_process(mail_time), expected)

    def test_weekends(self):
        # Test for mails received during weekends
        mail_time = datetime(2021, 2, 28, 10, 0)
        expected = datetime(2021, 3, 1, 8, 0)
        self.assertEqual(MailsToSanta.calculated_time_to_process(mail_time), expected)

    def test_holidays(self):
        # Test for mails received during holidays
        mail_time = datetime(2021, 1, 2, 10, 0)
        expected = datetime(2021, 1, 7, 8, 0)
        self.assertEqual(MailsToSanta.calculated_time_to_process(mail_time), expected)


if __name__ == '__main__':
    unittest.main()
