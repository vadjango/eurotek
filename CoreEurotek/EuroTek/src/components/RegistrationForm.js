import React, { useState } from "react"
import { TextInput, View, StyleSheet, Image, Pressable, Text } from "react-native"


const RegistrationForm = () => {
    const [employeeID, onChangeEmployeeID] = useState("");
    const [password, onChangePassword] = useState("");
    const [repeatedPassword, onChangedRepeatedPassword] = useState("");

    return (
        <View style={styles.formContainer}>
            <Image source={require("../logo.png")} />
            <View style={styles.inputBlock}>
                <TextInput style={styles.input}
                        onChange={onChangeEmployeeID}
                        placeholder="Employee-ID"
                        value={employeeID}/>
                <TextInput style={styles.input}
                        onChange={onChangePassword}
                        secureTextEntry
                        placeholder="Password"
                        value={password}/>
                <TextInput style={styles.input}
                        onChange={onChangedRepeatedPassword}
                        secureTextEntry
                        placeholder="Repeat password"
                        value={repeatedPassword}/>
            </View>
            <Pressable style={styles.submitButton} onPress={() => console.log("Pressed")}>
                <Text style={styles.submitText}>Sign up</Text>
            </Pressable>
        </View>
    )
}

const styles = StyleSheet.create({
    formContainer: {
        justifyContent: "space-around",
        alignItems: "center"
      },
    inputBlock: {
        flex: 0.5,
        width: "80%",
        justifyContent: "space-between"
    },
    input: {
        backgroundColor: "white",
        borderRadius: 10,
        padding: 8,
        width: 250,
        fontSize: 20,
        // fontFamily: "Poppins-Black",
        paddingLeft: 15
    },
    submitButton: {
        backgroundColor: "#001E41",
        borderRadius: 30,
        paddingTop: 15,
        paddingBottom: 15,
        paddingRight: 30,
        paddingLeft: 30
    },
    submitText: {
        color: "white",
        fontSize: 14,
        // fontFamily: "Poppins-Black"
    }
  });
export default RegistrationForm;