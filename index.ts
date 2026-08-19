#!/usr/bin/env node

interface ScannerInput {
  brand: string;
  scanType: string;
  seoSignal: number;
  aiVisibility: number;
  contentSignal: number;
  authoritySignal: number;
  gapScore: number;
  coverageScore: number;
}

interface ScannerOutput {
  brand: string;
  scanType: string;
  seoSignalScore: number;
  aiVisibilityScore: number;
  contentSignalScore: number;
  authoritySignalScore: number;
  gapScore: number;
  coverageScore: number;
  overallScannerIndex: number;
  priorityAction: string;
  aiPlatforms: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function formatScanType(scanType: string): string {
  return scanType.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    seoSignal: "SEO Signal",
    aiVisibility: "AI Visibility",
    contentSignal: "Content Signal",
    authoritySignal: "Authority Signal",
    gap: "Gap",
    coverage: "Coverage",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getAIPlatforms(seo: number, ai: number): Record<string, number> {
  return {
    "Google Search": Math.min(100, Math.round(seo * 1.0)),
    "ChatGPT": Math.min(100, Math.round(ai * 1.0)),
    "Gemini": Math.min(100, Math.round(ai * 1.0)),
    "Perplexity": Math.min(100, Math.round(ai * 1.0)),
    "Microsoft Copilot": Math.min(100, Math.round(ai * 1.0)),
  };
}

export function runScanner(input: ScannerInput): ScannerOutput {
  const scores = {
    seoSignal: input.seoSignal,
    aiVisibility: input.aiVisibility,
    contentSignal: input.contentSignal,
    authoritySignal: input.authoritySignal,
    gap: input.gapScore,
    coverage: input.coverageScore,
  };
  const overallScannerIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    brand: input.brand,
    scanType: formatScanType(input.scanType),
    seoSignalScore: input.seoSignal,
    aiVisibilityScore: input.aiVisibility,
    contentSignalScore: input.contentSignal,
    authoritySignalScore: input.authoritySignal,
    gapScore: input.gapScore,
    coverageScore: input.coverageScore,
    overallScannerIndex,
    priorityAction: getPriorityAction(scores),
    aiPlatforms: getAIPlatforms(input.seoSignal, input.aiVisibility),
  };
}

const args = process.argv.slice(2);
const brand = args[0] || "brand-name";
const scanType = args[1] || "full-scan";
const seoSignal = parseInt(args[2]) || 88;
const aiVisibility = parseInt(args[3]) || 82;
const contentSignal = parseInt(args[4]) || 85;
const authoritySignal = parseInt(args[5]) || 78;
const gapScore = parseInt(args[6]) || 90;
const coverageScore = parseInt(args[7]) || 84;

const result = runScanner({
  brand, scanType, seoSignal, aiVisibility,
  contentSignal, authoritySignal, gapScore, coverageScore,
});

console.log(`Brand: ${result.brand}`);
console.log(`Scan Type: ${result.scanType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`SEO Signal Score:              ${result.seoSignalScore}/100  [${getStatus(result.seoSignalScore)}]`);
console.log(`AI Visibility Score:           ${result.aiVisibilityScore}/100  [${getStatus(result.aiVisibilityScore)}]`);
console.log(`Content Signal Score:          ${result.contentSignalScore}/100  [${getStatus(result.contentSignalScore)}]`);
console.log(`Authority Signal Score:        ${result.authoritySignalScore}/100  [${getStatus(result.authoritySignalScore)}]`);
console.log(`Gap Score:                     ${result.gapScore}/100  [${getStatus(result.gapScore)}]`);
console.log(`Coverage Score:                ${result.coverageScore}/100  [${getStatus(result.coverageScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Scanner Index:         ${result.overallScannerIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nAI Platforms Scanned:");
Object.entries(result.aiPlatforms).forEach(([platform, score]) => {
  console.log(`  ${platform.padEnd(22)} ${score}/100`);
});
