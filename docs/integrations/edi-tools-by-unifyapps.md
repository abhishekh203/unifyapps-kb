# EDI Tools by UnifyApps

Source: https://www.unifyapps.com/docs/unify-integrations/edi-tools-by-unifyapps
Section: integrations

---

Electronic Data Interchange (EDI) encompasses a range of standards and protocols designed for exchanging business documents in B2B environments. Although considered older technology compared to modern options like RESTful APIs, it remains widely adopted in commercial trade and various applications.

EDI Tools by UnifyApps supports the following standards:

- EDIFACT
- X12

## How to Use EDI Tools by UnifyApps

You can access the EDI tools by UnifyApps directly from the automation builder.

1. Select the EDI tools app: In the actions application selector, choose EDI tools by UnifyApps.
2. Choose your action: Select the desired action—Generate EDI to create an EDI file or Parse EDI to read an EDI file.
3. Configure the action: Set up the action parameters as needed.

## Generate EDI action

The generated EDI action allows you to create an EDI document.

- **EDI standard:** Define the EDI standard for your document. Options include EDIFACT, and X12.
- **Setup via EDI sample:** Decide if you want to generate a document based on an EDI transaction type or by using a sample file.
- **Sample EDI document:** Provide a sample EDI document to generate a JSON template. This is for design-time use only and should not be mapped to datapills.
- **Release:** Select the appropriate release version to ensure compatibility with your trading partners and the correct data processing.
- **Transaction Set:** Select the correct transaction set for your document to ensure it conforms to the required structure and meets your business requirements.
- **Data Element Separator:** Define the character used to separate individual data elements within a segment in the EDI document. This ensures correct parsing and structure.
- **Segment Terminator:** Specify the character that marks the end of each segment in the EDI document. This helps distinguish individual segments during processing.
- **Composite Data Element Separator:** Set the character used to separate composite data elements within a segment. This is essential for correctly handling composite structures in the EDI file.
- **Escape Character:** Provide the character used to escape special characters within the EDI document. This prevents misinterpretation of characters that have a functional purpose.
- **Repetition Separator:** Specify the character used to separate repeated elements within a segment. This allows for handling multiple occurrences of the same data element.

## Parse EDI action

The Parse EDI action enables you to convert EDI documents into UnifyApps datapills.

To use this action, select the EDI standard, provide a sample document, and supply the EDI content to parse. The sample document is crucial for UnifyApps to generate the schema, which is later used to configure the downstream actions in the recipe.

- **EDI standard:** Define the EDI standard for your document. Options include EDIFACT, and X12.
- **Setup via EDI sample:** Decide if you want to generate a document based on an EDI transaction type or by using a sample file.
- **EDI document:** Enter the source document to be parsed
- **Sample EDI document:** Provide a sample EDI document to generate a JSON template. This is for design-time use only and should not be mapped to datapills.
- **Release:** Select the appropriate release version to ensure compatibility with your trading partners and the correct data processing.
- **Transaction Set:** Select the correct transaction set for your document to ensure it conforms to the required structure and meets your business requirements.
- **Data Element Separator:** Define the character used to separate individual data elements within a segment in the EDI document. This ensures correct parsing and structure.
- **Segment Terminator:** Specify the character that marks the end of each segment in the EDI document. This helps distinguish individual segments during processing.
- **Composite Data Element Separator:** Set the character used to separate composite data elements within a segment. This is essential for correctly handling composite structures in the EDI file.
- **Escape Character:** Provide the character used to escape special characters within the EDI document. This prevents misinterpretation of characters that have a functional purpose.
- **Repetition Separator:** Specify the character used to separate repeated elements within a segment. This allows for handling multiple occurrences of the same data element.
