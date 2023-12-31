import React from "react"
import { Pressable, Text, StyleSheet } from "react-native"

const FormLinkButton = ({text, onSubmit}) => {
    return (
        <Pressable onPress={onSubmit}>
            <Text style={styles.buttonText}>{text}</Text>
        </Pressable>
    )
}

const styles = StyleSheet.create({
    buttonText: {
        color: "#FFFFFF25"
    }
})
export default FormLinkButton