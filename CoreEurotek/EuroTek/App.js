import React, { useState, useEffect } from "react"
import { SafeAreaView, View, StyleSheet, StatusBar, useWindowDimensions, Platform } from "react-native"
import UserCabinet from "./src/screens/UserCabinet"
import AppBaseURL from "./src/AppBaseURL"
import { useFonts } from "expo-font"
import { storage } from "./src/components/Storage"
import axios from "axios"
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import RegistrationForm from "./src/screens/RegistrationForm"
import LoginForm from "./src/screens/Login"

const Stack = createNativeStackNavigator();


function App() {  
  console.log(storage.getString("auth"));
  const [fontsLoaded] = useFonts({
    Poppins: require("./assets/fonts/Poppins-Regular.ttf"),
  });

  const [loaded, setLoaded] = useState(false);
  const [error, setError] = useState(null);
  const [refreshed, setRefreshed] = useState(false);

  useEffect(() => {
    // if (!fontsLoaded) return;
    const authData = JSON.parse(storage.getString("auth"));
    axios.get(AppBaseURL + "report/", {
        headers: {
            Authorization: `Bearer ${authData.access}`
        }
    })
    .then((response) => {
        // console.log(response.data);
        // setReports(response.data);
        setLoaded(true);
    })
    .catch((e) => {
        // if status is 401, it means our access token is expired. Trying to get another one.
        if (e.response.status == 401) {
            axios.post(AppBaseURL + "auth/refresh/", {
                "refresh": authData.refresh
            })
            .then((response) => {
                authData.access = response.data.access;
                storage.set("auth", JSON.stringify(authData));
                setRefreshed(true);
            })
            .catch((e) => {
                setError(e);
                setLoaded(true);
            })
        } else {
            setError(e);
        }
    })
}, [refreshed, fontsLoaded])

if (!loaded) return null;

function isTokenValid() {
  if (error) {
    if (error.response.data["code"] === "token_not_valid") {
      return false
    }
  }
  return true
}


  return (
      <SafeAreaView style={styles.container}>
        <StatusBar backgroundColor={"#003867"} />
        <NavigationContainer>
          <Stack.Navigator screenOptions={{headerShown: false}} initialRouteName={(isTokenValid()) ? "UserCabinet" : "Login"}>
            <Stack.Screen component={RegistrationForm} name="Registration" />
            <Stack.Screen component={LoginForm} name="Login" />
            <Stack.Screen component={UserCabinet} name="UserCabinet" />
          </Stack.Navigator>
        </NavigationContainer>
      </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#003867",
    paddingTop: StatusBar.currentHeight || 0,
  }
})

export default App;