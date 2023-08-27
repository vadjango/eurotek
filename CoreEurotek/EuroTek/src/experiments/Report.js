import { storage } from "./Storage";
import { View } from "react-native";
BaseURL = "http://127.0.0.1:8000/api/v1/auth/login/"


function getUserTokens(credentials) {
    fetch(BaseURL + "", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        "body": credentials,
    })
    .then((response) => response.text())
    .then((data) => {
        storage.set("auth", data)
        storage.getString("auth");
    })
    .catch((e) => console.error(e))
    return (
        <View></View>
    )
}

const Report = () => {
    const userData = {
        "employee_id": "15642",
        "password": "bolit_hujnia"
    };
    getUserTokens(userData);
};


export default Report;