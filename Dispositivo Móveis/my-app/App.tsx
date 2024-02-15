import { StatusBar } from "expo-status-bar"
import { View, Text, Button, Alert, StyleSheet } from "react-native"

function App(){
  return(
    <View style={styles.container}>
      <StatusBar style="light"/>
      <Text>Hello, Android</Text>
      <Text>Hello, Android</Text>
      <Button title="Clique" onPress={alert} />
    </View>
  )
}

const styles = StyleSheet.create({
container: {
  backgroundColor: "#ff0000"
  }
})

export default App