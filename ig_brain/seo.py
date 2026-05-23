"""
SEO + AEO Optimizer — captions, hashtags, image prompts via Claude.
"""
import random
from .config import HASHTAG_POOLS, CONTENT_PILLARS, ACCOUNT_NICHE
from .memory import load_memory


def pick_hashtags(topic: str, count: int = 25) -> list:
    t = topic.lower()
    pool = []
    if any(w in t for w in ["crypto","coin","bitcoin","ethereum","token","defi","nft","blockchain"]):
        pool += HASHTAG_POOLS.get("crypto", [])
    if any(w in t for w in ["ooumph","ooumphcoin","myooumph"]):
        pool += HASHTAG_POOLS.get("ooumph", [])
    if any(w in t for w in ["web3","metaverse","decentraliz","nft","dao","wallet","altcoin"]):
        pool += HASHTAG_POOLS.get("web3", [])
    if any(w in t for w in ["startup","founder","build","entrepreneur","india","tech","launch"]):
        pool += HASHTAG_POOLS.get("startup", [])
    if any(w in t for w in ["motivat","success","hustle","grind","mindset","goal","vision","dream"]):
        pool += HASHTAG_POOLS.get("motivation", [])
    pool += HASHTAG_POOLS.get("general", [])
    seen, out = set(), []
    for tag in pool:
        if tag not in seen:
            seen.add(tag); out.append(tag)
    random.shuffle(out)
    return out[:count]


def generate_seo_caption(client, topic: str, pillar: str) -> str:
    mem      = load_memory()
    strategy = mem.get("strategy_notes", "")

    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=700,
        system=(
            "You are an expert Instagram SEO and AEO content writer for ooumph_official, "
            f"a Web3 and crypto community account for OoumphCoin. Niche: {ACCOUNT_NICHE}\n\n"
            "SEO Rules: First line = bold hook about crypto/Web3/OoumphCoin. Short punchy paragraphs.\n\n"
            "AEO Rules: Include a direct factual statement about Web3 or crypto early. "
            "Structure: Hook → Fact/Insight → Community angle → CTA.\n\n"
            "Tone: visionary crypto builder — bold, energetic, forward-thinking. "
            "Format: 150-250 words. Tasteful emojis. End with 1 engaging question. NO hashtags."
        ),
        messages=[{"role": "user", "content": (
            f"Topic: {topic}\nPillar: {pillar}\nStrategy: {strategy}\n\nWrite the Instagram caption:"
        )}]
    )
    return resp.content[0].text.strip()


def generate_image_prompt(client, topic: str) -> str:
    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=150,
        system="Write only a FLUX/Stable Diffusion image generation prompt. 2-3 sentences. No explanation.",
        messages=[{"role": "user", "content": (
            f"Topic: {topic}\n"
            "Style: futuristic, neon-lit, digital blockchain aesthetic, crypto/Web3 visual, "
            "bold colors, hyper-detailed, suitable for a crypto community Instagram account. Square 1:1. No text."
        )}]
    )
    return resp.content[0].text.strip()
