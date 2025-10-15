# Execute 3.1: Reorganize Section Order

**Status:** 🟢 Completed  
**Priority:** HIGH  
**Estimated Time:** 90-120 minutes  
**Phase:** 1 (Critical)

---

## Objective

Reorganize paper sections to follow a more logical flow: Methods before Data, and consolidate Model + Methods sections.

---

## Reviewer Feedback

> "If we directly jump to data, it will get confused, so first introduce methodology and then data, experiments."

---

## Current Structure (Problematic)

```
1. Introduction
2. Prior Literature
3. Data                    ← Appears before methodology
4. Model                   ← Separate from Methods
5. Methods                 ← Should come earlier
6. Results                 ← No explicit Experiments section
7. Analysis
8. Conclusion
9. Known Project Limitations
```

**Problems:**
- Data appears before readers understand the approach
- Model and Methods are separate (should be unified)
- No clear Experiments section describing setup
- Confusing flow for readers

---

## Target Structure (Improved)

```
1. Introduction
2. Prior Literature
3. Methods                 ← Merged Model + Methods, moved up
   3.1 Architecture
   3.2 Feature Representation
   3.3 Training Objective
4. Data                    ← Moved after Methods
   4.1 Synthetic Dataset Generation
   4.2 Annotation Format
   4.3 Dataset Statistics
5. Experiments             ← New section
   5.1 Experimental Setup
   5.2 Baselines
   5.3 Evaluation Metrics
6. Results
7. Analysis
8. Conclusion
9. Known Project Limitations
```

---

## Action Items

### Step 1: Backup Current Version
- [ ] Create backup copy of LaTeX file
- [ ] Name: `cs224u-experiment-protocol_backup_[date].tex`
- [ ] Verify backup is complete

### Step 2: Plan Section Consolidation

#### Merge Model (Section 4) + Methods (Section 5)
- [ ] Review current Model section (lines 142-189):
  - Embedding Layer
  - Transformer Encoder
  - Classification Head
  - Loss Function
- [ ] Review current Methods section (lines 213-231):
  - Chart Transformer description
  - Baseline description
  - Evaluation approach
- [ ] Plan unified Methods structure:
  - 3.1 Architecture (from Model section)
  - 3.2 Feature Representation (from Model + 1.5 content)
  - 3.3 Training Objective (from Model section)
  - 3.4 Baseline Models (from Methods section)

### Step 3: Create New Experiments Section

**Content to include:**
- [ ] Experimental setup (hardware, hyperparameters)
- [ ] Baseline description (ViT details)
- [ ] Evaluation metrics (accuracy, why chosen)
- [ ] Dataset split (train/val/test)
- [ ] Training procedure

**Draft Experiments Section:**
```
5. Experiments

5.1 Experimental Setup
- Hardware: [specify]
- Hyperparameters: [learning rate, batch size, epochs, etc.]
- Optimizer: [Adam, SGD, etc.]
- Training time: [duration]

5.2 Baselines
- Vision Transformer (ViT): [architecture details, pretrained weights]
- Configuration: [patch size, model size]
- Adaptation: [how ViT was adapted for this task]

5.3 Evaluation Metrics
- Primary metric: Accuracy (classification task)
- Justification: [why accuracy is appropriate]
- Additional metrics: [if any - precision, recall, F1]

5.4 Dataset Split
- Training: X charts
- Validation: Y charts
- Test: Z charts
- Split strategy: [random, stratified, etc.]
```

### Step 4: Reorganize Sections in LaTeX

- [ ] **Step 4a:** Copy Section 4 (Model) content
- [ ] **Step 4b:** Copy Section 5 (Methods) content
- [ ] **Step 4c:** Create new unified Section 3 (Methods)
- [ ] **Step 4d:** Paste and merge Model + Methods content
- [ ] **Step 4e:** Rename old Section 3 (Data) to Section 4
- [ ] **Step 4f:** Create new Section 5 (Experiments)
- [ ] **Step 4g:** Extract experimental details from Results/Methods
- [ ] **Step 4h:** Update all section numbers and references
- [ ] **Step 4i:** Update table of contents if present

### Step 5: Update Section Content

