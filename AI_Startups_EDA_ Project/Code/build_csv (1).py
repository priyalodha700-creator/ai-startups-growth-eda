import pandas as pd

data = [
# rank, name, search_growth_raw, growth_status, year_founded, location, funding_raw, funding_series, description
(1, "DeepL", "320%", "Exploding", 2009, "Cologne, Germany", "$400M", "Series Unknown", "Neural machine translation platform supporting 30+ languages for websites, documents, and emails."),
(2, "Frame AI", "1,088%", "Exploding", 2016, "New York City, New York", "$17.9M", "Series B", "AI customer success platform that detects themes in customer feedback via 'Voice of the Customer engine'."),
(3, "Uizard", "3,233%", "Exploding", 2018, "Copenhagen, Denmark", "$18.6M", "Series A", "AI platform that turns sketches/wireframes into functional app and website designs."),
(4, "Moveworks", "332%", "Exploding", 2016, "Mountain View, CA", "$305M", "Series C", "AI workplace platform using NLU and conversational AI to resolve employee IT/HR issues end-to-end."),
(5, "Databricks", "471%", "Exploding", 2013, "San Francisco, California", "$4B", "Series Unknown", "Unified data and AI analytics platform for building and deploying ML applications at scale."),
(6, "Synthesia", "5,100%", "Regular", 2017, "London, England", "$156.6M", "Series C", "AI video generation platform creating realistic videos with human-like avatars for e-learning and marketing."),
(7, "Codeium", "99x+", "Exploding", 2021, "San Jose, California", "$243M", "Series C", "AI coding assistant offering real-time code suggestions, search, and IDE integration."),
(8, "Cohere", "860%", "Exploding", 2019, "Toronto, Canada", "$942.9M", "Series D", "Enterprise LLM company with Command (generation), Embed (embeddings), and Rerank (search) models."),
(9, "Soundful", "4,100%", "Regular", 2019, "San Diego, California", "$4.5M", "Seed", "AI platform generating customizable soundtracks for videos, podcasts, and ads."),
(10, "Dialpad", "6,700%", "Regular", 2011, "San Francisco, California", "$450M", "Series F", "AI customer intelligence platform for video meetings, call recording, and conversational chatbots."),
(11, "Yellow.AI", "1,329%", "Exploding", 2016, "San Mateo, California", "$102.2M", "Series C", "Conversational AI/automation platform for customer service, sales, and marketing across 135+ languages."),
(12, "PlayHT", "9,800%", "Exploding", 2022, "San Francisco, California", "$2.2M", "Pre-Seed", "AI text-to-speech platform with 900+ voices in 142 languages, voice cloning, and API access."),
(13, "MindsDB", "6,200%", "Regular", 2017, "Berkeley, California", "$54.4M", "Seed", "Open-source AutoML platform for training and deploying predictive models without coding."),
(14, "Shield AI", "525%", "Exploding", 2015, "San Diego, CA", "$1.1B", "Debt Financing", "Defense tech company building autonomous drones and AI command/control software for military use."),
(15, "Eightfold", "567%", "Exploding", 2016, "Santa Clara, California", "$396.8M", "Series E", "AI-powered HR platform for talent acquisition, retention, and training."),
(16, "Netra", "57%", "Regular", 2013, "Boston, MA", "$3.9M", "Seed", "AI video analysis platform for safety analysis, metadata analysis, and object detection."),
(17, "Deepgram", "4,900%", "Exploding", 2015, "San Francisco, CA", "$85.9M", "Series B", "AI speech recognition platform transcribing and analyzing audio/video with high accuracy."),
(18, "Arthur AI", "650%", "Exploding", 2017, "New York, New York", "$60.3M", "Series B", "AI/ML model monitoring and bias detection platform; also builds LLM firewall Arthur Shield."),
(19, "OpenAI", "3,800%", "Regular", 2015, "San Francisco, CA", "$11.3B", "Secondary Market", "AI research company aiming for AGI; best known for ChatGPT."),
(20, "Capacity", "1,183%", "Exploding", 2017, "St. Louis, Missouri", "$61.5M", "Series C", "Fully AI-powered helpdesk that learns from employee-customer interactions."),
(21, "Read AI", "1,567%", "Exploding", 2020, "Seattle, Washington", "$31M", "Series A", "AI meeting-engagement tool measuring attendee engagement, talk-time, and sentiment in real time."),
(22, "Dataiku", "102%", "Regular", 2013, "Paris, France", "$846.8M", "Series F", "Enterprise AI platform/workbench for building customized AI and ML solutions."),
(23, "PhotoRoom", "99x+", "Exploding", 2019, "Paris, France", "$62.1M", "Series B", "AI photo editing app/API automating background removal, resizing, and blurring."),
(24, "DNSFilter", "150%", "Exploding", 2015, "Washington, DC", "$62.1M", "Series Unknown", "AI-powered cybersecurity platform protecting against phishing, ransomware, and malware."),
(25, "Spot AI", "717%", "Exploding", 2018, "Los Altos, CA", "$62M", "Series B", "AI platform analyzing consumer behavior for personalized marketing recommendations."),
(26, "Interactions", "6,900%", "Exploding", 2013, "Franklin, MA", "$162.8M", "Series Unknown", "Virtual assistant platform for enterprise customer experience, handling 2B+ annual conversations."),
(27, "Fireflies.AI", "9,800%", "Exploding", 2016, "San Francisco, California", "$19M", "Series A", "AI meeting assistant that records, transcribes, summarizes, and analyzes meetings."),
(28, "Otter AI", "3,233%", "Exploding", 2016, "Mountain View, California", "$63M", "Series B", "Speech-to-text transcription startup with automated meeting notes and action-item extraction."),
(29, "AssemblyAI", "8,100%", "Regular", 2017, "San Francisco, CA", "$158.1M", "Series C", "AI speech-to-text and NLP platform for real-time transcription and analysis."),
(30, "LogicMonitor", "24%", "Exploding", 2008, "Santa Barbara, CA", "$142.9M", "Private Equity", "SaaS IT monitoring platform with 2,000+ preconfigured integrations."),
(31, "Groq", "2,125%", "Exploding", 2016, "Mountain View, California", "$1B", "Series D", "High-performance AI inference hardware company; builds the Language Processing Unit (LPU) chip."),
(32, "HighSpot", "72%", "Regular", 2012, "Seattle, WA", "$644.9M", "Secondary Market", "AI-based sales enablement platform organizing content and coaching sales reps."),
(33, "Grammarly", "9%", "Regular", 2009, "San Francisco, CA", "$400M", "Private Equity", "AI-powered spelling/grammar editing software used by 30M+ people daily."),
(34, "AlphaSense", "288%", "Exploding", 2011, "New York, NY", "$1.4B", "Series F", "AI market intelligence research platform used by most of the S&P 500."),
(35, "YoDayo", "8,400%", "Exploding", 2021, "New York, New York", "$2.4M", "Seed", "Generative AI platform for anime/VTuber fans offering art generation and chatbots."),
(36, "Suno", "8,000%", "Regular", 2022, "Cambridge, Massachusetts", "$125M", "Series B", "AI music creation platform generating full songs (music, lyrics, vocals) from text prompts."),
(37, "CaseText", "2,167%", "Exploding", 2013, "San Francisco, CA", "$64.3M", "Series Unknown", "AI legal research company helping law firms find cases and draft briefs faster."),
(38, "Labelbox", "214%", "Exploding", 2018, "San Francisco, CA", "$188.9M", "Series D", "Collaborative platform for annotating and labeling training data for ML models."),
(39, "One AI", "1,025%", "Exploding", 2021, "Tel Aviv, Israel", "$8M", "Seed", "AI chatbot/virtual assistant platform for customer support automation."),
(40, "Abnormal Security", "809%", "Exploding", 2018, "San Francisco, CA", "$284M", "Series C", "B2B email security company using behavioral AI to prevent account takeovers."),
(41, "Snipfeed", "5,000%", "Regular", 2018, "Los Angeles, CA", "$8.4M", "Seed", "Link-in-bio monetization platform for creators with a GPT-powered AI Desk."),
(42, "Deepnote", "5,600%", "Regular", 2018, "San Francisco, CA", "$23.8M", "Series A", "Cloud-based collaborative data-science notebook platform with generative AI assistant."),
(43, "Luxonis", "8,800%", "Regular", 2019, "Littleton, CO", "$4.8M", "Seed", "Spatial AI and computer vision hardware company (OAK cameras, RobotHub)."),
(44, "Tabnine", "413%", "Exploding", 2013, "Tel Aviv, Israel", "$57.1M", "Series B", "Generative AI code-completion and developer assistant tool."),
(45, "FeedHive", "3,900%", "Peaked", 2021, "Zurich, Switzerland", "Bootstrapped", "Bootstrapped", "AI-powered social media marketing and content-management startup."),
(46, "Roboflow", "8,400%", "Regular", 2018, "Des Moines, IA", "$22.2M", "Series A", "Computer vision platform simplifying dataset annotation, training, and deployment."),
(47, "PhotoPrism", "7,000%", "Regular", 2022, "Berlin, Germany", "Bootstrapped", "Bootstrapped", "Privacy-friendly AI photo management app with facial recognition and object detection."),
(48, "Edge Impulse", "829%", "Exploding", 2019, "San Jose, CA", "$54.4M", "Series B", "Development platform for machine learning on edge devices with low-code tools."),
(49, "Docsumo", "7,400%", "Regular", 2018, "Singapore", "$3.5M", "Seed Round", "AI document processing platform automating data extraction from invoices and contracts."),
(50, "Perplexity AI", "7,800%", "Regular", 2022, "San Francisco, CA", "$165M", "Series Unknown", "AI-based search engine/chatbot generating answers via NLP and machine learning."),
(51, "HitPaw", "99x+", "Exploding", 2019, "Hong Kong", "Bootstrapped", "Bootstrapped", "3-in-1 AI editing software suite for video, photo, and audio editing."),
(52, "Briefly AI", "7,400%", "Regular", 2022, "Larkspur, CA", "Bootstrapped", "Bootstrapped", "AI writing assistant transcribing meetings and generating summaries via Chrome extension."),
(53, "Elicit AI", "7,500%", "Regular", 2023, "Oakland, CA", "$9M", "Seed Round", "AI research assistant that finds, summarizes, and extracts info from academic papers."),
(54, "AMP", "429%", "Exploding", 2014, "Louisville, Colorado", "$175.1M", "Series C", "Robotics/AI company sorting recyclables from waste streams via computer vision."),
(55, "Mem AI", "222%", "Exploding", 2021, "San Francisco, CA", "$29.1M", "Series A", "AI note-taking app with GPT-4-powered conversational 'Mem Chat' feature."),
(56, "Observe AI", "6,300%", "Regular", 2017, "San Francisco, CA", "$222M", "Series C", "AI contact-center conversational intelligence platform for call analysis and coaching."),
(57, "Copyleaks", "2,033%", "Exploding", 2014, "Stamford, CT", "$7.3M", "Series A", "Digital plagiarism and AI-content detection tool using NLP."),
(58, "Anthropic", "2,433%", "Exploding", 2021, "San Francisco, CA", "$9.7B", "Secondary Market", "AI safety and research company building large language models; creator of Claude."),
(59, "Peak AI", "786%", "Exploding", 2014, "Manchester, United Kingdom", "$117.7M", "Series C", "AI decision-intelligence platform for customer, inventory, and pricing applications."),
(60, "Scale AI", "700%", "Exploding", 2016, "San Francisco, CA", "$1.6B", "Series F", "Provides training data and generative AI platform for AI model development (self-driving, LLMs, robotics)."),
]

