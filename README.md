# Multi-Agent HR Blog Generator

## System Architecture
The project follows a modular multi-agent system design, where each agent is responsible for a specific task in generating a high-quality, SEO-optimized blog post on a trending HR topic.

### Components:
1. **Research Agent**: Scrapes HR websites to find trending HR topics.
2. **Content Planning Agent**: Creates a structured blog outline.
3. **Content Generation Agent**: Writes a comprehensive blog post based on the outline.
4. **SEO Optimization Agent**: Enhances the blog content with SEO best practices.
5. **Review Agent**: Proofreads and improves the overall readability of the content.

## Agent Workflow
1. **Research Agent** scrapes HR-related websites to find the latest trending topics.
2. **Content Planning Agent** structures a blog outline based on the chosen topic.
3. **Content Generation Agent** writes a detailed 2000-word blog using GPT-4.
4. **SEO Optimization Agent** ensures the blog follows best SEO practices, including keyword placement, meta descriptions, and content formatting.
5. **Review Agent** proofreads and refines the final content.
6. The final blog post is saved in multiple formats (Markdown, HTML, TXT).

## Tools and Frameworks Used
- **Python**: Primary programming language
- **BeautifulSoup**: Web scraping for collecting trending HR topics
- **Requests**: Fetching data from web pages
- **OpenAI API**: GPT-40-mini for content generation, outlining, and proofreading

## Installation and Execution Steps
### Prerequisites
Ensure Python is installed on your system (Python 3.7+ recommended).

### Step 1: Clone the Repository
```bash
git clone https://github.com/piyushh28/AI-LLM-Assessment
cd AI-LLM-Assessment
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up OpenAI API Key
Replace `your_api_key_here` in the script with your actual OpenAI API key.

### Step 4: Run the Script
```bash
python main.py
```

### Step 5: View Generated Blog Post
The final blog post will be saved in multiple formats:
- `final_blog_post.md`
- `final_blog_post.txt`
- `final_blog_post.html`


This project automates blog writing using AI-powered agents, ensuring high-quality, SEO-optimized content with minimal manual effort.

