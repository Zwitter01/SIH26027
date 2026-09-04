import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.shapes import MSO_CONNECTOR

def generate_impact_and_benefits_slide():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Color Palette
    DARK_BLUE = RGBColor(15, 23, 42)
    TEXT_DARK = RGBColor(30, 41, 59)
    TEXT_MUTED = RGBColor(71, 85, 105)
    
    COLOR_YELLOW = RGBColor(254, 240, 138)  # Social/Safety
    BORDER_YELLOW = RGBColor(202, 138, 4)
    
    COLOR_BLUE = RGBColor(224, 242, 254)    # Operational
    BORDER_BLUE = RGBColor(2, 132, 199)
    
    COLOR_GREEN = RGBColor(220, 252, 231)   # Environmental
    BORDER_GREEN = RGBColor(22, 163, 74)
    
    COLOR_RED = RGBColor(255, 228, 230)     # Economical
    BORDER_RED = RGBColor(225, 29, 72)
    
    COLOR_PURPLE = RGBColor(243, 232, 255)  # Technological
    BORDER_PURPLE = RGBColor(147, 51, 234)

    # 1. Slide Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.7), Inches(0.7))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = "IMPACT AND BENEFITS"
    p_title.font.name = "Segoe UI"
    p_title.font.size = Pt(28)
    p_title.font.bold = True
    p_title.font.color.rgb = DARK_BLUE

    # ----------------------------------------------------
    # LEFT HALF: BENEFITS FLOWCHART / TREE DIAGRAM
    # ----------------------------------------------------
    # Root Box: Benefits of the solution
    root_shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(1.8), Inches(1.15), Inches(3.2), Inches(0.65)
    )
    root_shape.fill.solid()
    root_shape.fill.fore_color.rgb = RGBColor(254, 215, 170) # Orange-amber
    root_shape.line.color.rgb = RGBColor(234, 88, 12)
    root_shape.line.width = Pt(2)
    tf_root = root_shape.text_frame
    p_r = tf_root.paragraphs[0]
    p_r.text = "🚆 Benefits of AI Block Planning"
    p_r.alignment = PP_ALIGN.CENTER
    p_r.font.name = "Segoe UI"
    p_r.font.size = Pt(13)
    p_r.font.bold = True
    p_r.font.color.rgb = DARK_BLUE

    # 5 Branch Boxes (Row 1: 3 boxes, Row 2: 2 boxes)
    # 1. Operational
    b1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(2.2), Inches(1.7), Inches(0.65))
    b1.fill.solid(); b1.fill.fore_color.rgb = COLOR_BLUE; b1.line.color.rgb = BORDER_BLUE; b1.line.width = Pt(1.5)
    p = b1.text_frame.paragraphs[0]; p.text = "⚙️ Operational"; p.alignment = PP_ALIGN.CENTER
    p.font.name = "Segoe UI"; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # 2. Economical
    b2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.55), Inches(2.2), Inches(1.7), Inches(0.65))
    b2.fill.solid(); b2.fill.fore_color.rgb = COLOR_RED; b2.line.color.rgb = BORDER_RED; b2.line.width = Pt(1.5)
    p = b2.text_frame.paragraphs[0]; p.text = "💰 Economical"; p.alignment = PP_ALIGN.CENTER
    p.font.name = "Segoe UI"; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # 3. Technological
    b3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.5), Inches(2.2), Inches(1.7), Inches(0.65))
    b3.fill.solid(); b3.fill.fore_color.rgb = COLOR_PURPLE; b3.line.color.rgb = BORDER_PURPLE; b3.line.width = Pt(1.5)
    p = b3.text_frame.paragraphs[0]; p.text = "⚡ Technological"; p.alignment = PP_ALIGN.CENTER
    p.font.name = "Segoe UI"; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # 4. Social & Safety
    b4 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.55), Inches(3.05), Inches(1.7), Inches(0.65))
    b4.fill.solid(); b4.fill.fore_color.rgb = COLOR_YELLOW; b4.line.color.rgb = BORDER_YELLOW; b4.line.width = Pt(1.5)
    p = b4.text_frame.paragraphs[0]; p.text = "🛡️ Safety & Social"; p.alignment = PP_ALIGN.CENTER
    p.font.name = "Segoe UI"; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # 5. Environmental
    b5 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.55), Inches(3.05), Inches(1.7), Inches(0.65))
    b5.fill.solid(); b5.fill.fore_color.rgb = COLOR_GREEN; b5.line.color.rgb = BORDER_GREEN; b5.line.width = Pt(1.5)
    p = b5.text_frame.paragraphs[0]; p.text = "🌱 Environmental"; p.alignment = PP_ALIGN.CENTER
    p.font.name = "Segoe UI"; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # Connectors (Tree lines)
    def add_tree_line(x1, y1, x2, y2):
        conn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
        conn.line.color.rgb = RGBColor(100, 116, 139)
        conn.line.width = Pt(1.5)

    add_tree_line(3.4, 1.8, 3.4, 2.0)
    add_tree_line(1.45, 2.0, 5.35, 2.0)
    add_tree_line(1.45, 2.0, 1.45, 2.2)
    add_tree_line(3.4, 2.0, 3.4, 2.2)
    add_tree_line(5.35, 2.0, 5.35, 2.2)

    # ----------------------------------------------------
    # BOTTOM-LEFT: POTENTIAL IMPACT ON TARGET AUDIENCE
    # ----------------------------------------------------
    impact_box = slide.shapes.add_textbox(Inches(0.6), Inches(3.9), Inches(5.8), Inches(3.2))
    tf_impact = impact_box.text_frame
    tf_impact.word_wrap = True
    tf_impact.margin_left = tf_impact.margin_right = tf_impact.margin_top = tf_impact.margin_bottom = 0

    p_imp_title = tf_impact.paragraphs[0]
    p_imp_title.text = "❖ Potential Impact on the Target Audience:"
    p_imp_title.font.name = "Segoe UI"
    p_imp_title.font.size = Pt(15)
    p_imp_title.font.bold = True
    p_imp_title.font.color.rgb = DARK_BLUE
    p_imp_title.space_after = Pt(6)

    audience_points = [
        ("• Section Controllers: ", "1-click automated corridor block plans replacing 3–5 days of manual phone calls."),
        ("• Maintenance Field Staff: ", "Guaranteed synchronized Mega Blocks with zero last-minute cancellations."),
        ("• Passenger Operations: ", "Zero delay for Rajdhani / Vande Bharat trains via strict 15-min headway buffers."),
        ("• Freight Operations: ", "Frees dedicated nocturnal track paths, boosting goods rake turnaround time.")
    ]
    for bold_t, norm_t in audience_points:
        p_pt = tf_impact.add_paragraph()
        p_pt.space_after = Pt(4)
        r_b = p_pt.add_run(); r_b.text = bold_t; r_b.font.name = "Segoe UI"; r_b.font.size = Pt(11.5); r_b.font.bold = True; r_b.font.color.rgb = DARK_BLUE
        r_n = p_pt.add_run(); r_n.text = norm_t; r_n.font.name = "Segoe UI"; r_n.font.size = Pt(11.5); r_n.font.color.rgb = TEXT_DARK

    # ----------------------------------------------------
    # RIGHT HALF: DETAILED BREAKDOWN OF BENEFITS
    # ----------------------------------------------------
    right_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.1), Inches(5.8), Inches(6.0))
    tf_right = right_box.text_frame
    tf_right.word_wrap = True
    tf_right.margin_left = tf_right.margin_right = tf_right.margin_top = tf_right.margin_bottom = 0

    sections_data = [
        ("⚙️ Operational:", [
            "Increases corridor asset availability from 91.2% to 96.6%+.",
            "Multi-department Shadow Blocks cut cumulative track closures by up to 40%."
        ]),
        ("💰 Economical:", [
            "Saves crores annually by eliminating locomotive idling fuel and overtime gang hours.",
            "Accelerates freight rake turnaround, boosting freight revenue paths."
        ]),
        ("⚡ Technological:", [
            "Pioneers Google OR-Tools CP-SAT optimization within Indian Railways CRIS systems.",
            "Sub-100ms algorithmic latency enables live What-If constraint recalculations."
        ]),
        ("🛡️ Safety & Social:", [
            "Prioritizes urgent IMR/OBS rail flaws and OHE defects to prevent derailments.",
            "Eliminates unexpected passenger train detentions at outer signals."
        ]),
        ("🌱 Environmental:", [
            "Reduces diesel locomotive idling at red signals, cutting direct CO2 emissions.",
            "Optimizes train momentum, lowering traction power peak surge demands."
        ])
    ]

    is_first = True
    for sec_title, bullets in sections_data:
        p_h = tf_right.paragraphs[0] if is_first else tf_right.add_paragraph()
        is_first = False
        p_h.text = sec_title
        p_h.font.name = "Segoe UI"
        p_h.font.size = Pt(14)
        p_h.font.bold = True
        p_h.font.color.rgb = DARK_BLUE
        p_h.space_before = Pt(0 if is_first else 6)
        p_h.space_after = Pt(2)

        for b in bullets:
            p_b = tf_right.add_paragraph()
            p_b.text = "• " + b
            p_b.font.name = "Segoe UI"
            p_b.font.size = Pt(11)
            p_b.font.color.rgb = TEXT_DARK
            p_b.space_after = Pt(2)

    output_path = r"c:\Users\kvish\OneDrive\Desktop\railway-planner\Slide6_Impact_and_Benefits_Editable.pptx"
    prs.save(output_path)
    print(f"Slide 6 editable PPTX saved: {output_path}")

if __name__ == "__main__":
    generate_impact_and_benefits_slide()
