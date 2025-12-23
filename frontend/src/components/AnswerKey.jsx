import React from 'react';
import { Text, View } from '@react-pdf/renderer';
import PropTypes from 'prop-types';
import styles from './styles'; // Import styles from a separate file

const AnswerKey = ({ answers }) => {
  const chunkedAnswers = [];
  for (let i = 0; i < answers.length; i += 10) {
    chunkedAnswers.push(answers.slice(i, i + 10));
  }

  return (
    <View style={styles.answerKeyContainer}>
      <Text style={styles.answerKeyText}>Answer Key</Text>
      <View style={styles.table}>
        {chunkedAnswers.map((chunk, rowIndex) => (
          <View style={styles.tableRow} key={rowIndex}>
            {chunk.map(({ number, answer }) => (
              <View style={styles.tableCol} key={number}>
                <Text style={styles.tableCell}>{number}. {answer}</Text>
              </View>
            ))}
          </View>
        ))}
      </View>
    </View>
  );
};

AnswerKey.propTypes = {
  answers: PropTypes.arrayOf(
    PropTypes.shape({
      number: PropTypes.number.isRequired,
      answer: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default AnswerKey;
