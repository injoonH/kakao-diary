import { StyleSheet, View, Text } from 'react-native';
import React from 'react';

const DiaryScreen = ({ route }) => {
    const date = route.params;

    return (
        <View style={styles.container}>
            <Text>DiaryScreen</Text>
            <Text>{ date }</Text>
        </View>
    )
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
})

export default DiaryScreen;
