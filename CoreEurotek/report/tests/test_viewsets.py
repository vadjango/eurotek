from datetime import datetime, timedelta
from report.fixtures.user import user, additional_user, manager
from report.fixtures.day_report import day_report
from rest_framework import status


class TestDayReport:
    api_endpoint = "/api/v1/report/"

    def test_get_reports(self, client, user, day_report):
        client.force_authenticate(user=user)
        response = client.get(self.api_endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    def test_get_current_user_report(self, client, user, day_report):
        client.force_authenticate(user=user)
        response = client.get(self.api_endpoint + f"{day_report.public_id.hex}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["employee"] == day_report.employee.pk
        assert response.data["shift"] == day_report.shift
        assert response.data["start_date"] == day_report.start_date
        assert response.data["start_time"] == day_report.start_time
        assert response.data["end_time"] == day_report.end_time
        assert response.data["type_num"] == day_report.type_num
        assert response.data["operation_num"] == day_report.operation_num
        assert response.data["operation_name"] == day_report.operation_name
        assert response.data["total_number_of_pieces"] == day_report.total_number_of_pieces
        assert response.data["min_norm"] == day_report.min_norm
        assert response.data["total_hours"] == day_report.total_hours

    def test_get_another_user_report(self, client, additional_user, day_report):
        client.force_authenticate(user=additional_user)
        response = client.get(self.api_endpoint + f"{day_report.public_id.hex}/")
        assert response.status_code == 404

    def test_get_user_report_by_manager(self, client, manager, day_report):
        client.force_authenticate(user=manager)
        response = client.get(self.api_endpoint + f"{day_report.public_id.hex}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["employee"] == day_report.employee.pk
        assert response.data["shift"] == day_report.shift
        assert response.data["start_date"] == day_report.start_date
        assert response.data["start_time"] == day_report.start_time
        assert response.data["end_time"] == day_report.end_time
        assert response.data["type_num"] == day_report.type_num
        assert response.data["operation_num"] == day_report.operation_num
        assert response.data["operation_name"] == day_report.operation_name
        assert response.data["total_number_of_pieces"] == day_report.total_number_of_pieces
        assert response.data["min_norm"] == day_report.min_norm
        assert response.data["total_hours"] == day_report.total_hours

    def test_create_report(self, client, user):
        dt_tm = datetime.now()
        start_time = (dt_tm - timedelta(hours=8)).time()
        end_time = dt_tm.time()
        report_data = {
            "shift": "afternoon",
            "start_date": dt_tm.strftime("%Y-%m-%d"),
            "start_time": start_time.strftime("%H:%M:%S"),
            "end_time": end_time.strftime("%H:%M:%S"),
            "type_num": "015",
            "operation_num": "125",
            "operation_name": "Some operation",
            "total_number_of_pieces": 2015,
            "min_norm": 500,
            "total_hours": 7.5
        }
        client.force_authenticate(user=user)
        response = client.post(self.api_endpoint,
                               data=report_data,
                               format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["shift"] == report_data["shift"]
        assert response.data["start_date"] == report_data["start_date"]
        assert response.data["start_time"] == report_data["start_time"]
        assert response.data["end_time"] == report_data["end_time"]
        assert response.data["type_num"] == report_data["type_num"]
        assert response.data["operation_num"] == report_data["operation_num"]
        assert response.data["operation_name"] == report_data["operation_name"]
        assert response.data["total_number_of_pieces"] == report_data["total_number_of_pieces"]
        assert response.data["min_norm"] == report_data["min_norm"]
        assert response.data["total_hours"] == report_data["total_hours"]

    def test_patch_report_by_current_user(self, client, user, day_report):
        client.force_authenticate(user=user)
        update_data = {
            "shift": "night",
            "start_time": "21:00:00",
            "end_time": "10:00:00"
        }
        response = client.patch(self.api_endpoint + f"{day_report.public_id.hex}/", update_data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["shift"] == update_data["shift"]
        assert response.data["start_time"] == update_data["start_time"]
        assert response.data["end_time"] == update_data["end_time"]

    def test_patch_report_by_additional_user(self, client, additional_user, day_report):
        client.force_authenticate(user=additional_user)
        update_data = {
            "shift": "night",
            "start_time": "21:00:00",
            "end_time": "10:00:00"
        }
        response = client.patch(self.api_endpoint + f"{day_report.public_id.hex}/", update_data, format="json")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_patch_report_by_manager(self, client, manager, day_report):
        client.force_authenticate(user=manager)
        update_data = {
            "shift": "night",
            "start_time": "21:00:00",
            "end_time": "10:00:00"
        }
        response = client.patch(self.api_endpoint + f"{day_report.public_id.hex}/", update_data, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_put_report_by_current_user(self, client, user, day_report):
        client.force_authenticate(user=user)
        update_data = {
            "shift": "night",
            "start_date": "2023-08-11",
            "start_time": "21:00:00",
            "end_time": "10:00:00",
            "type_num": "015",
            "operation_num": "1250",
            "operation_name": "tlumivka",
            "total_number_of_pieces": 2500,
            "min_norm": 500,
            "total_hours": 11.5
        }
        response = client.put(self.api_endpoint + f"{day_report.public_id.hex}/", update_data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["shift"] == update_data["shift"]
        assert response.data["start_date"] == update_data["start_date"]
        assert response.data["start_time"] == update_data["start_time"]
        assert response.data["end_time"] == update_data["end_time"]
        assert response.data["type_num"] == update_data["type_num"]
        assert response.data["operation_num"] == update_data["operation_num"]
        assert response.data["operation_name"] == update_data["operation_name"]
        assert response.data["total_number_of_pieces"] == update_data["total_number_of_pieces"]
        assert response.data["min_norm"] == update_data["min_norm"]
        assert response.data["total_hours"] == update_data["total_hours"]

    def test_put_report_by_additional_user(self, client, additional_user, day_report):
        client.force_authenticate(user=additional_user)
        update_data = {
            "shift": "night",
            "date": "2023-08-11",
            "start_time": "21:00:00",
            "end_time": "10:00:00",
            "type_num": "015",
            "operation_num": "1250",
            "operation_name": "tlumivka",
            "total_number_of_pieces": 2500,
            "min_norm": 500,
            "total_hours": 11.5
        }
        response = client.put(self.api_endpoint + f"{day_report.public_id.hex}/", update_data, format="json")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_put_report_by_manager(self, client, manager, day_report):
        client.force_authenticate(user=manager)
        update_data = {
            "shift": "night",
            "start_date": "2023-08-11",
            "start_time": "21:00:00",
            "end_time": "10:00:00",
            "type_num": "015",
            "operation_num": "1250",
            "operation_name": "tlumivka",
            "total_number_of_pieces": 2500,
            "min_norm": 500,
            "total_hours": 11.5
        }
        response = client.put(self.api_endpoint + f"{day_report.public_id.hex}/", update_data, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete(self, client, user, day_report):
        client.force_authenticate(user=user)
        response = client.delete(self.api_endpoint + f"{day_report.public_id.hex}/")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