columns = ["rank", "name", "search_growth_5yr_raw", "growth_status", "year_founded",
           "location", "funding_raw", "funding_series", "description"]

df = pd.DataFrame(data, columns=columns)

# ---- Derived numeric columns (useful for EDA/modeling later) ----
def parse_growth(x):
    x = x.replace(",", "").replace("%", "").strip()
    if "x+" in x:
        return float(x.replace("x+", "")) * 100  # treat "99x+" as >=9900%
    return float(x)

def parse_funding_musd(x):
    x = x.strip()
    if x == "Bootstrapped":
        return 0.0
    x = x.replace("$", "")
    if x.endswith("B"):
        return float(x[:-1]) * 1000
    if x.endswith("M"):
        return float(x[:-1])
    return None

df["search_growth_5yr_pct_numeric"] = df["search_growth_5yr_raw"].apply(parse_growth)
df["funding_musd"] = df["funding_raw"].apply(parse_funding_musd)
df["country"] = df["location"].apply(lambda x: x.split(",")[-1].strip())
df["company_age_2024"] = 2024 - df["year_founded"]

# reorder
df = df[["rank", "name", "year_founded", "company_age_2024", "location", "country",
          "funding_raw", "funding_musd", "funding_series",
          "search_growth_5yr_raw", "search_growth_5yr_pct_numeric", "growth_status",
          "description"]]

