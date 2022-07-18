import { StyleSheet, View, Text, Alert, Pressable, TextInput, KeyboardAvoidingView } from 'react-native';
import { MaterialIcons } from '@expo/vector-icons';
import { FontAwesome5 } from '@expo/vector-icons';
import { useEffect, useState } from 'react';

const DiaryScreen = ({ navigation, route }) => {
    const [isEditMode, setIsEditMode] = useState(false);
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    const date = route.params;

    useEffect(() => {
        // 서버에서 title과 content 가져오기
        setTitle('그라데이션 10cm');
        setContent(
`밤은 다시 길고 깊어졌네
나는 점점 너로 잠 못 들게 돼
글로 적어내긴 어려운 이 기분을
너도 느꼈으면 좋겠는데
\n
너는 아무 생각 없이 몇 번
나를 지나가며 웃은 거라지만
나의 하얀 옷에 너의 잉크가 묻어
닦아낼 수 없을 만큼 번졌네
\n
달콤한 색감이 물들어 조금씩
정신을 차렸을 땐 알아볼 수도 없지
가득 찬 마음이 여물다 못해 터지고 있어
내일은 말을 걸어봐야지`);
    }, []);

    return (
        <View style={{ flex: 1 }}>
            <View style={styles.header}>
                <Pressable
                    style={styles.backBtn}
                    onPress={() => navigation.goBack()}
                >
                    <FontAwesome5 name="chevron-left" size={28} color="#B4C49A" />
                </Pressable>
                <View style={styles.circle}>
                    <Text style={styles.header_text}>{date.split('-')[2]}</Text>
                </View>
            </View>
            {
                isEditMode ? (
                    <>
                        <Pressable
                            style={styles.checkBtn}
                            onPress={() => setIsEditMode(currMode => !currMode)}
                        >
                            <FontAwesome5 name="check" size={25} color="#B4C49A"/>
                        </Pressable>
                        <View style={styles.title}>
                            <TextInput style={styles.title_text} value={ title } onChangeText={setTitle} />
                        </View>
                        <View style={styles.body}>
                            <TextInput style={styles.body_text} value={ content } onChangeText={setContent} multiline />
                        </View>
                    </>
                ) : (
                    <>
                        <Pressable
                            style={styles.editBtn}
                            onPress={() => setIsEditMode(currMode => !currMode)}
                        >
                            <MaterialIcons name="edit" size={27} color="#B4C49A" />
                        </Pressable>
                        <View style={styles.title}>
                            <Text style={styles.title_text}>{ title }</Text>
                        </View>
                        <View style={styles.body}>
                            <Text style={styles.body_text}>{ content }</Text>
                        </View>
                    </>
                )
            }
            
            <View style={styles.footer}>
                <Text style={styles.footer_text}>{ date }</Text>
            </View>
        </View>
    )
};

const dayCircleDiameter = 60;

const styles = StyleSheet.create({
    // 레이아웃
    header: {
        flex: 4,
        marginTop: 20,
        justifyContent: 'center',
        alignItems: 'center',
    },
    title: {
        flex: 2,
        marginTop: -40,
        justifyContent: 'center',
        alignItems: 'center',
        // backgroundColor: '#B4C49A',
    },
    body: {
        flex: 8,
        //justifyContent: 'center',
        // alignItems: 'center',
        marginTop: 20,
        marginLeft: 60,
        marginRight: 60,
    },
    footer: {
        flex: 3,
        justifyContent: 'center',
        alignItems: 'center',
        // backgroundColor: '#B4C49A'
    },

    // 요소
    circle: {
        borderRadius: dayCircleDiameter / 2,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#B4C49A',
        width: dayCircleDiameter,
        height: dayCircleDiameter,
    },
    backBtn: {
        position: 'absolute',
        top: 85,
        left: 22,
    },

    editBtn: {
        position: 'absolute',
        top: 107,
        right: 22,
    },

    checkBtn: {
        position: 'absolute',
        top: 107,
        right: 24,
    },

    // 텍스트 폰트 설정
    header_text: {
        fontFamily: 'kangwonBold',
        fontSize: 26,
        color: '#FFFFFF',
    },

    title_text: {
        fontFamily: 'kangwonBold',
        fontSize: 26,
        color: '#1A1A1A',
        textAlign: 'center',
    },

    body_text: {
        fontFamily: 'kangwonLight',
        fontSize: 18,
        color: '#5B5454',
        textAlign: 'center',
    },

    footer_text: {
        fontFamily: 'kangwonLight',
        fontSize: 18,
        color: '#5B5454',
    },
})

export default DiaryScreen;
