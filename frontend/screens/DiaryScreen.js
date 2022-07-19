import { StyleSheet, View, Text, Pressable, TextInput } from 'react-native';
import { FontAwesome5, MaterialIcons } from '@expo/vector-icons';
import { useEffect, useState } from 'react';

const DiaryScreen = ({ navigation, route }) => {
    const [isEditMode, setIsEditMode] = useState(false);
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [diaryId, setDiaryId] = useState(null);

    const date = route.params;

    useEffect(() => {
        const fetchDiary = async () => {
            const res = await fetch(`http://192.249.18.122:80/diaries/${date}`);
            const json = await res.json();

            if (json.length > 0) {
                setTitle(json[0].title);
                setContent(json[0].content);
                setDiaryId(json[0].id);
                return;
            }

            setDiaryId(-1);
            
            setTitle('Default Title');
            setContent('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse feugiat sapien nisl, suscipit molestie ex hendrerit sed. Morbi ullamcorper mauris sit amet eleifend cursus. Nulla pharetra, nisl ut sollicitudin suscipit, mi nisi elementum neque, eu rutrum ex risus et mauris. Sed dictum ex nec eleifend fermentum. Quisque lacinia lacus neque, id sodales urna feugiat volutpat. Etiam malesuada justo a ex lobortis laoreet. Morbi ac risus eu ligula luctus dapibus in in ex. Proin quis nibh ut est tincidunt cursus non sed elit. Suspendisse arcu elit, luctus eget dictum quis, rutrum sit amet risus. Curabitur dictum libero cursus, feugiat ligula eget, sodales dolor. Praesent rutrum nisi vel varius vehicula. Aenean eu erat dignissim, molestie dui vitae, maximus nisl. Donec accumsan, magna in mollis sagittis, diam ante consectetur urna, vel feugiat leo diam ultricies ante. Phasellus maximus quis mauris ac bibendum. Suspendisse ac justo libero.');
        };

        fetchDiary();
    }, [date]);

    if (diaryId === null)
        return (
            <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
                <Text>로딩 중...</Text>
            </View>
        );
    
    if (diaryId === -1)
        return (
            <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
                <Text>해당 일자에 작성된 일기가 없습니다.</Text>
            </View>
        );

    return (
        <View style={{ flex: 1 }}>
            <View style={ styles.header }>
                <Pressable
                    style={ styles.backBtn }
                    onPress={() => navigation.goBack()}
                >
                    <FontAwesome5 name='chevron-left' size={ 28 } color='#B4C49A' />
                </Pressable>
                <View style={ styles.circle }>
                    <Text style={ styles.header_text }>{ date.split('-')[2] }</Text>
                </View>
                {
                    isEditMode ? (
                        <Pressable
                            style={ styles.checkBtn }
                            onPress={() => {
                                // TODO: Save updated title & content in DB
                                const updateDiary = async () => {
                                    const res = await fetch(`http://192.249.18.122:80/diaries/${diaryId}?title=${title}&content=${content}`, { method: 'PUT' });
                                    const json = await res.json();
                                    console.log('json', json);
                                };
                                updateDiary();
                                setIsEditMode(currMode => !currMode);
                            }}
                        >
                            <FontAwesome5 name='check' size={ 25 } color='#B4C49A'/>
                        </Pressable>
                    ) : (
                        <Pressable
                            style={ styles.editBtn }
                            onPress={() => {
                                setIsEditMode(currMode => !currMode);
                            }}
                        >
                            <MaterialIcons name='edit' size={ 27 } color='#B4C49A' />
                        </Pressable>
                    )
                }
            </View>
            {
                isEditMode ? (
                    <>
                        <View style={ styles.title }>
                            <TextInput
                                style={ styles.title_text }
                                value={ title }
                                onChangeText={ setTitle }
                            />
                        </View>
                        <View style={ styles.body }>
                            <TextInput
                                style={ styles.body_text }
                                value={ content }
                                onChangeText={ setContent }
                                multiline
                                autoFocus={ true }
                            />
                        </View>
                    </>
                ) : (
                    <>
                        <View style={ styles.title }>
                            <Text style={ styles.title_text }>{ title }</Text>
                        </View>
                        <View style={ styles.body }>
                            <Text style={ styles.body_text }>{ content }</Text>
                        </View>
                    </>
                )
            }
            <View style={ styles.footer }>
                <Text style={ styles.footer_text }>{ date }</Text>
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
        top: 85,
        right: 22,
    },

    checkBtn: {
        position: 'absolute',
        top: 85,
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
