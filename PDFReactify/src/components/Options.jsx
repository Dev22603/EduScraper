import React from 'react';
import { Text, View } from '@react-pdf/renderer';
import PropTypes from 'prop-types';
import styles from './styles'; // Import styles from a separate file

const Options = ({ options }) => {
  return (
    <View style={styles.optionsGrid}>
      {options.map((option, index) => (
        <View key={index} style={styles.optionItem}>
          <Text style={styles.optionText}>
            {String.fromCharCode(65 + index)}. {option}
          </Text>
        </View>
      ))}
    </View>
  );
};

Options.propTypes = {
  options: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default Options;
