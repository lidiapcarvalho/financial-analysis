# Financial Concepts

## Data Methodology

### Financial Statements

- The analysis uses **consolidated financial statements** for LVMH, Kering and Richemont.
- Consolidated statements are used to ensure that the three companies are compared at group level.
- Separate financial statements of individual parent companies are not used.

### Net Income

For comparability, `Net Income` represents the profit attributable to the owners/shareholders of the group:

- **LVMH:** Net profit, Group share
- **Kering:** Net income attributable to the Group
- **Richemont:** Profit attributable to owners of the parent company

Profit attributable to non-controlling interests is not included in the `Net Income` dataset value.

### Currency and Scale

- Financial figures are recorded using the **reporting currency presented in the source financial statements**.
- No currency conversion is performed when the source already presents the figures in the currency used for the dataset.
- The scale used in the source is preserved (for example, EUR millions).
- Financial values are stored as numeric values in the spreadsheet to allow calculations and later processing in Python.

### Fiscal Year

- The fiscal year and period-end date are recorded separately.
- This is particularly important for **Richemont**, whose financial year ends in March rather than December.

### Comparative Figures

- Financial statements ofthen include comparative figures for the previous year.
- There figures may differ from those originally published for the previous year because of **restatements, reclassifications or changes in presentation**.
- When a difference is identified, the original financial statement for that fiscal year is checked before the value is included in the dataset.

### Reporting Terminology

Different companies may use different terminology for economically equivalent financial comcepts. The original terminology is preserved in the source documentation, while the dataset uses standardized column names to make the companies comparable.
