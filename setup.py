from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="seo-ai-visibility-scanner",
    version="1.0.0",
    author="GetPR.Buzz",
    author_email="info@getpr.buzz",
    description="SEO AI Visibility Scanner evaluates a brand's visibility across both traditional search engines and AI-powered discovery platforms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://getpr.buzz",
    project_urls={
        "Homepage": "https://getpr.buzz",
        "GitHub": "https://github.com/getpr-buzz/seo-ai-visibility-scanner",
        "Documentation": "https://seo-ai-visibility-scanner.readthedocs.io",
        "PyPI": "https://pypi.org/project/seo-ai-visibility-scanner",
    },
    py_modules=["seo_ai_scanner"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
    ],
    keywords=[
        "seo-ai-visibility-scanner",
        "seo-scanning",
        "ai-visibility",
        "brand-visibility",
        "search-gap-analysis",
        "ai-search",
        "content-signals",
        "authority-signals",
        "getpr-buzz",
    ],
    entry_points={
        "console_scripts": [
            "seo-ai-scan=seo_ai_scanner:main",
        ],
    },
)
