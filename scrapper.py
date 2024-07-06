import requests
from bs4 import BeautifulSoup
import urllib3

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
        options = [opt.get_text(strip=True) for opt in question.select('.bix-tbl-options .bix-td-option-val div')]
        answer = question.select_one('.jq-hdnakq')['value']
        explanation = question.select_one('.bix-ans-description').get_text(strip=True) if question.select_one('.bix-ans-description') else 'N/A'
        mcqs.append({
            'question': q_text,
            'options': options,
            'answer': answer,
            'explanation': explanation
        })
    return mcqs

# Function to save MCQs to a text file
def save_mcqs(mcqs, topic_name):
    with open(f'{topic_name}.txt', 'a', encoding='utf-8') as file:
        for mcq in mcqs:
            file.write(f"Q: {mcq['question']}\n")
            for opt in mcq['options']:
                file.write(f"{opt}\n")
            file.write(f"Answer: {mcq['answer']}\n")
            file.write(f"Explanation: {mcq['explanation']}\n")
            file.write("\n")

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
