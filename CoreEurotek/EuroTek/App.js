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

const Pages = {
  REGISTRATION: "Registration",
  LOGIN: "Login",
  USER_CABINET: "UserCabinet"
}


function App() {  
  const [fontsLoaded] = useFonts({
    Poppins: require("./assets/fonts/Poppins-Regular.ttf"),
  });

  const [error, setError] = useState(null);
  const [refreshed, setRefreshed] = useState(false);
  const [initPageName, setInitPageName] = useState("");

  useEffect(() => {
    if (!storage.getString("auth")) {
      setInitPageName(Pages.REGISTRATION);
    }
    const authData = JSON.parse(storage.getString("auth"));
    axios.get(AppBaseURL + "report/", {
        headers: {
            Authorization: `Bearer ${authData.access}`
        }
    })
    .then((response) => {
        // console.log(response.data);
        // setReports(response.data);
        setInitPageName(Pages.USER_CABINET);
    })
    .catch((e) => {
        // if status is 401, it means our access token is expired. Trying to get another one.
        if (e.response.status == 401 && e.response.data["code"] === "token_not_valid") {
            axios.post(AppBaseURL + "auth/refresh/", {
                "refresh": authData.refresh
            })
            .then((response) => {
                authData.access = response.data.access;
                storage.set("auth", JSON.stringify(authData));
                setRefreshed(true);
            })
            .catch((e) => {
                setInitPageName(Pages.LOGIN)
            })
        } else {
            setError(e);
        }
    })
  }, [refreshed])

  if (!fontsLoaded) {
    return null
  }

  console.log("Page has been rendered, wow!");


  return (
      <SafeAreaView style={styles.container}>
        <StatusBar backgroundColor={"#003867"} />
        <NavigationContainer>
          <Stack.Navigator screenOptions={{headerShown: false}} initialRouteName={initPageName}>
            <Stack.Screen component={RegistrationForm} name={Pages.REGISTRATION} />
            <Stack.Screen component={LoginForm} name={Pages.LOGIN} />
            <Stack.Screen component={UserCabinet} name={Pages.USER_CABINET} />
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