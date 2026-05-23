"""
Central config for ooumph_official Instagram Brain
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env", override=True)

# Account
ACCOUNT_USERNAME = "ooumph_official"
ACCOUNT_USER_ID  = 12091703056
ACCOUNT_NICHE    = "OoumphCoin, Web3, crypto, blockchain lifestyle and community"

# Posting schedule (24h IST hours to post)
POSTING_HOURS    = [9, 13, 18, 21]
POSTS_PER_DAY    = 2

# Comment reply settings
REPLY_CHECK_INTERVAL = 300
REPLY_SLEEP_MIN      = 20
REPLY_SLEEP_MAX      = 50

# Evolution
EVOLUTION_AFTER_POSTS = 5

# Paths
BASE_DIR      = Path(__file__).parent.parent
MEMORY_FILE   = BASE_DIR / "brain_memory.json"
POSTED_FILE   = BASE_DIR / "posted_content.json"
REPLIED_FILE  = BASE_DIR / "replied_comments.json"
IMAGES_DIR    = BASE_DIR / "generated_images"
IMAGES_DIR.mkdir(exist_ok=True)

# API Keys
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
GROQ_KEY      = os.environ.get("GROQ_API_KEY", "")

# Content pillars — ooumph_official brand focus
CONTENT_PILLARS = [
    "OoumphCoin and Web3 community updates",
    "Crypto and blockchain lifestyle content",
    "Future of decentralized finance (DeFi)",
    "NFT culture and digital ownership",
    "Web3 entrepreneurship and innovation",
    "Motivational content for crypto builders",
    "Behind the scenes of Ooumph Networks",
    "Tech and startup culture in India",
    "Community highlights and milestones",
    "Vision for the future of Ooumph",
]

HASHTAG_POOLS = {
    "crypto":     ["#crypto", "#cryptocurrency", "#bitcoin", "#ethereum", "#web3", "#blockchain", "#defi", "#cryptoindia"],
    "ooumph":     ["#ooumph", "#ooumphcoin", "#ooumphnetworks", "#myooumph", "#ooumphofficial"],
    "web3":       ["#web3", "#web3community", "#nft", "#decentralized", "#metaverse", "#tokenomics", "#altcoin"],
    "startup":    ["#startup", "#startupindia", "#entrepreneurship", "#founder", "#buildinpublic", "#techindia"],
    "motivation": ["#motivation", "#success", "#hustle", "#grind", "#mindset", "#goals", "#vision"],
    "general":    ["#reels", "#explore", "#viral", "#trending", "#instareels", "#instagram", "#fyp"],
}
