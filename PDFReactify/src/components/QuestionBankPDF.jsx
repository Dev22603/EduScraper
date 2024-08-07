import React from 'react';
import { Page, Document } from '@react-pdf/renderer';
import PropTypes from 'prop-types';
import Question from './Question';
import AnswerKey from './AnswerKey';
import styles from './styles'; // Import styles from a separate file

const QuestionBankPDF = ({ questions }) => {
  const answers = questions.map((q, index) => ({
    number: index + 1,
    answer: q['Correct Option']
  }));

  return (
    <Document>
      <Page size="A4" style={styles.page}>
        {questions.map((question, index) => (
          <Question
            key={index}
            question={question.Question}
            options={question.Options}
          />
        ))}
        <AnswerKey answers={answers} />
      </Page>
    </Document>
  );
};

QuestionBankPDF.propTypes = {
  questions: PropTypes.arrayOf(
    PropTypes.shape({
      Question: PropTypes.string.isRequired,
      Options: PropTypes.arrayOf(PropTypes.string).isRequired,
      'Correct Option': PropTypes.string.isRequired,
      Explanation: PropTypes.string,
      Topic: PropTypes.string,
    })
  ).isRequired,
};

export default QuestionBankPDF;
