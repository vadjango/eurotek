from report.fixtures.user import user
from report.fixtures.day_report import day_report


class TestRegistration:
    endpoint = "http://127.0.0.1:8000/api/v1/auth/register"

    def test_post_registration(self, client, user, day_report):
        response = client.post(self.endpoint, data={
            # TODO: test registration
        })
