import React from 'react';
import { Text, View } from '@react-pdf/renderer';
import PropTypes from 'prop-types';
import Options from './Options';
import styles from './styles'; // Import styles from a separate file

const Question = ({ question, options }) => (
  <View style={styles.questionContainer}>
    <Text style={styles.questionText}>{question}</Text>
    <Options options={options} />
  </View>
);

Question.propTypes = {
  question: PropTypes.string.isRequired,
  options: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default Question;
