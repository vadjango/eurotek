import React from "react"
import { SafeAreaView, StyleSheet, StatusBar } from "react-native"
// import Registration from "./src/screens/Registration"
import Report from "./src/experiments/Report"
 

const App = () => {  

  return (
      <SafeAreaView style={styles.container}>
        {/* <Registration /> */}
        <Report />
      </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "darkblue",
    paddingTop: StatusBar.currentHeight,
  }
})

export default App;