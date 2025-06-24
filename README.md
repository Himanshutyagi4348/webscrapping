
🌐 LangChain Web Scraper
A high-performance web scraper built with LangChain that fetches pages using headless Chromium, parses HTML into clean text, and prepares it for LLM workflows—with parallelism built in.

🚀 Key Enhancements
Async page loading via AsyncChromiumLoader

Parallel I/O fetching using ThreadPoolExecutor to handle network-bound tasks concurrently 
medium.com
+15
scrapingant.com
+15
reddit.com
+15
reddit.com
webscrapingsite.com

CPU-intensive parsing offloaded to separate processes with Python’s multiprocessing.Pool

Best-of-both performance: threads maximize network throughput and processes utilize multiple CPU cores efficiently

🛠️ Quick Setup
Install dependencies:

bash
Copy
Edit
pip install playwright beautifulsoup4 langchain-community
playwright install
Run the scraper:

bash
Copy
Edit
python main.py
⚙️ Example Workflow
python
Copy
Edit
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer

urls = [...]  # target URLs

# Fetch pages concurrently (I/O-bound)
with ThreadPoolExecutor(max_workers=8) as executor:
    raw_pages = executor.map(lambda u: AsyncChromiumLoader([u]).load()[0], urls)

# Parse pages in parallel (CPU‑bound)
with Pool(cpu_count()) as pool:
    parsed = pool.map(BeautifulSoupTransformer().transform_documents, raw_pages)

# parsed is now clean text ready for LLM analysis
💡 Benefits
Fast I/O: Multiple threads perform network requests simultaneously, drastically reducing wait time 
webscrapingsite.com
+3
medium.com
+3
33rdsquare.com
+3
parazun.com

Efficient parsing: Using all CPU cores to handle parsing workloads boosts processing throughput 
zenrows.com
+4
webscrapingsite.com
+4
scrapingant.com
+4

Scalable: Easily tune thread and process counts based on system and target server capacity 
reddit.com
+1
scrapingant.com
+1
