import { StyleSheet, Text, View } from 'react-native';
import { Calendar } from 'react-native-calendars';

const HomeScreen = ({ navigation }) => {
    return (
        <View style={styles.container}>
            <Calendar style={styles.calendar}
                theme={{
                    backgroundColor: '#F5F5F5',
                    calendarBackground: '#F5F5F5',
                    dotColor: '#B4C49A',
                    todayTextColor: '#B4C49A',
                    dayTextColor: '#5B5454',
                    disabledArrowColor: '#B4C49A',
                    textDayFontFamily: 'kangwonLight',
                    textMonthFontFamily: 'kangwonBold',
                    textDayHeaderFontFamily: 'kangwonBold',
                    // textDayFontSize: 18,
                    // textMonthFontSize: 20,
                    // textDayHeaderFontSize: 18,
                }}
                markedDates={{'2022-07-17': {marked: true}}}
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
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#F5F5F5',
    },
});

export default HomeScreen;
