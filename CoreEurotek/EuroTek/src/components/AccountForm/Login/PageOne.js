import React, { useState } from "react";
import { StyleSheet, View, Image, TextInput, Pressable, Text  } from "react-native";
import axios from "axios";
import { errInputStyle, errLabelStyle } from "../../errorStyle";
import BaseURL from "./BaseURL";
import FormButton from "../FormButton"
import FormLinkButton from "../FormLinkButton";



const LoginPageOne = ({ navigation }) => {
    const [employeeID, onChangeEmployeeID] = useState("");
    const [empIDInputStyle, setEmpIDInputStyle] = useState(null);
    const [empIDErrText, setEmpIDLabelText] = useState("");
    const [password, onChangePassword] = useState("");
    const [passwordErrStyle, setPasswordErrStyle] = useState("");
    const [passwordLabelText, setPasswordLabelText] = useState("");
    const [validationErrText, setValidationErrText] = useState("");


    function handleFormPage(e) {
        if (!employeeID) {
            setEmpIDInputStyle(errInputStyle);
            setEmpIDLabelText("Field cannot be empty.");
            return
        }
        if (!password) {
            setPasswordErrStyle(errInputStyle)
            setPasswordLabelText("Field cannot be empty.");
            return
        }
        axios.post(BaseURL, {
            "employee_id": employeeID,
            "password": password
        })
        .then((response) => {
            navigation.navigate("LoginPageTwo", {employeeID: employeeID, password: password});
            console.log(response.data)
        })
        .catch((e) => {
            console.log(e);
            if (e.response) {
               setValidationErrText(e.response.data["detail"]);
        }
        })
    }

    return (
        <View style={styles.container}>
            <View style={styles.topBlock}>
                <Image source={require("../../../../assets/images/login_v2.png")} style={styles.logo}/>
            </View>
            <View style={styles.mainBlock}>
                <View style={styles.loginBlock}>
                    <FormLinkButton text={"Registration"} onSubmit={() => navigation.navigate("Registration", {screen: "RegPageOne"})} />
                </View>
                <View style={styles.inputContainer}>
                    <View>
                        <TextInput style={[styles.input, empIDInputStyle]}
                            keyboardType={"decimal-pad"}
                            onChangeText={onChangeEmployeeID}
                            onChange={() => {
                                if (empIDInputStyle) {
                                    setEmpIDInputStyle(null);
                                }
                                if (empIDErrText) {
                                    setEmpIDLabelText(null);
                                }
                                if (validationErrText) {
                                    setValidationErrText(null);
                                }
                            }}
                            placeholder="Employee-ID"
                            placeholderTextColor={empIDInputStyle ? "#FF000025" : "#17171729"}
                            value={employeeID}
                        />
                        <Text style={{color: errInputStyle.color}}>{empIDErrText}</Text>
                    </View>
                    <View>
                        <TextInput style={[styles.input, passwordErrStyle]}
                            onChangeText={onChangePassword}
                            onChange={() => {
                                if (passwordErrStyle) {
                                    setPasswordErrStyle(null);
                                }
                                if (passwordLabelText) {
                                    setPasswordLabelText(null);
                                }
                                if (validationErrText) {
                                    setValidationErrText(null);
                                }
                            }}
                            placeholder="Password"
                            secureTextEntry={true}
                            placeholderTextColor={passwordErrStyle ? "#FF000025" : "#17171729"}
                            value={password}
                        />
                        <Text style={{color: errInputStyle.color}}>{passwordLabelText}</Text>
                    </View>
                </View>
                <View style={styles.validationErrBlock}>
                    <Text style={errLabelStyle}>{validationErrText}</Text>
                </View>
                <View style={styles.buttonBlock}>
                    <FormButton text={"Continue"}
                                onPress={handleFormPage} 
                    />
                </View>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        justifyContent: "space-between",
        alignItems: "center",
        backgroundColor: "#003867",
        flex: 1,
    },
    logo: {
        width: 100,
        objectFit: "contain",
    },
    topBlock: {
        flex: 0.35,
        justifyContent: "flex-end"
    },
    mainBlock: {
        flex: 0.65,
        width: "60%",
        marginTop: 30,
    },
    buttonBlock: {
        flexDirection: "row",
        columnGap: 5,
        justifyContent: "center",
        marginTop: 50,
    },
    inputContainer: {
        marginTop: 15,
        rowGap: 5,
    },
    loginBlock: {
        alignItems: "flex-end",
    },
    input: {
        backgroundColor: "white",
        borderRadius: 10,
        padding: 8,
        paddingTop: 10,
        width: 250,
        fontSize: 16,
        fontFamily: "Poppins",
        paddingLeft: 25,
        textAlignVertical: "center"
    },
    validationErrBlock: {
        alignItems: "center",
    }
})
export default LoginPageOne;