out_path = "/mnt/user-data/outputs/ai_startups_2024.csv"
df.to_csv(out_path, index=False)
print(df.shape)
print(df.head())
print("Saved to", out_path)

# ---- Manual categorization (feature engineering — not in original PDF) ----
category_map = {
    "DeepL": "NLP/Translation", "Frame AI": "Customer Intelligence", "Uizard": "Design/UI",
    "Moveworks": "Enterprise Assistant", "Databricks": "Data/ML Platform", "Synthesia": "Video Generation",
    "Codeium": "Dev Tools", "Cohere": "LLM/Generative AI", "Soundful": "Audio/Music Generation",
    "Dialpad": "Customer Intelligence", "Yellow.AI": "Conversational AI", "PlayHT": "Voice/Speech",
    "MindsDB": "Data/ML Platform", "Shield AI": "Defense/Robotics", "Eightfold": "HR Tech",
    "Netra": "Computer Vision", "Deepgram": "Voice/Speech", "Arthur AI": "MLOps/Monitoring",
    "OpenAI": "LLM/Generative AI", "Capacity": "Conversational AI", "Read AI": "Meeting Intelligence",
    "Dataiku": "Data/ML Platform", "PhotoRoom": "Image Editing", "DNSFilter": "Cybersecurity",
    "Spot AI": "Marketing Analytics", "Interactions": "Conversational AI", "Fireflies.AI": "Meeting Intelligence",
    "Otter AI": "Meeting Intelligence", "AssemblyAI": "Voice/Speech", "LogicMonitor": "IT Ops/Monitoring",
    "Groq": "AI Hardware", "HighSpot": "Sales Enablement", "Grammarly": "Writing Assistant",
    "AlphaSense": "Market Intelligence", "YoDayo": "Generative AI/Art", "Suno": "Audio/Music Generation",
    "CaseText": "Legal Tech", "Labelbox": "Data Labeling/MLOps", "One AI": "Conversational AI",
    "Abnormal Security": "Cybersecurity", "Snipfeed": "Creator Economy", "Deepnote": "Data Science Tools",
    "Luxonis": "Computer Vision", "Tabnine": "Dev Tools", "FeedHive": "Social Media Marketing",
    "Roboflow": "Computer Vision", "PhotoPrism": "Image Editing", "Edge Impulse": "Edge ML/IoT",
    "Docsumo": "Document Processing", "Perplexity AI": "LLM/Generative AI", "HitPaw": "Image Editing",
    "Briefly AI": "Meeting Intelligence", "Elicit AI": "Research Assistant", "AMP": "Defense/Robotics",
    "Mem AI": "Productivity/Note-taking", "Observe AI": "Customer Intelligence", "Copyleaks": "Content Detection",
    "Anthropic": "LLM/Generative AI", "Peak AI": "Decision Intelligence", "Scale AI": "Data Labeling/MLOps",
}
df["category"] = df["name"].map(category_map)

