import { StyleSheet } from '@react-pdf/renderer';

const styles = StyleSheet.create({
  page: {
    padding: 30,
  },
  questionContainer: {
    borderWidth: 1,
    borderColor: '#e5e7eb',
    borderRadius: 8,
    padding: 16,
    marginBottom: 20,
    breakInside: 'avoid', // Prevent question break
  },
  questionText: {
    fontSize: 14,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  optionText: {
    fontSize: 12,
  },
  optionsGrid: {
    display: 'flex',
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    gap: 10, // Adjust gap as needed
  },
  optionItem: {
    width: '48%', // Adjust width to ensure 2 items per row
  },
  answerKeyContainer: {
    marginTop: 32,
  },
  table: {
    display: 'table',
    width: 'auto',
    borderStyle: 'solid',
    borderWidth: 1,
    borderColor: '#e5e7eb',
    marginTop: 20,
  },
  tableRow: {
    flexDirection: 'row',
  },
  tableCol: {
    width: '20%',
    borderStyle: 'solid',
    borderWidth: 1,
    borderColor: '#e5e7eb',
    textAlign: 'center',
  },
  tableCell: {
    margin: 5,
    fontSize: 10,
  },
  answerKeyText: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 8,
  },
});

export default styles;
