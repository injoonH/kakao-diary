import { StyleSheet, Text, View } from 'react-native';
import { Calendar } from 'react-native-calendars';

const HomeScreen = ({ navigation }) => {
    return (
        <View style={styles.container}>
            <Text>Hello World</Text>
            <Calendar
                onDayPress={(day) => {
                    console.log('day pressed', day);
                    navigation.navigate('Diary', day.dateString);
                }}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
});

export default HomeScreen;
