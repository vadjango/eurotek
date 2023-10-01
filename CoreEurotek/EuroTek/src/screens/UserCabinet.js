import React, { useState, useEffect } from "react";
import { View, Text, StyleSheet, Button } from "react-native"
import { storage } from "../components/Storage";

const UserCabinet = () => {
    const authDataString = storage.getString("auth");
    console.log(authDataString);
    let authData = null;
    if (authDataString) {
        authData = JSON.parse(authDataString);
    }

    return (
        <View style={styles.container}>
            <View style={{height: "30%"}}>
                <Text style={styles.text}>{(authData) ? `${authData.user.first_name} ${authData.user.last_name}` : "Anonymous"}</Text>
                <Button title="Logout"/>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#003867",
        flex: 1
    },
    text: {
        fontSize: 30,
        color: "white"
    }
})
export default UserCabinet