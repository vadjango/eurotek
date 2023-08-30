import React from "react"
import { SafeAreaView, View, StyleSheet, StatusBar, useWindowDimensions, Platform } from "react-native"
import RegistrationForm from "./src/components/Registration/PageTwo"
import { useFonts } from "expo-font"
// import ReportPage from "./src/experiments/ReportPage"


const App = () => {  

  const [loaded] = useFonts({
    Poppins: require("./assets/fonts/Poppins-Regular.ttf"),
  })

  if (!loaded) return null;

  return (
      <SafeAreaView style={styles.container}>
        <StatusBar backgroundColor={"#003867"} />
        <RegistrationForm />
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