# Execute 1.5: Move Technical Details to Methods

**Status:** 🟢 Completed  
**Priority:** HIGH  
**Estimated Time:** 60-90 minutes  
**Phase:** 1 (Critical)

---

## Objective

Reduce the detailed technical explanation in the Introduction (lines 59-84) to 2-3 sentences and move the full details to the Methods section.

---

## Reviewer Feedback

> "reduce this explanation highlighted in yellow to smaller and move these elaboration into methodology section."

**Highlighted section includes:**
- Dataset generation details (matplotlib, 43 classes, COCO format)
- Element extraction process (bounding boxes, OCR, embeddings)
- Transformer encoder details
- Advantages list (3 bullet points)

---

## Current State

**Location:** Introduction, lines 59-84

**Current Content (Too Detailed for Intro):**
```
To train and evaluate our system, we generate a large-scale synthetic dataset using
maptplotlib, covering 43 distinct chart element classes, including components from bar,
line, and area charts. For each chart, we programmatically extract bounding boxes using
the maptplotlib rendering backend, capturing pixel-accurate positions of visual elements
such as bars, titles, axes, and tick marks. Each chart is annotated in COCO-style JSON
format, ensuring compatibility with common vision datasets and workflows.

The extracted chart elements are converted into fixed-length feature vectors combining
class embeddings, OCR/text embeddings, and normalized layout information. These vectors
are projected and fed into a Transformer encoder, enabling downstream tasks like chart
retrieval, semantic similarity, and question answering.

This element-centric representation aligns with the inherent structure of charts and
offers several advantages:
- It preserves semantic and spatial relationships lost in patch-based models.
- It enables reasoning over individual elements and their roles in the chart.
- It supports generalization to downstream tasks such as chart-based question answering,
  retrieval, and summarization.
```

**Problem:** Too much implementation detail for Introduction. Should be high-level overview only.

---

## Action Items

### Step 1: Identify Content to Condense
- [ ] Dataset details → keep 1 sentence
- [ ] Element extraction → remove from intro
- [ ] Feature vectors and embeddings → remove from intro
- [ ] Advantages list → move to Methods or Results

### Step 2: Create Condensed Version for Introduction
- [ ] Draft 2-3 sentence summary covering:
  - We generate synthetic dataset with diverse chart types
  - We evaluate on element-level understanding tasks
  - Our approach shows advantages over patch-based methods
- [ ] Keep it high-level, no implementation details

**Condensed Draft:**
```
To train and evaluate our system, we generate a large-scale synthetic dataset covering
43 distinct chart element classes from multiple chart types, with COCO-style annotations.
We demonstrate that this element-centric representation enables more effective reasoning
over chart structure compared to patch-based approaches, supporting downstream tasks
such as element counting, chart retrieval, and question answering.
```

### Step 3: Prepare Detailed Content for Methods Section
- [ ] Extract full dataset generation details
- [ ] Extract element extraction process
- [ ] Extract feature vector construction
- [ ] Extract Transformer encoder details
- [ ] Keep advantages list for end of Methods or beginning of Results

**Content to Move:**
```
Dataset Generation:
- Matplotlib-based synthetic generation
- 43 element classes
- COCO-style JSON annotations
- Bounding box extraction process

Feature Engineering:
- Class embeddings
- OCR/text embeddings
- Normalized layout information
- Projection into Transformer encoder

Advantages:
- Preserves semantic and spatial relationships
- Enables element-level reasoning
- Supports downstream task generalization
```

### Step 4: Integrate into Methods Section
- [ ] Locate appropriate subsection in Methods (after model architecture)
- [ ] Add "Dataset Generation" subsection if not present
- [ ] Add "Feature Representation" subsection
- [ ] Move detailed content with proper formatting
- [ ] Ensure no duplication with existing Methods content

### Step 5: Update Introduction
- [ ] Replace lines 59-84 with condensed 2-3 sentence version
- [ ] Ensure smooth transition from our approach description
- [ ] Ensure smooth transition to next section
- [ ] Remove redundant details

### Step 6: Review Flow
- [ ] Check Introduction now focuses on motivation and high-level approach
- [ ] Check Methods now has complete implementation details
- [ ] Verify no information is lost in the move
- [ ] Ensure no duplication between sections

---

## Target Locations

**Remove from:** Introduction (lines 59-84)  
**Replace with:** 2-3 sentence high-level summary  
**Move to:** Methods section (Section 3 or 5, depending on reorganization)

---

## Dependencies

- **Related to:** 3.1 (Reorganize Sections) - Methods section structure may change
- **Coordinate with:** Data section (Section 3) - avoid duplication of dataset details

---

## Validation Checklist

- [ ] Introduction condensed to 2-3 sentences (40-60 words)
- [ ] Detailed content moved to Methods section
- [ ] No information lost in the process
- [ ] No duplication between Introduction and Methods
- [ ] Smooth transitions in both sections
- [ ] Introduction remains high-level and accessible
- [ ] Methods contains all implementation details
- [ ] Proofread both sections

---

## Before and After

### Before (Introduction - Too Detailed)
- 26 lines of technical details
- Dataset generation process
- Feature engineering specifics
- Advantages list

### After (Introduction - High-Level)
- 2-3 sentences (~50 words)
- Mentions dataset and evaluation
- High-level benefits
- No implementation details

### After (Methods - Comprehensive)
- Full dataset generation process
- Complete feature engineering pipeline
- Detailed advantages explanation
- Implementation specifics

---

## Notes

- This change makes Introduction more accessible to broader audience
- Methods section becomes the authoritative source for implementation details
- Advantages list could go in Methods (to justify design) or Results (to highlight findings)
- Consider where advantages fit best after reorganization

---

## Completion Criteria

Task is complete when:
1. ✅ Introduction condensed to 2-3 sentences
2. ✅ Detailed content moved to Methods section
3. ✅ No information lost
4. ✅ No duplication between sections
5. ✅ Smooth transitions in both locations
6. ✅ Reviewed and proofread

---

**Mark as 🟢 in PLAN_TRACKER.md when complete**
