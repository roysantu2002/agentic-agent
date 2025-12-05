# install required library
# pip install markdown-pdf

import os
from markdown_pdf import MarkdownPdf, Section

class PDFGenerator:
    def __init__(self):
        print("[PDF] PDFGenerator initialized")

    def generate_pdf(self, project_id: str) -> str:
        print(f"[PDF] Generating PDF for {project_id}")
        project_path = os.path.join("project_output", project_id)
        md_file = os.path.join(project_path, f"{project_id}.md")
        pdf_file = os.path.join(project_path, f"{project_id}.pdf")

        if not os.path.exists(md_file):
            raise FileNotFoundError(f"[PDF] Markdown file missing: {md_file}")

        # Read markdown
        with open(md_file, "r", encoding="utf‑8") as f:
            md_text = f.read()

        print(f"[PDF] Using markdown-pdf to convert {md_file} → {pdf_file}")
        pdf = MarkdownPdf(toc_level=2, optimize=True)
        pdf.meta["title"] = project_id
        pdf.meta["author"] = "Your App"

        # Add the markdown section
        pdf.add_section(Section(md_text, toc=True))

        # Save PDF
        pdf.save(pdf_file)

        print("[PDF] ✅ PDF created successfully")
        return pdf_file
