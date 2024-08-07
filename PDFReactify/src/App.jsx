import { PDFDownloadLink } from '@react-pdf/renderer';
import QuestionBankPDF from './components/QuestionBankPDF';
import questions from '../../Questions.json'; // Assume you have your questions in a JSON file

const App = () => (
  <div className="p-8">
    <h1 className="text-2xl font-bold mb-4">Question Bank</h1>
    <PDFDownloadLink
      document={<QuestionBankPDF questions={questions} />}
      fileName="question_bank.pdf"
    >
      {({ loading }) => (
        <button className="bg-gray-800 text-white py-2 px-4 rounded hover:bg-gray-700">
          {loading ? 'Loading document...' : 'Download PDF'}
        </button>
      )}
    </PDFDownloadLink>
  </div>
);
export default App;
