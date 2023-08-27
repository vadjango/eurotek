from rest_framework import status
from report.fixtures.user import user, additional_user, manager
from report.fixtures.day_report import day_report
from report.fixtures.comment import comment


class TestComment:
    api_endpoint = "/api/v1/report/{public_id}/comment/"

    def test_get_comments_by_default_user(self, client, day_report, user, comment):
        client.force_authenticate(user=user)
        url = self.api_endpoint.format(public_id=day_report.public_id)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    def test_get_comments_by_extra_user(self, client, day_report, additional_user, comment):
        client.force_authenticate(user=additional_user)
        url = self.api_endpoint.format(public_id=day_report.public_id.hex)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 0

    def test_get_comments_by_manager(self, client, day_report, manager, comment):
        client.force_authenticate(user=manager)
        url = self.api_endpoint.format(public_id=day_report.public_id.hex)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    def test_create_comments_by_user(self, client, day_report, user):
        client.force_authenticate(user=user)
        url = self.api_endpoint.format(public_id=day_report.public_id.hex)
        comment_data = {
            "day_report": day_report.public_id.hex,
            "body": "Test body"
        }
        response = client.post(url, data=comment_data, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_comments_by_manager(self, client, day_report, manager):
        client.force_authenticate(user=manager)
        url = self.api_endpoint.format(public_id=day_report.public_id.hex)
        comment_data = {
            "body": "Test body"
        }
        response = client.post(url, data=comment_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["body"] == comment_data["body"]

    def test_put_comment_by_manager(self, client, day_report, comment, manager):
        client.force_authenticate(user=manager)
        url = self.api_endpoint.format(public_id=day_report.public_id.hex)
        comment_data = {
            "body": "Changed body"
        }
        response = client.put(url + f"{comment.public_id}/", data=comment_data, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_patch_comment_by_manager(self, client, day_report, comment, manager):
        client.force_authenticate(user=manager)
        url = self.api_endpoint.format(public_id=day_report.public_id.hex)
        comment_data = {
            "body": "Changed body"
        }
        response = client.patch(url + f"{comment.public_id}/", data=comment_data, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_delete_comment_by_manager(self, client, day_report, comment, manager):
        client.force_authenticate(user=manager)
        url = self.api_endpoint.format(public_id=day_report.public_id.hex)
        response = client.delete(url + f"{comment.public_id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
