# Paper Improvement Plan
## Chart-Aware Transformers: Learning Structured Embeddings for BI Report Understanding

---

## Overview
This document outlines a structured plan to address reviewer feedback and improve the paper for arXiv submission.

---

## Section 1: Introduction Restructuring

### 1.1 Add Application Context (HIGH PRIORITY)
**Feedback:** "Give atleast one paragraph about Application. directly jumping into our idea may not give weight."

**Action Items:**
- [ ] Add opening paragraph describing real-world applications of chart understanding
- [ ] Include use cases: business intelligence dashboards, automated report generation, data accessibility
- [ ] Mention industry pain points (e.g., manual chart interpretation, accessibility for visually impaired)
- [ ] Cite 1-2 application-focused papers

**Target Location:** Before current Introduction paragraph 1

---

### 1.2 Strengthen Literature Context in Introduction
**Feedback:** "So it would be better to give little bit introduction and atleast one or two existing papers on how they addressed and achieved, issues."

**Action Items:**
- [ ] Add 1 paragraph summarizing how existing approaches (ViT, patch-based models) handle charts
- [ ] Briefly mention their limitations with citations
- [ ] Create smooth transition to "our approach addresses these gaps"
- [ ] Reference papers: UniChart, ChartAssistant, LayoutLMv3

**Target Location:** After application paragraph, before methodology description

---

### 1.3 Add Evidence for Model Limitations
**Feedback:** "proof like reference papers if any to state why the models lack."

**Action Items:**
- [ ] Add citations showing ViT struggles with structured documents
- [ ] Reference papers demonstrating patch-based limitations for charts
- [ ] Include quantitative evidence if available (e.g., "ViT achieves only X% on chart QA tasks")
- [ ] Suggested papers: Li et al. 2024, Huang et al. 2024 (already in references)

**Target Location:** Paragraph discussing ViT limitations (lines 39-44)

---

### 1.4 Refine Architecture Description
**Feedback:** "change as a novel architecture that explicitly models chart elements as tokens instead of blind chunking tokenize. add reference."

**Action Items:**
- [ ] Rewrite line 45-46 with stronger language: "novel architecture that explicitly models chart elements as tokens"
- [ ] Add contrast: "instead of blind patch-based tokenization"
- [ ] Add reference to patch-based tokenization (ViT paper: Dosovitskiy et al. 2020)

**Target Location:** Lines 45-46

---

### 1.5 Move Technical Details to Methods
**Feedback:** "reduce this explanation highlighted in yellow to smaller and move these elaboration into methodology section."

**Action Items:**
- [ ] Reduce lines 59-84 (dataset generation, element extraction, advantages) to 2-3 sentences
- [ ] Keep only: "We generate synthetic dataset with 43 element classes and evaluate on element counting tasks"
- [ ] Move detailed explanation to Methods section (Section 5)
- [ ] Move advantages list to end of Methods or beginning of Results

**Target Location:** Lines 59-84 → condense and relocate

---

## Section 2: Prior Literature Enhancement

### 2.1 Integrate Literature into Introduction
**Feedback:** "Beautiful survey, put a few in introduction part so that readers if they start they get positive opinion."

**Action Items:**
- [ ] Select 2-3 most relevant papers from Prior Literature section
- [ ] Add brief mentions in Introduction (1-2 sentences each)
- [ ] Keep full Prior Literature section but ensure no redundancy
- [ ] Papers to highlight: UniChart, ChartAssistant, LayoutLMv3

**Target Location:** Introduction section (new paragraph after application context)

---

## Section 3: Paper Structure Reorganization

### 3.1 Reorder Sections
**Feedback:** "If we directly jump to data, it will get confused, so first introduce methodology and then data, experiments."

**Current Order:**
1. Introduction
2. Prior Literature
3. Data
4. Model
5. Methods
6. Results
7. Analysis
8. Conclusion

**New Order:**
- [ ] 1. Introduction (enhanced)
- [ ] 2. Prior Literature
- [ ] 3. **Methods** (consolidate Model + Methods sections)
- [ ] 4. **Data** (move after Methods)
- [ ] 5. **Experiments** (new section: setup, baselines, metrics)
- [ ] 6. Results
- [ ] 7. Analysis
- [ ] 8. Conclusion

