import os
import requests
from bs4 import BeautifulSoup
import urllib3
import pandas as pd
# Suppress the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Function to get all topic URLs


def get_topics(base_url):
    response = requests.get(base_url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    topics = []
    for link in soup.select('ul.need-ul-filter a'):
        topic_url = link['href']
        topics.append(topic_url)
    return topics

# Function to get all pages for a given topic


def get_topic_pages(topic_url):
    pages = [topic_url]
    response = requests.get(topic_url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Select all page links from the pagination
    pagination = soup.select('ul.pagination a.page-link')
    for page in pagination:
        page_url = page['href']
        if page_url.startswith('http') and page_url not in pages:
            pages.append(page_url)

    return pages

# Function to get MCQs from a given page


def get_mcqs(page_url):
    response = requests.get(page_url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    mcqs = []
    for question in soup.select('.bix-div-container'):
        q_text = question.select_one('.bix-td-qtxt').get_text(strip=True)
        options = [opt.get_text(strip=True) for opt in question.select(
            '.bix-tbl-options .bix-td-option-val div')]
        answer = question.select_one('.jq-hdnakq')['value']
        explanation = question.select_one('.bix-ans-description').get_text(
            strip=True) if question.select_one('.bix-ans-description') else 'N/A'
        mcqs.append({
            'question': q_text,
            'options': options,
            'answer': answer,
            'explanation': explanation
        })
    return mcqs

# Function to save MCQs to a text file


def save_mcqs(mcqs, topic_name):
    directory = 'Aptitude'
    if not os.path.exists(directory):
        os.makedirs(directory)
    Columns = ["Question Number", "Question", "A",
               "B", "C", "D", "Correct Option", "explaination", "Topic"]

    question_numbers = []
    questions = []
    A = []
    B = []
    C = []
    D = []
    correct_options = []
    explanations = []
    topics = []

    with open(f'{directory}/{topic_name}.txt', 'a', encoding='utf-8') as file:
        for (index, mcq) in enumerate(mcqs):
            question_numbers.append(index+1)
            questions.append(mcq['question'])
            print(mcq['options'])
            A.append(mcq['options'][0])
            if len(mcq['options']) > 1:
                B.append(mcq['options'][1])
            else:
                B.append('NA')
            if len(mcq['options']) > 2:
                C.append(mcq['options'][2])
            else:
                C.append('NA')
            if len(mcq['options']) > 3:
                D.append(mcq['options'][3])
            else:
                D.append('NA')
            correct_options.append(mcq['answer'])
            explanations.append(mcq['explanation'])
            topics.append(topic_name)

            file.write(f"Q: {mcq['question']}\n")
            for opt in mcq['options']:
                file.write(f"{opt}\n")
            file.write(f"Answer: {mcq['answer']}\n")
            file.write(f"Explanation: {mcq['explanation']}\n")
            file.write("\n")
    data = {
        "Question Number": question_numbers,
        "Question": questions,
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "Correct Option": correct_options,
        "Explanation": explanations,
        "Topic": topics
    }
    Questions = pd.DataFrame(data)
    Questions.to_csv(f'Questions.csv', index=False, encoding='utf-8')


# Main function to scrape all topics and their pages


def main():
    base_url = 'https://www.indiabix.com/aptitude/questions-and-answers/'
    topics = get_topics(base_url)

    for topic in topics:
        topic_name = topic.split('/')[-2]
        pages = get_topic_pages(topic)

        for page in pages:
            mcqs = get_mcqs(page)
            save_mcqs(mcqs, topic_name)


if __name__ == "__main__":
    main()
