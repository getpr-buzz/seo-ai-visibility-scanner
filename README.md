# SEO AI Visibility Scanner 🔍🤖

[![npm](https://img.shields.io/npm/v/@getpr-buzz/seo-ai-visibility-scanner)](https://npmjs.com/package/@getpr-buzz/seo-ai-visibility-scanner)
[![PyPI](https://img.shields.io/pypi/v/seo-ai-visibility-scanner)](https://pypi.org/project/seo-ai-visibility-scanner)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22009341.svg)](https://doi.org/10.5281/zenodo.22009341)

SEO AI Visibility Scanner is a structured scanning framework that evaluates a brand's visibility across both traditional search engines and AI-powered discovery platforms. It measures SEO signals alongside AI visibility indicators to identify gaps and opportunities across the full search landscape. Built by [GetPR.Buzz](https://getpr.buzz).

## Overview

As search evolves from keyword-based results to AI-generated answers and recommendations, brands need visibility across both traditional search and AI-driven discovery. The SEO AI Visibility Scanner evaluates both layers — providing a unified score that reflects the complete modern search landscape.

## Key Capabilities

- **Traditional SEO Scanning** — Evaluate keyword rankings, organic traffic signals, on-page SEO, and technical performance
- **AI Visibility Scanning** — Measure brand recognition across ChatGPT, Gemini, Perplexity, and Copilot
- **Gap Analysis** — Identify the gap between SEO strength and AI visibility
- **Content Signal Scanning** — Assess how well content communicates brand expertise to AI systems
- **Authority Signal Scanning** — Measure digital PR, backlinks, and authoritative brand mentions
- **Unified Visibility Score** — Combined SEO + AI visibility scoring in one unified index

## Scan Types

| Scan | Description |
|------|-------------|
| seo-scan | Traditional search engine visibility and ranking signals |
| ai-scan | AI platform visibility across ChatGPT, Gemini, Perplexity, Copilot |
| content-scan | Content quality and brand expertise signals |
| authority-scan | Digital PR, backlinks, and authoritative mentions |
| gap-scan | Identify the gap between SEO strength and AI visibility |
| full-scan | Complete SEO + AI visibility scan across all signals |

## Features

- SEO Signal Score — evaluates traditional search engine visibility and ranking strength
- AI Visibility Score — measures brand recognition across AI search platforms
- Content Signal Score — assesses content quality and brand expertise signals
- Authority Signal Score — tracks digital PR and authoritative brand mentions
- Gap Score — quantifies the gap between SEO and AI visibility
- Coverage Score — measures how completely the full search landscape is covered
- CLI support in Node.js and Python
- Benchmark dataset included (20 scanner cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @getpr-buzz/seo-ai-visibility-scanner
npx seo-ai-scan "brand-name" full-scan 88 82 85 78 90 84
```

### Python

```bash
pip install seo-ai-visibility-scanner
python -m seo_ai_scanner "brand-name" full-scan 88 82 85 78 90 84
```

## Output

```
Brand: brand-name
Scan Type: Full Scan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEO Signal Score:              88 / 100  [Excellent]
AI Visibility Score:           82 / 100  [Healthy]
Content Signal Score:          85 / 100  [Excellent]
Authority Signal Score:        78 / 100  [Healthy]
Gap Score:                     90 / 100  [Excellent]
Coverage Score:                84 / 100  [Excellent]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Scanner Index:         85 / 100
Priority Action:               Authority Signal (lowest — act first)

AI Platforms Scanned:
  Google Search:           88 / 100
  ChatGPT:                 82 / 100
  Gemini:                  82 / 100
  Perplexity:              82 / 100
  Microsoft Copilot:       82 / 100
```

## AI Platforms Covered

| Platform | Coverage |
|----------|---------|
| Google Search | Organic, Local, AI Overviews |
| ChatGPT | Brand and content mention scanning |
| Gemini | Google AI search visibility |
| Perplexity | AI answer engine brand presence |
| Microsoft Copilot | Bing-powered AI search visibility |

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate visibility intervention required |
| 31–60 | At Risk | Significant improvements needed |
| 61–80 | Healthy | On track — optimise and expand |
| 81–100 | Excellent | Strong visibility — scale strategy |

## Keywords

SEO AI Visibility Scanner · SEO Scanning · AI Visibility · Brand Visibility · Search Gap Analysis · AI Search · Content Signals · Authority Signals · GetPR.Buzz

## Links

| Platform | URL |
|----------|-----|
| Website | https://getpr.buzz |
| GitHub | https://github.com/getpr-buzz/seo-ai-visibility-scanner |
| GitHub Pages | https://getpr-buzz.github.io/seo-ai-visibility-scanner/ |
| NPM | https://npmjs.com/package/@getpr-buzz/seo-ai-visibility-scanner |
| PyPI | https://pypi.org/project/seo-ai-visibility-scanner |
| Hugging Face | https://huggingface.co/datasets/getpr-buzz/seo-ai-scanner-benchmarks |
| Kaggle | https://www.kaggle.com/datasets/getprbuzz/seo-ai-scanner-benchmarks |
| Zenodo | https://zenodo.org/records/22009341 |
| Docs | https://seo-ai-visibility-scanner.readthedocs.io |
| SlideShare | https://www.slideshare.net/slideshow/get-pr-buzz-building-brand-visibility-and-authority-in-the-ai-first-digital-era/289334371 |
| Quora | https://www.quora.com/profile/GetPR |

## About GetPR.Buzz

GetPR.Buzz bridges SEO and AI visibility — helping brands evolve from keyword rankings into a broader brand-visibility strategy recognised across traditional search and AI-powered discovery platforms.

## License

MIT — [GetPR.Buzz](https://getpr.buzz)
