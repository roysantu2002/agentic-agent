import os
from markdown_pdf import MarkdownPdf, Section

class PDFGenerator:
    def __init__(self, output_dir: str = "output"):
        """
        output_dir:
        Directory where ALL markdown and PDFs live (flat structure).
        """
        self.output_dir = output_dir
        print(f"[PDF] PDFGenerator initialized (output_dir={self.output_dir})")

    def generate_pdf(self, project_id: str) -> str:
        print(f"[PDF] Generating PDF for {project_id}")

        md_file = os.path.join(self.output_dir, f"{project_id}.md")
        pdf_file = os.path.join(self.output_dir, f"{project_id}.pdf")

        print(f"[PDF] Markdown : {md_file}")
        print(f"[PDF] PDF out  : {pdf_file}")

        if not os.path.exists(md_file):
            raise FileNotFoundError(f"[PDF] Markdown file missing: {md_file}")

        # Read markdown
        with open(md_file, "r", encoding="utf-8") as f:
            md_text = f.read()

        pdf = MarkdownPdf(toc_level=2, optimize=True)
        pdf.meta["title"] = project_id
        pdf.meta["author"] = "Your App"

        pdf.add_section(Section(md_text, toc=True))

        # Save PDF in SAME folder as MD
        pdf.save(pdf_file)

        print("[PDF] ✅ PDF created successfully")
        return pdf_file
