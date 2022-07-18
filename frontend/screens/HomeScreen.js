import { StyleSheet, Text, View } from 'react-native';
import { Calendar, LocaleConfig } from 'react-native-calendars';
import { FontAwesome5 } from '@expo/vector-icons';

LocaleConfig.locales['fr'] = {
    monthNames: [
        'Janvier',
        'Février',
        'Mars',
        'Avril',
        'Mai',
        'Juin',
        'Juillet',
        'Août',
        'Septembre',
        'Octobre',
        'Novembre',
        'Décembre'
      ],
      monthNamesShort: ['Jan', 'Feb', 'Mar', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      dayNames: ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'],
      dayNamesShort: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      today: "Aujourd'hui"
};
LocaleConfig.defaultLocale = 'fr';

const dayCircleDiameter = 60;

const HomeScreen = ({ navigation }) => {
    return (
        <View style={styles.container}>
            <View style={styles.circle}></View>
            <View style={{ height: 465, zIndex: 1 }}>
                <Calendar style={styles.calendar}
                    renderArrow={(direction) => {
                        return (
                            <FontAwesome5 name={`chevron-${direction}`} size={14} color='#B4C49A' />
                        );
                    }}
                    monthFormat={'MMM'}
                    enableSwipeMonths={true}
                    theme={{
                        'stylesheet.calendar.header': {
                            week: styles.week
                        },
                        // 'stylesheet.calender.arrowImage': {
                        //     arrow: styles.arrow
                        // },
                        // 'stylesheet.calendar.disabledArrowImage': {
                        //     tintColor: appStyle.disabledArrowColor
                        // },
                        backgroundColor: '#F5F5F5',
                        calendarBackground: '#F5F5F5',
                        dotColor: '#B4C49A',
                        todayTextColor: '#FFFFFF',
                        todayBackgroundColor: '#B4C49A',
                        dayTextColor: '#5B5454',
                        monthTextColor: '#FFFFFF',
                        textDayFontFamily: 'kangwonLight',
                        textMonthFontFamily: 'kangwonBold',
                        textDayHeaderFontFamily: 'kangwonBold',
                        textDayFontSize: 18,
                        textMonthFontSize: 24,
                        textDayHeaderFontSize: 18,
                    }}
                    markedDates={{'2022-07-17': {marked: true}}}
                    onDayPress={(day) => {
                        console.log('day pressed', day);
                        navigation.navigate('Diary', day.dateString);
                    }}
                />
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    //레이아웃
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#F5F5F5',
    },
    calendar:{
        width: 350,
        backgroundColor: '#FFFFFF00',
    },
    week: {
        paddingHorizontal: 7,
        marginTop: 100,
        flexDirection: 'row',
        justifyContent: 'space-between',
        textColor: '#787878',
    },
    // 요소
    circle: {
        position: 'absolute',
        top: 190,
        borderRadius: dayCircleDiameter / 2,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#B4C49A',
        width: dayCircleDiameter,
        height: dayCircleDiameter,
        zIndex: 0,
    },
});

export default HomeScreen;
