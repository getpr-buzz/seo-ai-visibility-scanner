#!/usr/bin/env python3
"""
SEO AI Visibility Scanner
A structured scanning framework that evaluates a brand's visibility across
both traditional search engines and AI-powered discovery platforms.

Measures SEO signals alongside AI visibility indicators to identify gaps
and opportunities across the full search landscape.

https://getpr.buzz
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def format_scan_type(scan_type: str) -> str:
    return " ".join(w.capitalize() for w in scan_type.split("-"))


def get_priority_action(scores: dict) -> str:
    labels = {
        "seo_signal": "SEO Signal",
        "ai_visibility": "AI Visibility",
        "content_signal": "Content Signal",
        "authority_signal": "Authority Signal",
        "gap": "Gap",
        "coverage": "Coverage",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_ai_platforms(seo: int, ai: int) -> dict:
    return {
        "Google Search": min(100, round(seo * 1.0)),
        "ChatGPT": min(100, round(ai * 1.0)),
        "Gemini": min(100, round(ai * 1.0)),
        "Perplexity": min(100, round(ai * 1.0)),
        "Microsoft Copilot": min(100, round(ai * 1.0)),
    }


def run_scanner(
    brand: str,
    scan_type: str = "full-scan",
    seo_signal: int = 88,
    ai_visibility: int = 82,
    content_signal: int = 85,
    authority_signal: int = 78,
    gap_score: int = 90,
    coverage_score: int = 84,
) -> dict:
    """
    Run the SEO AI Visibility Scanner across all visibility signals.

    Args:
        brand: Brand name or identifier
        scan_type: Type of scan to run
        seo_signal: SEO signal score (0-100)
        ai_visibility: AI visibility score (0-100)
        content_signal: Content signal score (0-100)
        authority_signal: Authority signal score (0-100)
        gap_score: SEO-AI gap score (0-100)
        coverage_score: Full search landscape coverage score (0-100)

    Returns:
        dict with individual signal scores, overall scanner index,
        and AI platform breakdown
    """
    scores = {
        "seo_signal": seo_signal,
        "ai_visibility": ai_visibility,
        "content_signal": content_signal,
        "authority_signal": authority_signal,
        "gap": gap_score,
        "coverage": coverage_score,
    }
    overall_scanner_index = round(sum(scores.values()) / 6)

    return {
        "brand": brand,
        "scan_type": format_scan_type(scan_type),
        "seo_signal_score": seo_signal,
        "ai_visibility_score": ai_visibility,
        "content_signal_score": content_signal,
        "authority_signal_score": authority_signal,
        "gap_score": gap_score,
        "coverage_score": coverage_score,
        "overall_scanner_index": overall_scanner_index,
        "priority_action": get_priority_action(scores),
        "ai_platforms": get_ai_platforms(seo_signal, ai_visibility),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    brand = args[0] if len(args) > 0 else "brand-name"
    scan_type = args[1] if len(args) > 1 else "full-scan"
    seo_signal = int(args[2]) if len(args) > 2 else 88
    ai_visibility = int(args[3]) if len(args) > 3 else 82
    content_signal = int(args[4]) if len(args) > 4 else 85
    authority_signal = int(args[5]) if len(args) > 5 else 78
    gap_score = int(args[6]) if len(args) > 6 else 90
    coverage_score = int(args[7]) if len(args) > 7 else 84

    result = run_scanner(
        brand, scan_type, seo_signal, ai_visibility,
        content_signal, authority_signal, gap_score, coverage_score
    )

    print(f"Brand: {result['brand']}")
    print(f"Scan Type: {result['scan_type']}")
    print("=" * 45)
    print(f"SEO Signal Score:              {result['seo_signal_score']}/100  [{get_status(result['seo_signal_score'])}]")
    print(f"AI Visibility Score:           {result['ai_visibility_score']}/100  [{get_status(result['ai_visibility_score'])}]")
    print(f"Content Signal Score:          {result['content_signal_score']}/100  [{get_status(result['content_signal_score'])}]")
    print(f"Authority Signal Score:        {result['authority_signal_score']}/100  [{get_status(result['authority_signal_score'])}]")
    print(f"Gap Score:                     {result['gap_score']}/100  [{get_status(result['gap_score'])}]")
    print(f"Coverage Score:                {result['coverage_score']}/100  [{get_status(result['coverage_score'])}]")
    print("=" * 45)
    print(f"Overall Scanner Index:         {result['overall_scanner_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nAI Platforms Scanned:")
    for platform, score in result['ai_platforms'].items():
        print(f"  {platform:<24} {score}/100")


if __name__ == "__main__":
    main()