**Action Items:**
- [ ] Merge Section 4 (Model) and Section 5 (Methods) into single "Methods" section
- [ ] Move Data section after Methods
- [ ] Create new "Experiments" section describing setup before Results

---

## Section 4: Results Enhancement

### 4.1 Add Comparative Results Table
**Feedback:** "if would good if we put ViT performance as well. instead of simply telling chart transformer performance. Tabulation will be good."

**Action Items:**
- [ ] Create comparison table with columns: Model | Accuracy | Parameters | Training Time
- [ ] Include rows for:
  - Vision Transformer (ViT)
  - Chart Transformer (Ours)
- [ ] Add ViT baseline accuracy (currently missing specific number)
- [ ] Consider adding: precision, recall, F1 if available
- [ ] Add table caption explaining the task and dataset

**Target Location:** Section 6 (Results), replace lines 204-236

**Example Table Format:**
```
| Model              | Accuracy | Params | Notes                    |
|--------------------|----------|--------|--------------------------|
| ViT (baseline)     | XX%      | XXM    | Patch-based tokenization |
| Chart Transformer  | 92%      | XXM    | Element-based (ours)     |
```

---

## Section 5: Writing Quality Improvements

### 5.1 Fix Typos and Inconsistencies
**Action Items:**
- [ ] Line 60: "maptplotlib" → "matplotlib" (appears twice)
- [ ] Ensure consistent terminology: "Chart Transformer" vs "Chart-Aware Transformer"
- [ ] Check all section numbering (currently has duplicate "5" and "6")
- [ ] Proofread for grammar and clarity

---

## Section 6: Additional Enhancements (Optional but Recommended)

### 6.1 Add Figures
**Action Items:**
- [ ] Figure 1: Architecture diagram showing element tokenization pipeline
- [ ] Figure 2: Example chart with annotated elements
- [ ] Figure 3: Comparison of patch-based vs element-based tokenization
- [ ] Figure 4: Results visualization (accuracy comparison bar chart)

### 6.2 Expand Experiments
**Action Items:**
- [ ] Add ablation study: impact of class embeddings, bbox embeddings, area features
- [ ] Test on multiple chart types (currently focuses on bar charts)
- [ ] Include error analysis: where does the model fail?

### 6.3 Strengthen Conclusion
**Action Items:**
- [ ] Summarize key contributions more clearly
- [ ] Quantify improvements over baseline
- [ ] Make future work more specific and actionable

---

## Implementation Checklist

### Phase 1: Critical Changes (Must Do)
- [ ] 1.1: Add application paragraph to Introduction
- [ ] 1.2: Add literature context to Introduction
- [ ] 1.5: Move technical details from Introduction to Methods
- [ ] 3.1: Reorganize section order (Methods before Data)
- [ ] 4.1: Create results comparison table

### Phase 2: Important Changes (Should Do)
- [ ] 1.3: Add citations for model limitations
- [ ] 1.4: Refine architecture description
- [ ] 2.1: Integrate key literature into Introduction
- [ ] 5.1: Fix typos and inconsistencies

### Phase 3: Enhancement Changes (Nice to Have)
- [ ] 6.1: Add figures and diagrams
- [ ] 6.2: Expand experiments with ablations
- [ ] 6.3: Strengthen conclusion

---

## Timeline Estimate

- **Phase 1 (Critical):** 4-6 hours
- **Phase 2 (Important):** 2-3 hours
- **Phase 3 (Enhancement):** 4-8 hours (if adding figures/experiments)

**Total:** 10-17 hours for comprehensive revision

---

## Notes

- Keep the paper within page limits (check conference/journal requirements)
- Ensure all new citations are properly formatted
- Run spell check and grammar check before final submission
- Consider having a colleague review the revised version
- Update abstract if major changes are made to Introduction

---

## Reviewer Feedback Summary

**Strengths Noted:**
- "Beautiful survey" (Prior Literature section)
- Strong technical approach with element-based tokenization

**Main Concerns:**
1. Introduction lacks application context and literature integration
2. Too much technical detail in Introduction (should be in Methods)
3. Section ordering is confusing (Data before Methods)
4. Results lack comparative table with baseline performance
5. Missing citations for claims about model limitations

**Overall Assessment:** Paper has strong technical content but needs structural reorganization and better contextualization for broader audience.
