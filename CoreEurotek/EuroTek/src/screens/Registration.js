import React from "react"
import { View, Image, StyleSheet } from "react-native"
import RegistrationForm from "../components/RegistrationForm"

const Registration = () => {
    return (
        <View style={styles.container}>
            <RegistrationForm />
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "space-around",
        alignItems: "center",
        backgroundColor: "#003867"
    }
})
export default Registration