#### New Section 3: Methods
- [ ] Add subsection headers (3.1, 3.2, 3.3, 3.4)
- [ ] Integrate content from 1.5 (technical details from Introduction)
- [ ] Ensure logical flow within section
- [ ] Add transitions between subsections

#### New Section 4: Data
- [ ] Keep existing content
- [ ] Ensure it references Methods section appropriately
- [ ] Update any forward references

#### New Section 5: Experiments
- [ ] Write experimental setup details
- [ ] Describe baselines thoroughly
- [ ] Explain evaluation metrics
- [ ] Document dataset splits

### Step 6: Update Cross-References
- [ ] Find all `\ref{}` commands referencing sections
- [ ] Update section numbers in text (e.g., "In Section 3" → "In Section 4")
- [ ] Update figure/table references if affected
- [ ] Check "as described in Section X" references

### Step 7: Update Section Headers
- [ ] Ensure consistent formatting
- [ ] Update section numbering
- [ ] Verify subsection numbering
- [ ] Check LaTeX labels (`\label{sec:...}`)

### Step 8: Review Transitions
- [ ] Introduction → Prior Literature (unchanged)
- [ ] Prior Literature → Methods (update transition)
- [ ] Methods → Data (add transition explaining "now that we've described approach, here's our data")
- [ ] Data → Experiments (add transition)
- [ ] Experiments → Results (update transition)

### Step 9: Compile and Check
- [ ] Compile LaTeX document
- [ ] Fix any compilation errors
- [ ] Check PDF output for correct section order
- [ ] Verify all cross-references work
- [ ] Check table of contents

### Step 10: Final Review
- [ ] Read through entire paper with new structure
- [ ] Ensure logical flow
- [ ] Check for orphaned content
- [ ] Verify no duplication
- [ ] Proofread transitions

---

## Section Mapping

| Old Section | New Section | Action |
|-------------|-------------|--------|
| 1. Introduction | 1. Introduction | Keep |
| 2. Prior Literature | 2. Prior Literature | Keep |
| 3. Data | 4. Data | Move down |
| 4. Model | 3. Methods (3.1-3.3) | Merge & move up |
| 5. Methods | 3. Methods (3.4) | Merge into 3 |
| - | 5. Experiments | Create new |
| 6. Results | 6. Results | Keep (renumber) |
| 7. Analysis | 7. Analysis | Keep (renumber) |
| 8. Conclusion | 8. Conclusion | Keep (renumber) |
| 9. Limitations | 9. Limitations | Keep (renumber) |

---

## Dependencies

- **Coordinate with:** 1.5 (Move Details) - content goes into new Methods section
- **Impacts:** All execution plans referencing section numbers
- **Update:** IMPROVEMENT_PLAN.md with new section numbers

---

## Validation Checklist

- [ ] Backup created
- [ ] Sections reordered: Methods before Data
- [ ] Model + Methods merged into single Methods section
- [ ] New Experiments section created
- [ ] All section numbers updated
- [ ] All cross-references updated
- [ ] LaTeX compiles without errors
- [ ] PDF shows correct section order
- [ ] Transitions between sections are smooth
- [ ] No content lost or duplicated
- [ ] Table of contents correct (if present)

---

## Common Pitfalls to Avoid

- ❌ Forgetting to update `\ref{}` commands
- ❌ Breaking figure/table references
- ❌ Losing content during copy-paste
- ❌ Inconsistent subsection numbering
- ❌ Broken LaTeX labels
- ❌ Awkward transitions between sections

---

## Notes

- This is a major structural change - take time to do it carefully
- Test compile frequently to catch errors early
- Keep backup file until confident new structure works
- Update PLAN_TRACKER.md section references after completion
- This change improves paper flow significantly

---

## Completion Criteria

Task is complete when:
1. ✅ Sections reordered: Methods (3) → Data (4) → Experiments (5)
2. ✅ Model + Methods merged into unified Methods section
3. ✅ New Experiments section created with complete content
4. ✅ All section numbers and cross-references updated
5. ✅ LaTeX compiles successfully
6. ✅ PDF shows correct structure
7. ✅ Smooth transitions between all sections
8. ✅ Reviewed and proofread

---

**Mark as 🟢 in PLAN_TRACKER.md when complete**
