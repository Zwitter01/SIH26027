import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def generate_editable_slide():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Blank slide layout
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Color Constants
    DARK_BLUE = RGBColor(15, 23, 42)
    ACCENT_BLUE = RGBColor(2, 132, 199)
    TEXT_DARK = RGBColor(30, 41, 59)
    TEXT_MUTED = RGBColor(71, 85, 105)

    # 1. Slide Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.8))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = "FEASIBILITY AND VIABILITY"
    p_title.font.name = "Segoe UI"
    p_title.font.size = Pt(28)
    p_title.font.bold = True
    p_title.font.color.rgb = DARK_BLUE

    # ----------------------------------------------------
    # LEFT COLUMN (X = 0.8 in, Width = 5.6 in)
    # ----------------------------------------------------
    left_col_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(5.6), Inches(5.8))
    tf_left = left_col_box.text_frame
    tf_left.word_wrap = True
    tf_left.margin_left = tf_left.margin_right = tf_left.margin_top = tf_left.margin_bottom = 0

    # Section 1: Feasibility
    p = tf_left.paragraphs[0]
    p.text = "⚖️ Feasibility:"
    p.font.name = "Segoe UI"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.space_after = Pt(4)

    feasibility_points = [
        ("1. Technical: ", "Powered by Google OR-Tools CP-SAT constraint solver running in <0.06s with sub-100ms latency."),
        ("2. Modularisation: ", "Layered architecture enables phased rollout from 131 km pilot to national scale."),
        ("3. Integration: ", "Non-invasive REST API/webhook integration with existing CRIS, TMS, SMMS, and COA servers."),
        ("4. Economic: ", "Zero specialized hardware required; runs on existing Indian Railways cloud infrastructure.")
    ]
    for bold_txt, norm_txt in feasibility_points:
        p_pt = tf_left.add_paragraph()
        p_pt.space_after = Pt(3)
        run_b = p_pt.add_run()
        run_b.text = bold_txt
        run_b.font.name = "Segoe UI"
        run_b.font.size = Pt(11.5)
        run_b.font.bold = True
        run_b.font.color.rgb = DARK_BLUE

        run_n = p_pt.add_run()
        run_n.text = norm_txt
        run_n.font.name = "Segoe UI"
        run_n.font.size = Pt(11.5)
        run_n.font.color.rgb = TEXT_DARK

    # Space before next block
    p_sp1 = tf_left.add_paragraph()
    p_sp1.space_before = Pt(8)
    p_sp1.text = "⚙️ Viability:"
    p_sp1.font.name = "Segoe UI"
    p_sp1.font.size = Pt(16)
    p_sp1.font.bold = True
    p_sp1.font.color.rgb = DARK_BLUE
    p_sp1.space_after = Pt(4)

    viability_points = [
        ("1. Regulatory Compliance: ", "Built strictly around Indian Railways G&SR Rules and Block Manuals."),
        ("2. Standardized PTW: ", "Auto-generates statutory Form 351 Joint Disconnection Notices with 3-dept sign-offs."),
        ("3. High Scalability: ", "Extensible across all 17 Zonal Railways and 68,000+ route kilometers."),
        ("4. Operational Safety: ", "Mathematical guarantee of zero train-block collisions eliminates human error.")
    ]
    for bold_txt, norm_txt in viability_points:
        p_pt = tf_left.add_paragraph()
        p_pt.space_after = Pt(3)
        run_b = p_pt.add_run()
        run_b.text = bold_txt
        run_b.font.name = "Segoe UI"
        run_b.font.size = Pt(11.5)
        run_b.font.bold = True
        run_b.font.color.rgb = DARK_BLUE

        run_n = p_pt.add_run()
        run_n.text = norm_txt
        run_n.font.name = "Segoe UI"
        run_n.font.size = Pt(11.5)
        run_n.font.color.rgb = TEXT_DARK

    # Space before Challenges block
    p_sp2 = tf_left.add_paragraph()
    p_sp2.space_before = Pt(8)
    p_sp2.text = "⚠️ Challenges & Mitigations:"
    p_sp2.font.name = "Segoe UI"
    p_sp2.font.size = Pt(16)
    p_sp2.font.bold = True
    p_sp2.font.color.rgb = DARK_BLUE
    p_sp2.space_after = Pt(4)

    challenge_points = [
        ("1. Data Inconsistency: ", "Pydantic schemas sanitize field timestamps, chainage markers, and defect logs."),
        ("2. Machine Conflicts: ", "NoOverlap logic prevents double-booking scarce Track Machines and Tower Wagons."),
        ("3. Emergency Disruptions: ", "Dynamic What-If engine reschedules around urgent rail flaws in <150ms.")
    ]
    for bold_txt, norm_txt in challenge_points:
        p_pt = tf_left.add_paragraph()
        p_pt.space_after = Pt(3)
        run_b = p_pt.add_run()
        run_b.text = bold_txt
        run_b.font.name = "Segoe UI"
        run_b.font.size = Pt(11.5)
        run_b.font.bold = True
        run_b.font.color.rgb = DARK_BLUE

        run_n = p_pt.add_run()
        run_n.text = norm_txt
        run_n.font.name = "Segoe UI"
        run_n.font.size = Pt(11.5)
        run_n.font.color.rgb = TEXT_DARK

    # ----------------------------------------------------
    # RIGHT COLUMN (X = 6.8 in, Width = 5.7 in)
    # ----------------------------------------------------
    right_col_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.2), Inches(5.7), Inches(3.6))
    tf_right = right_col_box.text_frame
    tf_right.word_wrap = True
    tf_right.margin_left = tf_right.margin_right = tf_right.margin_top = tf_right.margin_bottom = 0

    # Section 4: Use Cases
    p_r1 = tf_right.paragraphs[0]
    p_r1.text = "🚆 Use Cases:"
    p_r1.font.name = "Segoe UI"
    p_r1.font.size = Pt(16)
    p_r1.font.bold = True
    p_r1.font.color.rgb = DARK_BLUE
    p_r1.space_after = Pt(4)

    use_case_points = [
        ("1. Section Controllers: ", "Automated corridor block windows without manual phone coordination."),
        ("2. Civil / P-Way (TMS): ", "Prioritizes urgent IMR rail flaw welds and deep screening tamping blocks."),
        ("3. Traction (TDMS): ", "Synchronizes OHE cantilever overhauls and power isolation with track closures."),
        ("4. Signal & Telecom (SMMS): ", "Co-schedules axle counter testing and point machine calibration into Mega Blocks.")
    ]
    for bold_txt, norm_txt in use_case_points:
        p_pt = tf_right.add_paragraph()
        p_pt.space_after = Pt(3)
        run_b = p_pt.add_run()
        run_b.text = bold_txt
        run_b.font.name = "Segoe UI"
        run_b.font.size = Pt(11.5)
        run_b.font.bold = True
        run_b.font.color.rgb = DARK_BLUE

        run_n = p_pt.add_run()
        run_n.text = norm_txt
        run_n.font.name = "Segoe UI"
        run_n.font.size = Pt(11.5)
        run_n.font.color.rgb = TEXT_DARK

    # Space before Operational Potential
    p_r2 = tf_right.add_paragraph()
    p_r2.space_before = Pt(8)
    p_r2.text = "📊 Operational Potential:"
    p_r2.font.name = "Segoe UI"
    p_r2.font.size = Pt(16)
    p_r2.font.bold = True
    p_r2.font.color.rgb = DARK_BLUE
    p_r2.space_after = Pt(4)

    operational_points = [
        ("1. Availability Gain: ", "Elevates corridor asset availability from 91.2% to 96.6%+, unlocking new paths."),
        ("2. Downtime Compression: ", "Multi-department Shadow Blocks cut cumulative closures by up to 40%."),
        ("3. Punctuality Boost: ", "Eliminates cascading train detentions and unplanned speed restrictions."),
        ("4. Digital Governance: ", "100% digital audit trail from maintenance requisition to final section clearance.")
    ]
    for bold_txt, norm_txt in operational_points:
        p_pt = tf_right.add_paragraph()
        p_pt.space_after = Pt(3)
        run_b = p_pt.add_run()
        run_b.text = bold_txt
        run_b.font.name = "Segoe UI"
        run_b.font.size = Pt(11.5)
        run_b.font.bold = True
        run_b.font.color.rgb = DARK_BLUE

        run_n = p_pt.add_run()
        run_n.text = norm_txt
        run_n.font.name = "Segoe UI"
        run_n.font.size = Pt(11.5)
        run_n.font.color.rgb = TEXT_DARK

    # ----------------------------------------------------
    # BOTTOM-RIGHT HIGHLIGHT CARD (Rounded Box)
    # ----------------------------------------------------
    card_shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(6.8), Inches(4.9), Inches(5.7), Inches(2.1)
    )
    # Style card
    card_shape.fill.solid()
    card_shape.fill.fore_color.rgb = RGBColor(240, 249, 255) # Light sky blue
    card_shape.line.color.rgb = RGBColor(2, 132, 199)       # Sky blue border
    card_shape.line.width = Pt(1.5)

    tf_card = card_shape.text_frame
    tf_card.word_wrap = True
    tf_card.margin_left = Inches(0.18)
    tf_card.margin_right = Inches(0.18)
    tf_card.margin_top = Inches(0.12)
    tf_card.margin_bottom = Inches(0.12)

    p_card_title = tf_card.paragraphs[0]
    p_card_title.text = "⭐ Supporting Facts for Feasibility & Viability"
    p_card_title.font.name = "Segoe UI"
    p_card_title.font.size = Pt(13)
    p_card_title.font.bold = True
    p_card_title.font.color.rgb = ACCENT_BLUE
    p_card_title.space_after = Pt(4)

    card_points = [
        "➔ CAG Railway Audit: Studies indicate up to 30–35% of sanctioned blocks are underutilized due to decentralized manual coordination between departments.",
        "➔ Network Scale: Coordinates across 68,000+ route km & 13,000+ daily trains, recovering thousands of train delay hours annually.",
        "➔ Proven Benchmark: NDLS–ALJN pilot achieved 100% critical task completion with 4 Mega Blocks in under 0.1 seconds."
    ]
    for cp in card_points:
        p_cp = tf_card.add_paragraph()
        p_cp.text = cp
        p_cp.font.name = "Segoe UI"
        p_cp.font.size = Pt(10.5)
        p_cp.font.color.rgb = TEXT_DARK
        p_cp.space_after = Pt(2)

    output_path = r"c:\Users\kvish\OneDrive\Desktop\railway-planner\Slide5_Feasibility_Editable.pptx"
    prs.save(output_path)
    print(f"Editable PowerPoint presentation saved to: {output_path}")

if __name__ == "__main__":
    generate_editable_slide()