out_path2 = "/mnt/user-data/outputs/ai_startups_2024.csv"
df.to_csv(out_path2, index=False)
print("Categories added. Unique categories:", df["category"].nunique())

# ---- Broader grouping for cleaner charts (fewer buckets) ----
group_map = {
    "LLM/Generative AI": "LLM/Generative AI", "Generative AI/Art": "LLM/Generative AI",
    "Voice/Speech": "Voice/Audio", "Audio/Music Generation": "Voice/Audio",
    "Meeting Intelligence": "Meeting Intelligence",
    "Conversational AI": "Conversational AI/Chatbots", "Enterprise Assistant": "Conversational AI/Chatbots",
    "Computer Vision": "Computer Vision", "Dev Tools": "Dev Tools",
    "Data/ML Platform": "Data/ML Platform", "Data Science Tools": "Data/ML Platform",
    "Cybersecurity": "Cybersecurity", "HR Tech": "HR Tech",
    "Image Editing": "Image/Video Editing", "Video Generation": "Image/Video Editing",
    "MLOps/Monitoring": "MLOps/Data Infra", "Data Labeling/MLOps": "MLOps/Data Infra",
    "Sales Enablement": "Sales/Marketing", "Marketing Analytics": "Sales/Marketing",
    "Social Media Marketing": "Sales/Marketing", "Creator Economy": "Sales/Marketing",
    "Legal Tech": "Research/Legal Tech", "Research Assistant": "Research/Legal Tech",
    "Content Detection": "Research/Legal Tech", "Market Intelligence": "Research/Legal Tech",
    "Document Processing": "Research/Legal Tech",
    "Defense/Robotics": "Defense/Robotics", "AI Hardware": "AI Hardware",
    "Writing Assistant": "Productivity/Writing", "Productivity/Note-taking": "Productivity/Writing",
    "Design/UI": "Design/UI", "Customer Intelligence": "Customer Intelligence",
    "Edge ML/IoT": "Edge ML/IoT", "NLP/Translation": "NLP/Translation", "IT Ops/Monitoring": "MLOps/Data Infra",
}
df["category_group"] = df["category"].map(group_map)
df.to_csv("/mnt/user-data/outputs/ai_startups_2024.csv", index=False)
print(df["category_group"].value_counts())
