# Work Diary

## 29 September 2026

### Project Definition

- Started the financial analysis project
- **Goal:** build a portofolio project using Python and real-world financial data
- **Focus:** financial analysis, data analysis, and financial terminology

### Industry Selection

- Considered two industries:
  - Automotive
  - Luxury goods
- Selected the **luxury goods sector**
- Reason:
  - The automotive industry was already used in a previoues Silumação Empresarial project
  - The luxury sector provides an opportunity to explore a different industry

### Company Selection

Selected three companies:

- **LVMH**
- **Kering**
- **Richemont**

The companies were selected because:

- They operate in the same broad sector
- They have different business profiles
- Their differences can provide useful context when analysing their financial performance

### Analysis Period

- Defined the analysis period as **2020-2025**
- The period includes:
  - COVID-19 disruption
  - Subsequent recovery
  - Following years of financial performance

### Initial Financial Metrics

Financial data:

- Revenue
- Operating Income
- Net Income
- Total Assets
- Total Liabilities
- Shareholders' Equity

Initial indicators:

- Revenue Growth
- Operating Margin
- Net Profit Margin
- Return on Assets (ROA)
- Return on Equity (ROE)
- More advanced metrics may be added later

### Currency

- LVMH and Kering report in **EUR**
- Richemont reports in **CHF**
- Original reported currencies will be preserved
- A documented currency-conversion step may be added when a common currency is needed for comparison

### Project Language

- The project will be developed in English
- This will also be used as an opportunity to improve financial and technical English vocabulary

### Documentation

- `financial-concepts.md` will contain explanations, formulas, and notes about financial concepts
- `financial-glossary.md` will contain financial vocabulary:
  - English term
  - Portuguese translation
  - Meaning/context
  - Learning status

## 30 September 2026

### Financial Glossary

- Added `financial-glossary.md`
- Defined a colour-coded status system:
  - 🟢 Familiar
  - 🟡 Learning
  - 🔴 Review
- Added financial terms introduced in the README:
  - Revenue
  - Operating Income
  - Net Income
  - Total Assets
  - Total Liabilities
  - Shareholders' Equity
  - Revenue Growth
  - Operating Margin
  - Net Profit Margin
  - Return on Assets (ROA)
  - Return on Equity (ROE)
  - Financial Performance
  - Business Profile
  - Reporting Currency
  - Exchange Rate
  - Currency Conversion
  - Luxury Goods
  - Diversified
  - Conglomerate
- Adjusted the status of terms according to previous knowledge
- Added notes about about the distinction between `Revenue` and `Income`
- Clarified that `Revenue` is translated as **receita** in the context of this project

### Project Strucutre

- Corrected the project structure display in `README.md`
- Added `financial-glossary.md` to the documentation project structure
- Used a code block to preserve the folder and file hierarchy correctly in Markdown

### Language Learning

- Identified that much of the financial vocabulary used in the project is already recognisable
- Decided to use the project as an opportunity to consolidate technical financial English rather than learning everything from scratch

## 01 October 2026

### Data Preparation

- Started preparing the financial data collection phase
- Created a company-based structure inside the `data/` folder
- Began collecting LVMH financial reports and financial statements in PDF format
- Started reviewing the reports from **2025 backwards to 2020**

### LVMH Data

- Identified that LVMH reports financial results by business group/product category
- Examples include:
    - Wines & Spirits
    - Fashion & Leather Goods
    - Perfumes & Cosmetics
    - Watches & Jewelry
- Noted that segment-level financial information may provide an additional dimensio for the analysis

### Source Checklist

- Started organising a checklist to track the availability of the required financial information
- The checklist will be used to record:
    - Revenue
    - Operating Income
    - Net Income
    - Total Assets
    - Total Liabilities
    - Shareholders' Equity
    - Source and page reference

### Data Issue Identified

- A possible gap was identified for **2022** while reviewing the LVMH reports
- 2021 contains the expected information, so the reason for the apparente 2022 gap needs to be investigated before continuing the data collection

### Tools

- Started using LibreOffice Calc to organise the data-source checklist
- Tested an Office Viewer extension in VS Code
- The current extension may be replaced if a more reliable option is found

## 02 October 2026

### LVMH

- Located the LVMH **2022 financial report**, after initially thinking there was a gap in the available documents
-  Discovered the LVMH **Financial Calendar**, which may be useful for identifying publication dates and financial events
- Subscribed to LVMH's financial newsletter

### Financial Communication

- Subscribed to the financial newsletters of the three selected groups:
  - LVMH
  - Kering
  - Richemont
- Noted that the financial communication of large international groups is much broader than initially expected

### Kering

- Started reviewing Kering's financial documents
- Identified that some documents use **French file names** and that some reports are also available in French
- Noted that the documents are not completely uniform across years.
- 2023 documentation was not immediately located
- The 2020 documentation contains more information than some of the more recent documents reviewed so far
- Noted this as an issue to investigate rather than assuming a reason for the differences in documentation

### French Financial Vocabulary

- Identified an opportunity to use the Kering documentation to practise financial terminology in French as well as English

## 03 October 2026

### Richemont

- Completed the collection of Richemont financial documents for 2020-2026
- Noted that the 2020 and 2021 oficial PDFs were password-protected
- Located accessible copies of the financial documents through AnnualReports.com
- The financial information itself remains sourced from Richemont's published financial reports
- Noted that Richemont's financial reporting period differs from LVMH and Kering and will require careful treatment when aligning the data

### Source Collection

- Completed the initial document collection for all three companies:
  - LVMH: 2020–2025
  - Kering: 2020–2025
  - Richemont: 2020–2026

### Next Step

- Begin reviewing the financial statements and identifying the required financial data
- Map the terminology used by each company before creating the final dataset
- Record the exact source document and page for each financial figure
