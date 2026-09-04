import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR

def generate_clean_white_architecture():
    prs = Presentation()
    # 16:9 Widescreen slide
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Color Constants
    DARK_TEXT = RGBColor(15, 23, 42)       # #0f172a Black/Dark Slate Font
    TEXT_MUTED = RGBColor(71, 85, 105)     # #475569
    CARD_BG_WHITE = RGBColor(255, 255, 255)# Pure White Background for all small blocks
    
    CONTAINER_BG = RGBColor(241, 245, 249) # #f1f5f9 Light Gray container layer
    CONTAINER_BORDER = RGBColor(148, 163, 184) # #94a3b8
    
    CYAN_BORDER = RGBColor(2, 132, 199)    # #0284c7
    GREEN_BORDER = RGBColor(22, 163, 74)   # #16a34a
    GREEN_TEXT = RGBColor(22, 163, 74)
    
    ORANGE_BORDER = RGBColor(234, 88, 12)  # #ea580c
    PURPLE_BORDER = RGBColor(147, 51, 234) # #9333ea
    PINK_TEXT = RGBColor(219, 39, 119)     # #db2777
    BLUE_BORDER = RGBColor(37, 99, 235)    # #2563eb
    
    ARROW_COLOR = RGBColor(2, 132, 199)

    def draw_arrow(x1, y1, x2, y2):
        conn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
        conn.line.color.rgb = ARROW_COLOR
        conn.line.width = Pt(2)

    # =========================================================================
    # 1. LAYER 1: DATA & INGESTION LAYER (Top Center)
    # =========================================================================
    # Train Graphic Badge Top-Left outside
    tr_badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.2), Inches(0.8), Inches(1.6), Inches(0.5))
    tr_badge.fill.solid(); tr_badge.fill.fore_color.rgb = CARD_BG_WHITE
    tr_badge.line.color.rgb = CYAN_BORDER; tr_badge.line.width = Pt(1.5)
    tf_tr = tr_badge.text_frame; tf_tr.word_wrap = True; tf_tr.margin_top = Inches(0.08)
    p = tf_tr.paragraphs[0]; p.text = "🚆 🚋  IR LIVE"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # Layer 1 Container Box (Light Gray)
    l1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.9), Inches(0.35), Inches(5.9), Inches(2.2))
    l1.fill.solid(); l1.fill.fore_color.rgb = CONTAINER_BG; l1.line.color.rgb = CONTAINER_BORDER; l1.line.width = Pt(1.5)
    tf = l1.text_frame; tf.margin_left = Inches(0.18); tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "Data & Ingestion Layer"; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # COA Feed Node (White BG, Black Text, Cyan Border)
    n_coa = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.15), Inches(0.75), Inches(2.55), Inches(0.55))
    n_coa.fill.solid(); n_coa.fill.fore_color.rgb = CARD_BG_WHITE; n_coa.line.color.rgb = CYAN_BORDER; n_coa.line.width = Pt(1.5)
    tf = n_coa.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.1)
    p = tf.paragraphs[0]; p.text = "📈 COA Real-Time Train Feed"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(9.5); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # TMS Node (White BG, Black Text, Cyan Border)
    n_tms = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.0), Inches(0.75), Inches(2.6), Inches(0.55))
    n_tms.fill.solid(); n_tms.fill.fore_color.rgb = CARD_BG_WHITE; n_tms.line.color.rgb = CYAN_BORDER; n_tms.line.width = Pt(1.5)
    tf = n_tms.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.1)
    p = tf.paragraphs[0]; p.text = "⚙️ TMS / SMMS / TDMS Task APIs"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(9.5); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # Database Cylinder Node (Cyan Blue with White Text for contrast cylinder shape)
    n_db = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.1), Inches(1.55), Inches(3.5), Inches(0.75))
    n_db.fill.solid(); n_db.fill.fore_color.rgb = RGBColor(2, 132, 199); n_db.line.color.rgb = RGBColor(3, 105, 161); n_db.line.width = Pt(2)
    tf_db = n_db.text_frame; tf_db.word_wrap = True; tf_db.margin_top = Inches(0.08)
    p = tf_db.paragraphs[0]; p.text = "🗄️ SQLite / PostgreSQL 🐘"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = RGBColor(255, 255, 255)
    p_sub = tf_db.add_paragraph(); p_sub.text = "(WAL Mode Enabled)"; p_sub.alignment = PP_ALIGN.CENTER; p_sub.font.size = Pt(8.5); p_sub.font.color.rgb = RGBColor(224, 242, 254)

    # =========================================================================
    # 2. LAYER 2: FASTAPI SERVICE LAYER (Middle)
    # =========================================================================
    # Layer 2 Container Box (Light Gray)
    l2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(2.9), Inches(5.1), Inches(1.9))
    l2.fill.solid(); l2.fill.fore_color.rgb = CONTAINER_BG; l2.line.color.rgb = CONTAINER_BORDER; l2.line.width = Pt(1.5)
    tf = l2.text_frame; tf.margin_left = Inches(0.18); tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "FastAPI Service Layer"; p.font.size = Pt(10.5); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # FastAPI API Bar (White BG, Black Text, Green Border)
    n_fapi = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.75), Inches(3.28), Inches(2.7), Inches(0.5))
    n_fapi.fill.solid(); n_fapi.fill.fore_color.rgb = CARD_BG_WHITE; n_fapi.line.color.rgb = GREEN_BORDER; n_fapi.line.width = Pt(2)
    tf = n_fapi.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "⚡ FastAPI Async REST API"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # Priority Scorer Engine (White BG, Black Text)
    n_sc = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.3), Inches(4.05), Inches(1.85), Inches(0.55))
    n_sc.fill.solid(); n_sc.fill.fore_color.rgb = CARD_BG_WHITE; n_sc.line.color.rgb = CONTAINER_BORDER; n_sc.line.width = Pt(1.2)
    tf = n_sc.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]; p.text = "Priority Scorer Engine"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(9); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # Conflict Detector (White BG, Black Text)
    n_dt = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.35), Inches(4.05), Inches(2.05), Inches(0.55))
    n_dt.fill.solid(); n_dt.fill.fore_color.rgb = CARD_BG_WHITE; n_dt.line.color.rgb = CONTAINER_BORDER; n_dt.line.width = Pt(1.2)
    tf = n_dt.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "Spatial-Temporal Conflict\nDetector"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # =========================================================================
    # 3. LAYER 3: PRESENTATION & DISPATCH LAYER (Bottom-Left)
    # =========================================================================
    # Layer 3 Container Box (Light Gray)
    l3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.3), Inches(5.15), Inches(7.1), Inches(1.2))
    l3.fill.solid(); l3.fill.fore_color.rgb = CONTAINER_BG; l3.line.color.rgb = CONTAINER_BORDER; l3.line.width = Pt(1.5)
    tf = l3.text_frame; tf.margin_left = Inches(0.18); tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]; p.text = "Presentation & Dispatch Layer"; p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # D3 Stringline Chart Card (White BG, Black Text, Orange Border)
    n_d3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(5.5), Inches(2.1), Inches(0.6))
    n_d3.fill.solid(); n_d3.fill.fore_color.rgb = CARD_BG_WHITE; n_d3.line.color.rgb = ORANGE_BORDER; n_d3.line.width = Pt(1.5)
    tf = n_d3.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]; p.text = "🟠 D3.js Stringline Chart"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # Calendar Card (White BG, Black Text, Cyan Border)
    n_cal = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.8), Inches(5.5), Inches(2.2), Inches(0.6))
    n_cal.fill.solid(); n_cal.fill.fore_color.rgb = CARD_BG_WHITE; n_cal.line.color.rgb = CYAN_BORDER; n_cal.line.width = Pt(1.5)
    tf = n_cal.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "📅 Weekly Calendar &\nGantt"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # PTW Notice Card (White BG, Black Text, Purple Border)
    n_ptw = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.2), Inches(5.5), Inches(2.0), Inches(0.6))
    n_ptw.fill.solid(); n_ptw.fill.fore_color.rgb = CARD_BG_WHITE; n_ptw.line.color.rgb = PURPLE_BORDER; n_ptw.line.width = Pt(1.5)
    tf = n_ptw.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]; p.text = "📄 Form 351 PTW Notice"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # =========================================================================
    # 4. LAYER 4: CONSTRAINT PROGRAMMING ENGINE (Bottom-Right)
    # =========================================================================
    # Layer 4 Container Box (Light Gray)
    l4 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.65), Inches(5.15), Inches(5.4), Inches(2.15))
    l4.fill.solid(); l4.fill.fore_color.rgb = CONTAINER_BG; l4.line.color.rgb = CONTAINER_BORDER; l4.line.width = Pt(1.5)
    tf = l4.text_frame; tf.margin_left = Inches(0.18); tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]; p.text = "Constraint Programming Engine"; p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = DARK_TEXT

    # CP-SAT Solver Banner (White BG, Blue Border, Dark Blue Bold Text)
    n_cpsat = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.3), Inches(5.45), Inches(4.3), Inches(0.5))
    n_cpsat.fill.solid(); n_cpsat.fill.fore_color.rgb = CARD_BG_WHITE; n_cpsat.line.color.rgb = BLUE_BORDER; n_cpsat.line.width = Pt(2)
    tf = n_cpsat.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "🧩 Google OR-Tools CP-SAT Solver"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(10); p.font.bold = True; p.font.color.rgb = BLUE_BORDER

    # Hard Constraints Box (White BG, Dark Text with Green bullet)
    n_hard = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.85), Inches(6.15), Inches(2.4), Inches(0.95))
    n_hard.fill.solid(); n_hard.fill.fore_color.rgb = CARD_BG_WHITE; n_hard.line.color.rgb = CONTAINER_BORDER; n_hard.line.width = Pt(1.2)
    tf_h = n_hard.text_frame; tf_h.word_wrap = True; tf_h.margin_left = tf_h.margin_right = Inches(0.1); tf_h.margin_top = Inches(0.08)
    p = tf_h.paragraphs[0]; p.text = "Hard Constraints Validator"; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = CYAN_BORDER; p.space_after = Pt(2)
    p1 = tf_h.add_paragraph(); p1.text = "• NoOverlap (Machines & Tracks)"; p1.font.size = Pt(7.5); p1.font.color.rgb = DARK_TEXT; p1.space_after = Pt(2)
    p2 = tf_h.add_paragraph(); p2.text = "• Zero Train-Block Collision"; p2.font.size = Pt(7.5); p2.font.bold = True; p2.font.color.rgb = GREEN_TEXT

    # Soft Constraints Box (White BG, Dark Text with Pink bullet)
    n_soft = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.45), Inches(6.15), Inches(2.45), Inches(0.95))
    n_soft.fill.solid(); n_soft.fill.fore_color.rgb = CARD_BG_WHITE; n_soft.line.color.rgb = CONTAINER_BORDER; n_soft.line.width = Pt(1.2)
    tf_s = n_soft.text_frame; tf_s.word_wrap = True; tf_s.margin_left = tf_s.margin_right = Inches(0.1); tf_s.margin_top = Inches(0.08)
    p = tf_s.paragraphs[0]; p.text = "Soft Constraints & Objective"; p.font.size = Pt(8.5); p.font.bold = True; p.font.color.rgb = PURPLE_BORDER; p.space_after = Pt(2)
    p1 = tf_s.add_paragraph(); p1.text = "• Maximize High-Priority Tasks"; p1.font.size = Pt(7.5); p1.font.color.rgb = DARK_TEXT; p1.space_after = Pt(2)
    p2 = tf_s.add_paragraph(); p2.text = "• Shadow Block Bonus"; p2.font.size = Pt(7.5); p2.font.bold = True; p2.font.color.rgb = PINK_TEXT

    # =========================================================================
    # 5. DIRECTIONAL CONNECTORS (Exact paths matching reference image)
    # =========================================================================
    draw_arrow(5.4, 1.3, 6.5, 1.55)     # COA to DB
    draw_arrow(8.2, 1.3, 7.1, 1.55)     # TMS to DB
    draw_arrow(6.8, 2.3, 6.8, 3.28)     # DB to FastAPI
    draw_arrow(7.0, 3.78, 7.2, 4.05)    # FastAPI to Scorer
    draw_arrow(7.0, 3.78, 9.35, 4.05)   # FastAPI to Detector
    draw_arrow(5.75, 3.55, 1.5, 5.5)    # FastAPI to D3
    draw_arrow(5.75, 3.55, 3.8, 5.5)    # FastAPI to Calendar
    draw_arrow(5.75, 3.78, 6.2, 5.5)    # FastAPI to PTW
    draw_arrow(9.35, 4.6, 10.4, 5.45)   # Detector to CP-SAT
    draw_arrow(7.2, 4.6, 10.4, 5.45)    # Scorer to CP-SAT
    draw_arrow(9.5, 5.95, 9.0, 6.15)    # CP-SAT to Hard
    draw_arrow(11.0, 5.95, 11.5, 6.15)  # CP-SAT to Soft

    output_path = r"c:\Users\kvish\OneDrive\Desktop\railway-planner\Architecture_Diagram_WhiteCards_Editable.pptx"
    prs.save(output_path)
    print(f"White Cards Architecture PPTX created: {output_path}")

if __name__ == "__main__":
    generate_clean_white_architecture()
