# tests/test_pdf_generator_keep_artifacts.py
import os
from util.pdf_generator import PDFGenerator

def main():
    print(">>> Starting PDF generation test (artifacts will be kept)...")
    project_id = "spiritual_growth_consciousness_development_course_blueprint_and_content_guide"
    project_path = os.path.join("output", project_id)
    print(f"[TEST] project_path: {project_path}")
    md_file = os.path.join(project_path, f"{project_id}.md")
    pdf_file = os.path.join(project_path, f"{project_id}.pdf")

    print(f"[TEST] project_path: {project_path}")
    print(f"[TEST] markdown path: {md_file}")
    print(f"[TEST] expected pdf path: {pdf_file}")

    # # ✅ safer condition
    # if not os.path.exists(md_file):
    #     print("[TEST] Markdown missing — creating isolated fallback example.")
    #     os.makedirs(project_path, exist_ok=True)

    #     with open(md_file, "w", encoding="utf-8") as fh:
    #         fh.write("# Example Project Title\n\n")
    #         fh.write("This is a sample markdown body. The generator will not modify this file.\n\n")
    #         fh.write("## Subsection\nDetails here.\n")

    print("[TEST] Instantiating PDFGenerator...")
    gen = PDFGenerator()

    # ✅ defensive try/catch so the test doesn’t kill your terminal
    try:
        pdf_path = gen.generate_pdf(project_id)
    except Exception as e:
        print("[TEST] ❌ PDF generator raised exception:", e)
        return

    print(f"[TEST] ✅ PDF generated at: {pdf_path}")

    if os.path.exists(pdf_path):
        print("[TEST] ✅ Confirmed PDF exists.")
        print("[TEST] Size (bytes):", os.path.getsize(pdf_path))
    else:
        print("[TEST] ❌ PDF missing — test failed.")

    print("[TEST] Done — no files deleted. Inspect the folder:")
    print("       ", project_path)

if __name__ == "__main__":
    main()
