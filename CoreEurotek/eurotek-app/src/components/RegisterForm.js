import React, { useState } from "react"
import { Image, TextInput, View, StyleSheet } from "react-native"

const RegisterForm = () => {
    const [employeeID, onChangeEmployeeID] = useState(null);
    const [password, onChangePassword] = useState(null);

    return (
    <View style={styles.container}>
        <Image source={require("../logo.png")} style={styles.logo} /> 
        <View style={styles.inputBlock}>
            <TextInput style={styles.input}
                       onChange={onChangeEmployeeID}
                       placeholder="Employee ID"/>
        </View>
    </View>
    )
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: "#1155AA",
      alignItems: "center",
      justifyContent: "center",
    },
    logo: {
        width: "40%",
        resizeMode: "contain"
    },
    inputBlock: {
        width: "60%"
    },
    input: {
        backgroundColor: "white",
        borderRadius: 10,
        padding: 10
    }
  });
export default RegisterForm;