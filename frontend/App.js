import { useFonts } from 'expo-font';
import { useEffect } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Navigation from './navigations/navigation';

const App = () => {
    const [loaded, error] = useFonts({
        'kangwonBold': require('./assets/fonts/kangwonBold.ttf'),
        'kangwonCute': require('./assets/fonts/kangwonCute.ttf'),
        'kangwonLight': require('./assets/fonts/kangwonLight.ttf'),
        'kangwonStrong': require('./assets/fonts/kangwonStrong.ttf'),
    });

    console.log(loaded ? 'Fonts loaded' : 'Fonts not loaded');

    if (!loaded) {
        return (
            <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
                <Text>Loading Fonts...</Text>
            </View>
        )
    }

    return (
        <View style={styles.root}>
            <Navigation />
        </View>
    );
};

const styles = StyleSheet.create({
    root: {
        width: '100%',
        height: '100%',
        backgroundColor: '#F5F5F5',
    }
});

export default App;
