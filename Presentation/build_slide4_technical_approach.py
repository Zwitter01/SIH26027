import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR

def build_slide4_technical_approach():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Colors
    DARK_BLUE = RGBColor(15, 23, 42)
    NAVY_ACCENT = RGBColor(2, 132, 199)
    TEXT_DARK = RGBColor(30, 41, 59)
    TEXT_MUTED = RGBColor(71, 85, 105)
    
    # 1. Slide Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.7), Inches(0.7))
    tf_title = title_box.text_frame
    p_title = tf_title.paragraphs[0]
    p_title.text = "TECHNICAL APPROACH"
    p_title.font.name = "Segoe UI"
    p_title.font.size = Pt(28)
    p_title.font.bold = True
    p_title.font.color.rgb = DARK_BLUE

    # ----------------------------------------------------
    # LEFT HALF: TECHNOLOGIES + 4-STEP IMPLEMENTATION FLOW
    # ----------------------------------------------------
    # Top Left Box: Technologies to be used (Rounded Rectangle Container)
    tech_container = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.6), Inches(1.15), Inches(5.6), Inches(3.4)
    )
    tech_container.fill.solid(); tech_container.fill.fore_color.rgb = RGBColor(248, 250, 252)
    tech_container.line.color.rgb = NAVY_ACCENT; tech_container.line.width = Pt(1.5)
    
    tf_t = tech_container.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_right = Inches(0.18)
    tf_t.margin_top = Inches(0.15)
    
    p = tf_t.paragraphs[0]
    p.text = "• Technologies to be used"
    p.font.name = "Segoe UI"; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = DARK_BLUE
    p.space_after = Pt(6)

    tech_items = [
        ("➔ Language & Backend: ", "Python 3.14 (High-Performance Async) | FastAPI + Pydantic V2 + OpenAPI"),
        ("➔ AI/ML & Optimization: ", "Google OR-Tools CP-SAT Constraint Solver + Multi-Objective Genetic Heuristics"),
        ("➔ Database: ", "SQLAlchemy 2.0 | SQLite (WAL Mode for Dev) / PostgreSQL (CRIS Production)"),
        ("➔ UI & Visuals: ", "Interactive D3.js Stringline (Marey) Diagram + Multi-Track Calendar Matrix"),
        ("➔ Connectors: ", "REST Webhooks for TMS (Civil), SMMS (Signals), TDMS (Traction), COA (Operations)")
    ]
    for b_txt, n_txt in tech_items:
        p_pt = tf_t.add_paragraph()
        p_pt.space_after = Pt(4)
        rb = p_pt.add_run(); rb.text = b_txt; rb.font.bold = True; rb.font.size = Pt(10); rb.font.color.rgb = DARK_BLUE
        rn = p_pt.add_run(); rn.text = n_txt; rn.font.size = Pt(10); rn.font.color.rgb = TEXT_DARK

    # Bottom Left Section Header: Methodology & Process
    m_head_box = slide.shapes.add_textbox(Inches(0.6), Inches(4.65), Inches(5.6), Inches(0.4))
    tf_mh = m_head_box.text_frame; tf_mh.word_wrap = True; tf_mh.margin_left = tf_mh.margin_right = tf_mh.margin_top = 0
    p_mh = tf_mh.paragraphs[0]
    p_mh.text = "• Methodology and Process (Implementation Flowchart)"
    p_mh.font.name = "Segoe UI"; p_mh.font.size = Pt(14); p_mh.font.bold = True; p_mh.font.color.rgb = DARK_BLUE

    # 4 Flowchart Step Badges
    steps_data = [
        ("STEP 1: INGEST", "TMS + SMMS +\nTDMS + COA", RGBColor(224, 242, 254), RGBColor(2, 132, 199), "🗄️"),
        ("STEP 2: MCDA", "Urgency + Safety\nOverdue x Speed", RGBColor(254, 237, 213), RGBColor(234, 88, 12), "⚖️"),
        ("STEP 3: BUNDLE", "Spatial Clustered\n10-km Sections", RGBColor(220, 252, 231), RGBColor(22, 163, 74), "📍"),
        ("STEP 4: SOLVE", "CP-SAT Off-peak\n15-min Headway", RGBColor(243, 232, 255), RGBColor(147, 51, 234), "🧩")
    ]
    
    step_w = 1.25
    step_gap = 0.15
    for i, (s_title, s_sub, bg_c, b_c, icon) in enumerate(steps_data):
        sx = 0.6 + i * (step_w + step_gap)
        s_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(sx), Inches(5.15), Inches(step_w), Inches(1.8))
        s_box.fill.solid(); s_box.fill.fore_color.rgb = bg_c; s_box.line.color.rgb = b_c; s_box.line.width = Pt(1.5)
        
        tf_s = s_box.text_frame; tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_right = Inches(0.06); tf_s.margin_top = Inches(0.1)
        
        # Icon
        p_ic = tf_s.paragraphs[0]; p_ic.text = icon; p_ic.alignment = PP_ALIGN.CENTER; p_ic.font.size = Pt(14); p_ic.space_after = Pt(2)
        
        # Title
        p_st = tf_s.add_paragraph(); p_st.text = s_title; p_st.alignment = PP_ALIGN.CENTER
        p_st.font.name = "Segoe UI"; p_st.font.size = Pt(8.5); p_st.font.bold = True; p_st.font.color.rgb = b_c; p_st.space_after = Pt(3)
        
        # Subtext
        p_sb = tf_s.add_paragraph(); p_sb.text = s_sub; p_sb.alignment = PP_ALIGN.CENTER
        p_sb.font.name = "Segoe UI"; p_sb.font.size = Pt(7.5); p_sb.font.color.rgb = TEXT_DARK

        # Connector arrow between steps
        if i < 3:
            arr_x = sx + step_w + 0.02
            arr_box = slide.shapes.add_textbox(Inches(arr_x), Inches(5.8), Inches(step_gap), Inches(0.4))
            tf_a = arr_box.text_frame; tf_a.margin_left = tf_a.margin_right = tf_a.margin_top = 0
            p_a = tf_a.paragraphs[0]; p_a.text = "➔"; p_a.font.size = Pt(11); p_a.font.color.rgb = RGBColor(100, 116, 139)

    # ----------------------------------------------------
    # RIGHT HALF: EDITABLE NATIVE ARCHITECTURE DIAGRAM
    # ----------------------------------------------------
    # Outer Frame for Right Architecture
    arch_frame = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(6.5), Inches(1.15), Inches(6.2), Inches(5.8)
    )
    arch_frame.fill.solid(); arch_frame.fill.fore_color.rgb = RGBColor(255, 255, 255)
    arch_frame.line.color.rgb = RGBColor(203, 213, 225); arch_frame.line.width = Pt(1.5)

    # Layer 1: Data & Ingestion (Top)
    l1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.7), Inches(1.3), Inches(5.8), Inches(1.4))
    l1.fill.solid(); l1.fill.fore_color.rgb = RGBColor(241, 245, 249); l1.line.color.rgb = RGBColor(148, 163, 184); l1.line.width = Pt(1)
    tf = l1.text_frame; tf.margin_left = Inches(0.1); tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]; p.text = "Data & Ingestion Layer"; p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # Nodes inside Layer 1
    # Train Icon
    tr_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.6), Inches(0.8), Inches(0.4))
    tr_box.text_frame.margin_left = tr_box.text_frame.margin_top = 0
    tr_box.text_frame.paragraphs[0].text = "🚆 IR LIVE"; tr_box.text_frame.paragraphs[0].font.size = Pt(8); tr_box.text_frame.paragraphs[0].font.bold = True

    # COA Node
    n_coa = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.7), Inches(1.5), Inches(2.2), Inches(0.4))
    n_coa.fill.solid(); n_coa.fill.fore_color.rgb = RGBColor(11, 19, 41); n_coa.line.color.rgb = RGBColor(56, 189, 248); n_coa.line.width = Pt(1)
    p = n_coa.text_frame.paragraphs[0]; p.text = "📊 COA Real-Time Train Feed"; p.font.size = Pt(8); p.font.color.rgb = RGBColor(255, 255, 255); p.alignment = PP_ALIGN.CENTER

    # TMS Node
    n_tms = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.05), Inches(1.5), Inches(2.3), Inches(0.4))
    n_tms.fill.solid(); n_tms.fill.fore_color.rgb = RGBColor(11, 19, 41); n_tms.line.color.rgb = RGBColor(56, 189, 248); n_tms.line.width = Pt(1)
    p = n_tms.text_frame.paragraphs[0]; p.text = "⚙️ TMS / SMMS / TDMS APIs"; p.font.size = Pt(8); p.font.color.rgb = RGBColor(255, 255, 255); p.alignment = PP_ALIGN.CENTER

    # Database Cylinder
    n_db = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.5), Inches(2.05), Inches(2.8), Inches(0.55))
    n_db.fill.solid(); n_db.fill.fore_color.rgb = RGBColor(2, 132, 199); n_db.line.color.rgb = RGBColor(56, 189, 248); n_db.line.width = Pt(1.5)
    tf_db = n_db.text_frame; tf_db.margin_top = Inches(0.06)
    p = tf_db.paragraphs[0]; p.text = "🪶 SQLite / PostgreSQL 🐘"; p.font.size = Pt(9); p.font.bold = True; p.font.color.rgb = RGBColor(255, 255, 255); p.alignment = PP_ALIGN.CENTER
    p_sub = tf_db.add_paragraph(); p_sub.text = "(WAL Mode Enabled)"; p_sub.font.size = Pt(7); p_sub.font.color.rgb = RGBColor(224, 242, 254); p_sub.alignment = PP_ALIGN.CENTER

    # Layer 2: FastAPI Service Layer (Middle)
    l2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.4), Inches(2.95), Inches(4.9), Inches(1.2))
    l2.fill.solid(); l2.fill.fore_color.rgb = RGBColor(241, 245, 249); l2.line.color.rgb = RGBColor(148, 163, 184); l2.line.width = Pt(1)
    p = l2.text_frame.paragraphs[0]; p.text = "FastAPI Service Layer"; p.font.size = Pt(9); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # FastAPI API Bar
    n_fapi = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.6), Inches(3.2), Inches(2.5), Inches(0.35))
    n_fapi.fill.solid(); n_fapi.fill.fore_color.rgb = RGBColor(4, 40, 18); n_fapi.line.color.rgb = RGBColor(34, 197, 94); n_fapi.line.width = Pt(1)
    p = n_fapi.text_frame.paragraphs[0]; p.text = "⚡ FastAPI Async REST API"; p.font.size = Pt(8); p.font.bold = True; p.font.color.rgb = RGBColor(255, 255, 255); p.alignment = PP_ALIGN.CENTER

    # Scorer Engine
    n_sc = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.3), Inches(3.65), Inches(1.8), Inches(0.35))
    n_sc.fill.solid(); n_sc.fill.fore_color.rgb = RGBColor(15, 23, 42); n_sc.line.color.rgb = RGBColor(71, 85, 105); n_sc.line.width = Pt(1)
    p = n_sc.text_frame.paragraphs[0]; p.text = "Priority Scorer Engine"; p.font.size = Pt(7.5); p.font.color.rgb = RGBColor(255, 255, 255); p.alignment = PP_ALIGN.CENTER

    # Spatial Detector
    n_dt = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.25), Inches(3.65), Inches(1.9), Inches(0.35))
    n_dt.fill.solid(); n_dt.fill.fore_color.rgb = RGBColor(15, 23, 42); n_dt.line.color.rgb = RGBColor(71, 85, 105); n_dt.line.width = Pt(1)
    p = n_dt.text_frame.paragraphs[0]; p.text = "Conflict Detector"; p.font.size = Pt(7.5); p.font.color.rgb = RGBColor(255, 255, 255); p.alignment = PP_ALIGN.CENTER

    # Layer 3: Presentation & Dispatch (Bottom-Left of Arch)
    l3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.7), Inches(4.35), Inches(5.8), Inches(0.85))
    l3.fill.solid(); l3.fill.fore_color.rgb = RGBColor(241, 245, 249); l3.line.color.rgb = RGBColor(148, 163, 184); l3.line.width = Pt(1)
    p = l3.text_frame.paragraphs[0]; p.text = "Presentation & Dispatch Layer"; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # 3 Dispatch Cards
    n_d3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.65), Inches(1.8), Inches(0.4))
    n_d3.fill.solid(); n_d3.fill.fore_color.rgb = RGBColor(15, 23, 42); n_d3.line.color.rgb = RGBColor(249, 115, 22); n_d3.line.width = Pt(1)
    p = n_d3.text_frame.paragraphs[0]; p.text = "🟠 D3.js Stringline"; p.font.size = Pt(7); p.font.color.rgb = RGBColor(255, 255, 255); p.alignment = PP_ALIGN.CENTER

    n_cal = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.7), Inches(4.65), Inches(1.8), Inches(0.4))
    n_cal.fill.solid(); n_cal.fill.fore_color.rgb = RGBColor(15, 23, 42); n_cal.line.color.rgb = RGBColor(71, 85, 105); n_cal.line.width = Pt(1)
    p = n_cal.text_frame.paragraphs[0]; p.text = "📅 Weekly Calendar"; p.font.size = Pt(7); p.font.color.rgb = RGBColor(255, 255, 255); p.alignment = PP_ALIGN.CENTER

    n_ptw = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.6), Inches(4.65), Inches(1.8), Inches(0.4))
    n_ptw.fill.solid(); n_ptw.fill.fore_color.rgb = RGBColor(15, 23, 42); n_ptw.line.color.rgb = RGBColor(71, 85, 105); n_ptw.line.width = Pt(1)
    p = n_ptw.text_frame.paragraphs[0]; p.text = "📄 Form 351 PTW"; p.font.size = Pt(7); p.font.color.rgb = RGBColor(255, 255, 255); p.alignment = PP_ALIGN.CENTER

    # Layer 4: Constraint Programming Engine (Bottom)
    l4 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.7), Inches(5.35), Inches(5.8), Inches(1.45))
    l4.fill.solid(); l4.fill.fore_color.rgb = RGBColor(241, 245, 249); l4.line.color.rgb = RGBColor(148, 163, 184); l4.line.width = Pt(1)
    p = l4.text_frame.paragraphs[0]; p.text = "Constraint Programming Engine"; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # CP-SAT Solver Banner
    n_cpsat = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.5), Inches(5.6), Inches(4.2), Inches(0.35))
    n_cpsat.fill.solid(); n_cpsat.fill.fore_color.rgb = RGBColor(30, 27, 75); n_cpsat.line.color.rgb = RGBColor(59, 130, 246); n_cpsat.line.width = Pt(1.5)
    p = n_cpsat.text_frame.paragraphs[0]; p.text = "🧩 Google OR-Tools CP-SAT Solver"; p.font.size = Pt(8); p.font.bold = True; p.font.color.rgb = RGBColor(96, 165, 250); p.alignment = PP_ALIGN.CENTER

    # Hard & Soft constraints cards
    n_hard = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(6.05), Inches(2.7), Inches(0.65))
    n_hard.fill.solid(); n_hard.fill.fore_color.rgb = RGBColor(15, 23, 42); n_hard.line.color.rgb = RGBColor(71, 85, 105); n_hard.line.width = Pt(1)
    tf_h = n_hard.text_frame; tf_h.margin_top = Inches(0.04)
    p = tf_h.paragraphs[0]; p.text = "Hard Constraints Validator"; p.font.size = Pt(7.5); p.font.bold = True; p.font.color.rgb = RGBColor(96, 165, 250)
    p1 = tf_h.add_paragraph(); p1.text = "• NoOverlap (Machines & Tracks)"; p1.font.size = Pt(6.5); p1.font.color.rgb = RGBColor(203, 213, 225)
    p2 = tf_h.add_paragraph(); p2.text = "• Zero Train-Block Collision"; p2.font.size = Pt(6.5); p2.font.bold = True; p2.font.color.rgb = RGBColor(74, 222, 128)

    n_soft = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.65), Inches(6.05), Inches(2.7), Inches(0.65))
    n_soft.fill.solid(); n_soft.fill.fore_color.rgb = RGBColor(15, 23, 42); n_soft.line.color.rgb = RGBColor(71, 85, 105); n_soft.line.width = Pt(1)
    tf_s = n_soft.text_frame; tf_s.margin_top = Inches(0.04)
    p = tf_s.paragraphs[0]; p.text = "Soft Constraints & Objective"; p.font.size = Pt(7.5); p.font.bold = True; p.font.color.rgb = RGBColor(192, 132, 252)
    p1 = tf_s.add_paragraph(); p1.text = "• Maximize High-Priority Tasks"; p1.font.size = Pt(6.5); p1.font.color.rgb = RGBColor(203, 213, 225)
    p2 = tf_s.add_paragraph(); p2.text = "• Shadow Block Bonus"; p2.font.size = Pt(6.5); p2.font.bold = True; p2.font.color.rgb = RGBColor(244, 114, 182)

    # Save standalone Slide 4 presentation
    output_path = r"c:\Users\kvish\OneDrive\Desktop\railway-planner\Slide4_Technical_Approach_Editable.pptx"
    prs.save(output_path)
    print(f"Slide 4 Technical Approach saved to: {output_path}")

if __name__ == "__main__":
    build_slide4_technical_approach()
