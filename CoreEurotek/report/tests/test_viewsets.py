from report.fixtures.user import user
from report.fixtures.day_report import day_report


class TestDayReport:
    api_endpoint = "/api/v1/report/"

    def test_get_reports(self, client, user, day_report):
        client.force_authenticate(user=user)
        response = client.get(self.api_endpoint)
        assert response.status_code == 301
        assert response.data["count"] == 1
