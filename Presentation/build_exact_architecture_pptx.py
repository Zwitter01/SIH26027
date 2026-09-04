import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR

def generate_exact_architecture_pptx():
    prs = Presentation()
    # 16:9 Widescreen slide
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Color Palette matching the exact image
    DARK_BLUE = RGBColor(15, 23, 42)
    BG_CARD_NAVY = RGBColor(11, 25, 44)        # #0b192c Dark card body
    CONTAINER_BG = RGBColor(203, 213, 225)     # #cbd5e1 Gray container box
    CONTAINER_BORDER = RGBColor(100, 116, 139) # #64748b Slate border
    
    CYAN_BORDER = RGBColor(2, 132, 199)        # #0284c7
    CYAN_GRADIENT = RGBColor(3, 105, 161)      # #0369a1
    CYAN_TEXT = RGBColor(56, 189, 248)         # #38bdf8
    
    GREEN_BORDER = RGBColor(34, 197, 94)       # #22c55e
    GREEN_BG = RGBColor(4, 40, 18)             # #042812
    GREEN_TEXT = RGBColor(74, 222, 128)        # #4ade80
    
    ORANGE_BORDER = RGBColor(234, 88, 12)      # #ea580c
    PURPLE_BORDER = RGBColor(168, 85, 247)     # #a855f7
    PURPLE_TEXT = RGBColor(192, 132, 252)      # #c084fc
    PINK_TEXT = RGBColor(244, 114, 182)        # #f472b6
    
    WHITE = RGBColor(255, 255, 255)
    ARROW_COLOR = RGBColor(2, 132, 199)

    def draw_connector(x1, y1, x2, y2):
        conn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
        conn.line.color.rgb = ARROW_COLOR
        conn.line.width = Pt(2)

    # =========================================================================
    # 1. LAYER 1: DATA & INGESTION LAYER (Top)
    # =========================================================================
    # Train Graphic Badge Top-Left outside
    tr_badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.3), Inches(0.85), Inches(1.5), Inches(0.48))
    tr_badge.fill.solid(); tr_badge.fill.fore_color.rgb = BG_CARD_NAVY
    tr_badge.line.color.rgb = CYAN_BORDER; tr_badge.line.width = Pt(1.5)
    tf_tr = tr_badge.text_frame; tf_tr.word_wrap = True
    p = tf_tr.paragraphs[0]; p.text = "🚆 🚋  IR LIVE"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = CYAN_TEXT

    # Layer 1 Gray Container Box
    l1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.9), Inches(0.35), Inches(5.8), Inches(2.2))
    l1.fill.solid(); l1.fill.fore_color.rgb = CONTAINER_BG; l1.line.color.rgb = CONTAINER_BORDER; l1.line.width = Pt(1.5)
    tf = l1.text_frame; tf.margin_left = Inches(0.18); tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "Data & Ingestion Layer"; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # COA Feed Node
    n_coa = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.15), Inches(0.8), Inches(2.5), Inches(0.52))
    n_coa.fill.solid(); n_coa.fill.fore_color.rgb = BG_CARD_NAVY; n_coa.line.color.rgb = CYAN_BORDER; n_coa.line.width = Pt(1.5)
    tf = n_coa.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "📈 COA Real-Time Train Feed"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(9.5); p.font.bold = True; p.font.color.rgb = WHITE

    # TMS Node
    n_tms = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(0.8), Inches(2.55), Inches(0.52))
    n_tms.fill.solid(); n_tms.fill.fore_color.rgb = BG_CARD_NAVY; n_tms.line.color.rgb = CYAN_BORDER; n_tms.line.width = Pt(1.5)
    tf = n_tms.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "⚙️ TMS / SMMS / TDMS Task APIs"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(9.5); p.font.bold = True; p.font.color.rgb = WHITE

    # Database Cylinder Node
    n_db = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.1), Inches(1.6), Inches(3.4), Inches(0.75))
    n_db.fill.solid(); n_db.fill.fore_color.rgb = CYAN_GRADIENT; n_db.line.color.rgb = CYAN_TEXT; n_db.line.width = Pt(2)
    tf_db = n_db.text_frame; tf_db.word_wrap = True; tf_db.margin_top = Inches(0.08)
    p = tf_db.paragraphs[0]; p.text = "🗄️ SQLite / PostgreSQL 🐘"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = WHITE
    p_sub = tf_db.add_paragraph(); p_sub.text = "(WAL Mode Enabled)"; p_sub.alignment = PP_ALIGN.CENTER; p_sub.font.size = Pt(8.5); p_sub.font.color.rgb = RGBColor(224, 242, 254)

    # =========================================================================
    # 2. LAYER 2: FASTAPI SERVICE LAYER (Middle)
    # =========================================================================
    # Layer 2 Gray Container Box
    l2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(2.9), Inches(5.1), Inches(1.9))
    l2.fill.solid(); l2.fill.fore_color.rgb = CONTAINER_BG; l2.line.color.rgb = CONTAINER_BORDER; l2.line.width = Pt(1.5)
    tf = l2.text_frame; tf.margin_left = Inches(0.18); tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "FastAPI Service Layer"; p.font.size = Pt(10.5); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # FastAPI API Bar
    n_fapi = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.75), Inches(3.28), Inches(2.6), Inches(0.48))
    n_fapi.fill.solid(); n_fapi.fill.fore_color.rgb = GREEN_BG; n_fapi.line.color.rgb = GREEN_BORDER; n_fapi.line.width = Pt(1.5)
    tf = n_fapi.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "⚡ FastAPI Async REST API"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(9.5); p.font.bold = True; p.font.color.rgb = WHITE

    # Priority Scorer Engine
    n_sc = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.3), Inches(4.05), Inches(1.85), Inches(0.55))
    n_sc.fill.solid(); n_sc.fill.fore_color.rgb = BG_CARD_NAVY; n_sc.line.color.rgb = RGBColor(71, 85, 105); n_sc.line.width = Pt(1)
    tf = n_sc.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]; p.text = "Priority Scorer Engine"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(9); p.font.bold = True; p.font.color.rgb = WHITE

    # Conflict Detector
    n_dt = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.35), Inches(4.05), Inches(2.05), Inches(0.55))
    n_dt.fill.solid(); n_dt.fill.fore_color.rgb = BG_CARD_NAVY; n_dt.line.color.rgb = RGBColor(71, 85, 105); n_dt.line.width = Pt(1)
    tf = n_dt.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "Spatial-Temporal Conflict\nDetector"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = WHITE

    # =========================================================================
    # 3. LAYER 3: PRESENTATION & DISPATCH LAYER (Bottom-Left)
    # =========================================================================
    # Layer 3 Gray Container Box
    l3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.3), Inches(5.15), Inches(7.1), Inches(1.15))
    l3.fill.solid(); l3.fill.fore_color.rgb = CONTAINER_BG; l3.line.color.rgb = CONTAINER_BORDER; l3.line.width = Pt(1.5)
    tf = l3.text_frame; tf.margin_left = Inches(0.18); tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]; p.text = "Presentation & Dispatch Layer"; p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # D3 Stringline Chart Card
    n_d3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(5.5), Inches(2.1), Inches(0.58))
    n_d3.fill.solid(); n_d3.fill.fore_color.rgb = BG_CARD_NAVY; n_d3.line.color.rgb = ORANGE_BORDER; n_d3.line.width = Pt(1.5)
    tf = n_d3.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]; p.text = "🟠 D3.js Stringline Chart"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = WHITE

    # Calendar Card
    n_cal = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.8), Inches(5.5), Inches(2.2), Inches(0.58))
    n_cal.fill.solid(); n_cal.fill.fore_color.rgb = BG_CARD_NAVY; n_cal.line.color.rgb = CYAN_BORDER; n_cal.line.width = Pt(1.5)
    tf = n_cal.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "📅 Weekly Calendar &\nGantt"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = WHITE

    # PTW Notice Card
    n_ptw = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.2), Inches(5.5), Inches(2.0), Inches(0.58))
    n_ptw.fill.solid(); n_ptw.fill.fore_color.rgb = BG_CARD_NAVY; n_ptw.line.color.rgb = PURPLE_BORDER; n_ptw.line.width = Pt(1.5)
    tf = n_ptw.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]; p.text = "📄 Form 351 PTW Notice"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = WHITE

    # =========================================================================
    # 4. LAYER 4: CONSTRAINT PROGRAMMING ENGINE (Bottom-Right)
    # =========================================================================
    # Layer 4 Gray Container Box
    l4 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.65), Inches(5.15), Inches(5.4), Inches(2.1))
    l4.fill.solid(); l4.fill.fore_color.rgb = CONTAINER_BG; l4.line.color.rgb = CONTAINER_BORDER; l4.line.width = Pt(1.5)
    tf = l4.text_frame; tf.margin_left = Inches(0.18); tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]; p.text = "Constraint Programming Engine"; p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # CP-SAT Solver Banner
    n_cpsat = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.3), Inches(5.45), Inches(4.3), Inches(0.48))
    n_cpsat.fill.solid(); n_cpsat.fill.fore_color.rgb = RGBColor(30, 27, 75); n_cpsat.line.color.rgb = RGBColor(59, 130, 246); n_cpsat.line.width = Pt(2)
    tf = n_cpsat.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "🧩 Google OR-Tools CP-SAT Solver"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = RGBColor(96, 165, 250)

    # Hard Constraints Box
    n_hard = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.85), Inches(6.15), Inches(2.4), Inches(0.95))
    n_hard.fill.solid(); n_hard.fill.fore_color.rgb = BG_CARD_NAVY; n_hard.line.color.rgb = RGBColor(71, 85, 105); n_hard.line.width = Pt(1)
    tf_h = n_hard.text_frame; tf_h.word_wrap = True; tf_h.margin_left = tf_h.margin_right = Inches(0.1); tf_h.margin_top = Inches(0.08)
    p = tf_h.paragraphs[0]; p.text = "Hard Constraints Validator"; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = CYAN_TEXT; p.space_after = Pt(2)
    p1 = tf_h.add_paragraph(); p1.text = "• NoOverlap (Machines & Tracks)"; p1.font.size = Pt(7.5); p1.font.color.rgb = RGBColor(203, 213, 225); p1.space_after = Pt(2)
    p2 = tf_h.add_paragraph(); p2.text = "• Zero Train-Block Collision"; p2.font.size = Pt(7.5); p2.font.bold = True; p2.font.color.rgb = GREEN_TEXT

    # Soft Constraints Box
    n_soft = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.45), Inches(6.15), Inches(2.45), Inches(0.95))
    n_soft.fill.solid(); n_soft.fill.fore_color.rgb = BG_CARD_NAVY; n_soft.line.color.rgb = RGBColor(71, 85, 105); n_soft.line.width = Pt(1)
    tf_s = n_soft.text_frame; tf_s.word_wrap = True; tf_s.margin_left = tf_s.margin_right = Inches(0.1); tf_s.margin_top = Inches(0.08)
    p = tf_s.paragraphs[0]; p.text = "Soft Constraints & Objective"; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = PURPLE_TEXT; p.space_after = Pt(2)
    p1 = tf_s.add_paragraph(); p1.text = "• Maximize High-Priority Tasks"; p1.font.size = Pt(7.5); p1.font.color.rgb = RGBColor(203, 213, 225); p1.space_after = Pt(2)
    p2 = tf_s.add_paragraph(); p2.text = "• Shadow Block Bonus"; p2.font.size = Pt(7.5); p2.font.bold = True; p2.font.color.rgb = PINK_TEXT

    # =========================================================================
    # 5. DIRECTIONAL CONNECTORS (Exact paths matching reference image)
    # =========================================================================
    # COA / TMS down to Database
    draw_connector(5.4, 1.32, 6.5, 1.6)
    draw_connector(8.2, 1.32, 7.1, 1.6)
    
    # DB down to FastAPI API
    draw_connector(6.8, 2.35, 6.8, 3.28)
    
    # FastAPI to Scorer & Conflict Detector
    draw_connector(7.0, 3.76, 7.2, 4.05)
    draw_connector(7.0, 3.76, 9.35, 4.05)
    
    # FastAPI down to D3, Calendar, PTW
    draw_connector(5.75, 3.55, 1.5, 5.5)
    draw_connector(5.75, 3.55, 3.8, 5.5)
    draw_connector(5.75, 3.76, 6.2, 5.5)
    
    # Detector & Scorer to CP-SAT Solver
    draw_connector(9.35, 4.6, 10.4, 5.45)
    draw_connector(7.2, 4.6, 10.4, 5.45)
    
    # CP-SAT Solver internal links to Hard & Soft Constraints
    draw_connector(9.5, 5.93, 9.0, 6.15)
    draw_connector(11.0, 5.93, 11.5, 6.15)

    output_path = r"c:\Users\kvish\OneDrive\Desktop\railway-planner\Architecture_Diagram_Editable.pptx"
    prs.save(output_path)
    print(f"Architecture Diagram Editable PPTX saved: {output_path}")

if __name__ == "__main__":
    generate_exact_architecture_pptx()
