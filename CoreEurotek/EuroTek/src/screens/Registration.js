import React from "react"
import { Platform, KeyboardAvoidingView, StyleSheet, View } from "react-native"
import RegistrationForm from "../components/RegistrationForm"

const Registration = () => {
    return (
        <KeyboardAvoidingView 
            behavior={Platform.OS == "ios" ? "padding" : "height"}
            style={{flex: 1}}
        >
            <RegistrationForm />
        </KeyboardAvoidingView >
    )
}
export default Registration