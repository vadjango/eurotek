import React, { useState } from "react"
import { 
        TextInput,  
        View, 
        StyleSheet, 
        Image, 
        Platform, 
        Pressable, 
        Text,
        ScrollView,
        KeyboardAvoidingView
    } from "react-native"
import KeyboardAvoidingContainer from "../KeyboardAvoidingContainer";


const RegistrationForm = () => {
    const [firstname, onChangeFirstName] = useState("");
    const [lastname, onChangeLastName] = useState("");
    const [password, onChangePassword] = useState("");
    const [repeatedPassword, onChangedRepeatedPassword] = useState("");

    return (
        <KeyboardAvoidingContainer>
            <View style={styles.container}>
                <View style={styles.topBlock}>
                    <Image source={require("../../logo.png")} style={styles.logo}/>
                </View>
                <View style={styles.mainBlock}>
                    <View style={styles.form}>
                        <View style={styles.loginBlock}>
                            <Pressable>
                                <Text style={styles.loginButtonText}>Login</Text>
                            </Pressable>
                        </View>
                        <View style={styles.inputBlock}>
                            <TextInput style={styles.input}
                                    onChangeText={onChangeFirstName}
                                    placeholder="Your firstname"
                                    placeholderTextColor={"#17171729"}
                                    value={firstname}/>
                            <TextInput style={styles.input}
                                    onChangeText={onChangeLastName}
                                    placeholder="Your lastname"
                                    placeholderTextColor={"#17171729"}
                                    value={lastname}/>
                            <TextInput style={styles.input}
                                    onChangeText={onChangePassword}
                                    secureTextEntry
                                    placeholder="Password"
                                    placeholderTextColor={"#17171729"}
                                    value={password}/>
                            <TextInput style={styles.input}
                                    onChangeText={onChangedRepeatedPassword}
                                    secureTextEntry
                                    placeholder="Repeat password"
                                    placeholderTextColor={"#17171729"}
                                    value={repeatedPassword}/>
                        </View>
                        <View style={styles.buttonBlock}>
                            <Pressable style={styles.button} onPress={() => console.log("Return")}>
                                <Text style={styles.buttonText}>Return</Text>
                            </Pressable>
                            <Pressable style={styles.button} onPress={() => {
                                console.log("Continue")}
                            }>
                                <Text style={styles.buttonText}>Continue</Text>
                            </Pressable>
                        </View>
                    </View>
                </View>
        </View>
        </KeyboardAvoidingContainer>
    )
}

const styles = StyleSheet.create({
    container: {
        justifyContent: "space-between",
        alignItems: "center",
        flex: 1,
    },
    logo: {
        width: 150,
        objectFit: "contain",
    },
    topBlock: {
        flex: 0.3,
        justifyContent: "flex-end"
    },
    mainBlock: {
        flex: 0.7,
        width: "60%",
        marginTop: 30,
    },
    buttonBlock: {
        flexDirection: "row",
        columnGap: 5,
        justifyContent: "center",
    },
    inputBlock: {
        marginTop: 15,
        marginBottom: 50,
        rowGap: 15,
    },
    loginBlock: {
        alignItems: "flex-end",
    },
    loginButtonText: {
        color: "#FFFFFF25"
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
    button: {
        backgroundColor: "#001E41",
        borderRadius: 30,
        paddingTop: 15,
        paddingBottom: 15,
        paddingRight: 30,
        paddingLeft: 30,
    },
    buttonText: {
        color: "white",
        fontSize: 14,
        // fontFamily: "Poppins-Black"
    }
  });
export default RegistrationForm;