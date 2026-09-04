import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_slide6_research_references():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Color Palette
    DARK_BLUE = RGBColor(15, 23, 42)
    NAVY_ACCENT = RGBColor(2, 132, 199)
    TEXT_DARK = RGBColor(30, 41, 59)
    TEXT_MUTED = RGBColor(71, 85, 105)
    TABLE_HEADER_BG = RGBColor(241, 245, 249)
    ROW_BG_ALT = RGBColor(248, 250, 252)

    # 1. Slide Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.7), Inches(0.7))
    tf_title = title_box.text_frame
    p_title = tf_title.paragraphs[0]
    p_title.text = "RESEARCH AND REFERENCES"
    p_title.font.name = "Segoe UI"
    p_title.font.size = Pt(28)
    p_title.font.bold = True
    p_title.font.color.rgb = DARK_BLUE

    # ----------------------------------------------------
    # TOP-LEFT: REFERENCES & STANDARDS (X = 0.8 in, Width = 5.2 in)
    # ----------------------------------------------------
    ref_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(5.2), Inches(3.2))
    tf_ref = ref_box.text_frame
    tf_ref.word_wrap = True
    tf_ref.margin_left = tf_ref.margin_right = tf_ref.margin_top = 0

    p_ref_head = tf_ref.paragraphs[0]
    p_ref_head.text = "❖ References & Research:"
    p_ref_head.font.name = "Segoe UI"
    p_ref_head.font.size = Pt(16)
    p_ref_head.font.bold = True
    p_ref_head.font.color.rgb = NAVY_ACCENT
    p_ref_head.space_after = Pt(6)

    references_data = [
        ("Official Indian Railways Systems:", [
            "TMS (Track Management System): https://tms.indianrailways.gov.in/",
            "COA (Control Office Application): https://coa.cris.org.in/",
            "BDMS (Block Demarcation & Management System): https://ireps.gov.in/"
        ]),
        ("Regulatory Standards & Working Manuals:", [
            "Indian Railways Permanent Way Manual (IRPWM - G&SR Rules)",
            "TRD Maintenance Manual for 25kV AC Traction Power Distribution",
            "Signal Engineering Manual (SEM) for Interlocking & Block Instruments"
        ]),
        ("Audits & Optimization Benchmarks:", [
            "CAG Audit Report No. 22 on Punctuality & Block Utilisation in IR",
            "Google OR-Tools CP-SAT Combinatorial Optimization Suite (v9.15)"
        ])
    ]

    for category, links in references_data:
        p_c = tf_ref.add_paragraph()
        p_c.text = category
        p_c.font.name = "Segoe UI"
        p_c.font.size = Pt(11)
        p_c.font.bold = True
        p_c.font.color.rgb = DARK_BLUE
        p_c.space_before = Pt(3)
        p_c.space_after = Pt(1)

        for lnk in links:
            p_l = tf_ref.add_paragraph()
            p_l.text = "➤ " + lnk
            p_l.font.name = "Segoe UI"
            p_l.font.size = Pt(9.5)
            p_l.font.color.rgb = TEXT_DARK
            p_l.space_after = Pt(1)

    # ----------------------------------------------------
    # BOTTOM-LEFT: PLACEHOLDER FOR WORKING BASE PROTOTYPE
    # ----------------------------------------------------
    proto_card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.8), Inches(4.55), Inches(5.2), Inches(2.45)
    )
    proto_card.fill.solid()
    proto_card.fill.fore_color.rgb = RGBColor(240, 249, 255) # Light sky blue
    proto_card.line.color.rgb = RGBColor(2, 132, 199)
    proto_card.line.width = Pt(1.5)

    tf_proto = proto_card.text_frame
    tf_proto.word_wrap = True
    tf_proto.margin_left = tf_proto.margin_right = Inches(0.2)
    tf_proto.margin_top = Inches(0.15)

    p_pr = tf_proto.paragraphs[0]
    p_pr.text = "💻 Working Base Prototype Model (Local Server: 127.0.0.1:8000)"
    p_pr.font.name = "Segoe UI"
    p_pr.font.size = Pt(12)
    p_pr.font.bold = True
    p_pr.font.color.rgb = NAVY_ACCENT
    p_pr.space_after = Pt(4)

    p_desc = tf_proto.add_paragraph()
    p_desc.text = "• Live CP-SAT Optimizer solves 131.2 km corridor (NDLS–ALJN) in 0.06s.\n• Features D3.js Stringline (Marey) Diagram, Weekly Block Calendar Grid, and 4 Coordinated Multi-Dept Shadow Blocks.\n\n[PASTE YOUR DASHBOARD SCREENSHOT HERE]"
    p_desc.font.name = "Segoe UI"
    p_desc.font.size = Pt(10)
    p_desc.font.color.rgb = TEXT_DARK

    # ----------------------------------------------------
    # RIGHT HALF: COMPARISON WITH EXISTING SYSTEMS (TABLE)
    # ----------------------------------------------------
    # Table Header Box
    head_box = slide.shapes.add_textbox(Inches(6.3), Inches(1.15), Inches(6.2), Inches(0.4))
    tf_h = head_box.text_frame
    p_h = tf_h.paragraphs[0]
    p_h.text = "❖ Comparison with Existing Systems:"
    p_h.font.name = "Segoe UI"
    p_h.font.size = Pt(16)
    p_h.font.bold = True
    p_h.font.color.rgb = NAVY_ACCENT

    # Add Table (8 rows, 5 columns)
    table_shape = slide.shapes.add_table(
        rows=8, cols=5,
        left=Inches(6.3), top=Inches(1.6),
        width=Inches(6.2), height=Inches(5.4)
    )
    table = table_shape.table

    # Column widths
    table.columns[0].width = Inches(2.2) # Feature
    table.columns[1].width = Inches(1.1) # Our AI System
    table.columns[2].width = Inches(1.0) # Manual BDMS
    table.columns[3].width = Inches(0.95) # Standalone COA
    table.columns[4].width = Inches(0.95) # TMS/SMMS Silos

    # Headers
    headers = ["Feature", "Our AI System\n(SIH26027)", "Manual Plan\n(BDMS)", "Standalone\nCOA", "TMS/TDMS\nStandalone"]
    for col_idx, h_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(15, 23, 42) if col_idx == 1 else RGBColor(226, 232, 240)
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.alignment = PP_ALIGN.CENTER
        p.font.name = "Segoe UI"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255) if col_idx == 1 else DARK_BLUE

    # Table Row Data
    rows_data = [
        ("Multi-Dept Shadow Blocking", "☑️ Yes (Auto)", "❌ No", "❌ No", "❌ No"),
        ("4-Factor AI Priority Ranking", "☑️ Yes (AI)", "❌ No", "❌ No", "❌ (Basic)"),
        ("Zero Train Conflict Guarantee", "☑️ Yes (Hard)", "❌ (Prone)", "❌ (Manual)", "❌ No"),
        ("Night Window (01:00-05:00) Sync", "☑️ Yes (Auto)", "❌ (Manual)", "❌ No", "❌ No"),
        ("Sub-100ms Optimization Latency", "☑️ Yes (0.06s)", "❌ (3-5 Days)", "❌ No", "❌ No"),
        ("Live 'What-If' Parameter Sliders", "☑️ Yes (Live)", "❌ No", "❌ No", "❌ No"),
        ("Statutory Form 351 PTW Memo", "☑️ Yes (1-Click)", "❌ (Manual)", "❌ No", "❌ No"),
    ]

    for row_idx, row_content in enumerate(rows_data, start=1):
        for col_idx, text_val in enumerate(row_content):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            if col_idx == 1:
                cell.fill.fore_color.rgb = RGBColor(224, 242, 254) # Highlight our system
            elif row_idx % 2 == 1:
                cell.fill.fore_color.rgb = RGBColor(248, 250, 252)
            else:
                cell.fill.fore_color.rgb = RGBColor(255, 255, 255)

            p = cell.text_frame.paragraphs[0]
            p.text = text_val
            p.alignment = PP_ALIGN.LEFT if col_idx == 0 else PP_ALIGN.CENTER
            p.font.name = "Segoe UI"
            p.font.size = Pt(9.5)
            if col_idx == 1:
                p.font.bold = True
                p.font.color.rgb = RGBColor(3, 105, 161)
            elif "☑️" in text_val:
                p.font.bold = True
                p.font.color.rgb = RGBColor(22, 163, 74)
            elif "❌" in text_val:
                p.font.color.rgb = RGBColor(225, 29, 72)
            else:
                p.font.color.rgb = TEXT_DARK

    output_path = r"c:\Users\kvish\OneDrive\Desktop\railway-planner\Slide6_Research_and_References_Editable.pptx"
    prs.save(output_path)
    print(f"Slide 6 Research and References saved to: {output_path}")

if __name__ == "__main__":
    build_slide6_research_references()
