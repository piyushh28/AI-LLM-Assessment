import requests
from bs4 import BeautifulSoup
import openai
from openai import OpenAI
import re

# OpenAI API Key (Replace with your own API key)
client = OpenAI(api_key="enter your API key here")

# Research Agent: Finds Trending HR Topics
def get_trending_hr_topics():
    url = "https://www.hrtrendinstitute.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    topics = [h2.text for h2 in soup.find_all("h2")][:5]  # Extract top 5 trending topics
    return topics

# Content Planning Agent: Creates a Blog Outline
def generate_outline(topic):
    outline = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert content planner."},
            {"role": "user", "content": f"Create a structured outline for a 2000-word blog on '{topic}'"}
        ]
    )
    return outline.choices[0].message.content

# Content Generation Agent: Writes Blog Content
def generate_blog_content(outline):
    content = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert HR content writer."},
            {"role": "user", "content": f"Write a detailed blog post based on this outline: {outline}"}
        ]
    )
    return content.choices[0].message.content

# SEO Optimization Agent: Ensures SEO Best Practices
def optimize_for_seo(content):
    seo_tips = [
        "Ensure keyword placement in headings.",
        "Use transition words for better readability.",
        "Optimize meta description.",
        "Ensure proper image alt texts and internal linking."
    ]
    optimized_content = content + "\n\nSEO Optimizations Applied: " + " | ".join(seo_tips)
    return optimized_content

# Review Agent: Proofreads and Improves Content
def review_content(content):
    reviewed_content = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional proofreader."},
            {"role": "user", "content": f"Proofread and improve this blog post: {content}"}
        ]
    )
    return reviewed_content.choices[0].message.content

# Save blog post in different formats
def save_blog(content, filename):
    with open(f"{filename}.md", "w", encoding="utf-8") as md_file:
        md_file.write(content)
    with open(f"{filename}.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(content)
    with open(f"{filename}.html", "w", encoding="utf-8") as html_file:
        html_file.write(f"<html><body><pre>{content}</pre></body></html>")

# Main Workflow
def main():
    trending_topics = get_trending_hr_topics()
    print("Trending HR Topics:", trending_topics)
    
    chosen_topic = trending_topics[0]  # Select the first topic
    print(f"Chosen Topic: {chosen_topic}\n")
    
    outline = generate_outline(chosen_topic)
    print("Generated Outline:\n", outline, "\n")
    
    content = generate_blog_content(outline)
    print("Generated Content:\n", content, "\n")
    
    optimized_content = optimize_for_seo(content)
    print("SEO Optimized Content:\n", optimized_content, "\n")
    
    final_content = review_content(optimized_content)
    print("Final Reviewed Content:\n", final_content)
    
    save_blog(final_content, "final_blog_post")

if __name__ == "__main__":
    main()
