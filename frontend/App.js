import { StyleSheet, Text, View } from 'react-native';
import Navigation from './navigations/navigation';

const App = () => {
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
        backgroundColor: '#0ead90',
    }
});

export default App;
