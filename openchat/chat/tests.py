from django.test import TestCase


from .models import Message


class MessageModelTests(TestCase):
    def test___str___with_short_message_text(self):
        """
        __str__ returns complete message if text is shorter than
        21 characters
        """
        text = "I'm a short message."
        message = Message(text=text)
        result_text = message.__str__()
        expected_text = "\n{} // sent {}\n".format(
            message.text, message.date
            )

        self.assertAlmostEqual(
            expected_text,
            result_text
            )

    def test___str___with_long_message_text(self):
        """
        __str__ returns complete message if text is longer than
        21 characters
        """
        text = "I'm a looong message."
        message = Message(text=text)
        result_text = message.__str__()
        expected_text = "\n{}... // sent {}\n".format(
            message.text[:20], message.date
            )

        self.assertAlmostEqual(
            expected_text,
            result_text
            )
