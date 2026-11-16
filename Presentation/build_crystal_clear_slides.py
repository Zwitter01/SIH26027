import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def apply_slide_dark_background(slide):
    """Sets a rich dark background matching the user's master presentation theme."""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(11, 17, 32) # Dark Slate Navy #0B1120

def add_clean_white_card(slide, left, top, width, height, border_color=None):
    """Creates a high-contrast, pure-white rounded rectangle card."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = RGBColor(255, 255, 255) # Pure White
    
    if border_color is None:
        border_color = RGBColor(203, 213, 225) # Slate-300
    card.line.color.rgb = border_color
    card.line.width = Pt(1.5)
    return card

def build_slide5_feasibility_viability():
    """Builds Slide 5: Operational Feasibility & Compliance with 6 high-contrast white cards."""
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    apply_slide_dark_background(slide)

    # Slide Header
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.733), Inches(0.65))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
    p = tf_t.paragraphs[0]
    p.text = "🛡️ Operational Feasibility & Compliance"
    p.font.name = "Segoe UI"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255) # Crisp White Title

    # ----------------------------------------------------
    # COLUMN 1 (LEFT): Width = 5.7 in, Left = 0.8 in
    # ----------------------------------------------------
    # 1. Feasibility Card
    c1 = add_clean_white_card(slide, Inches(0.8), Inches(1.15), Inches(5.7), Inches(1.88), RGBColor(2, 132, 199))
    tf1 = c1.text_frame; tf1.word_wrap = True; tf1.margin_left = tf1.margin_right = Inches(0.2); tf1.margin_top = Inches(0.12)
    p = tf1.paragraphs[0]; p.text = "⚖️  Feasibility:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = RGBColor(3, 105, 161); p.space_after = Pt(3)
    feasibility_data = [
        ("1. Technical: ", "Powered by Google OR-Tools CP-SAT solver running in <0.06s with sub-100ms latency."),
        ("2. Modularisation: ", "Layered architecture enables phased rollout from 131 km pilot to national scale."),
        ("3. Integration: ", "Non-invasive REST API/webhooks with existing CRIS, TMS, SMMS, and COA servers."),
        ("4. Economic: ", "Zero specialized hardware required; runs on existing Indian Railways cloud servers.")
    ]
    for bold_txt, norm_txt in feasibility_data:
        pt = tf1.add_paragraph(); pt.space_after = Pt(2)
        r_b = pt.add_run(); r_b.text = bold_txt; r_b.font.bold = True; r_b.font.size = Pt(9.8); r_b.font.color.rgb = RGBColor(15, 23, 42)
        r_n = pt.add_run(); r_n.text = norm_txt; r_n.font.size = Pt(9.5); r_n.font.color.rgb = RGBColor(30, 41, 59)

    # 2. Viability Card
    c2 = add_clean_white_card(slide, Inches(0.8), Inches(3.15), Inches(5.7), Inches(1.88), RGBColor(2, 132, 199))
    tf2 = c2.text_frame; tf2.word_wrap = True; tf2.margin_left = tf2.margin_right = Inches(0.2); tf2.margin_top = Inches(0.12)
    p = tf2.paragraphs[0]; p.text = "⚙️  Viability:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = RGBColor(3, 105, 161); p.space_after = Pt(3)
    viability_data = [
        ("1. Regulatory Compliance: ", "Built strictly around Indian Railways G&SR Rules and Block Manuals."),
        ("2. Standardized PTW: ", "Auto-generates statutory Form 351 Joint Disconnection Notices with 3-dept sign-offs."),
        ("3. High Scalability: ", "Extensible across all 17 Zonal Railways and 68,000+ route kilometers."),
        ("4. Operational Safety: ", "Mathematical guarantee of zero train-block collisions eliminates human error.")
    ]
    for bold_txt, norm_txt in viability_data:
        pt = tf2.add_paragraph(); pt.space_after = Pt(2)
        r_b = pt.add_run(); r_b.text = bold_txt; r_b.font.bold = True; r_b.font.size = Pt(9.8); r_b.font.color.rgb = RGBColor(15, 23, 42)
        r_n = pt.add_run(); r_n.text = norm_txt; r_n.font.size = Pt(9.5); r_n.font.color.rgb = RGBColor(30, 41, 59)

    # 3. Challenges & Mitigations Card
    c3 = add_clean_white_card(slide, Inches(0.8), Inches(5.15), Inches(5.7), Inches(1.85), RGBColor(217, 119, 6))
    tf3 = c3.text_frame; tf3.word_wrap = True; tf3.margin_left = tf3.margin_right = Inches(0.2); tf3.margin_top = Inches(0.12)
    p = tf3.paragraphs[0]; p.text = "⚠️  Challenges & Mitigations:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = RGBColor(180, 83, 9); p.space_after = Pt(3)
    challenges_data = [
        ("1. Data Inconsistency: ", "Pydantic schemas sanitize field timestamps, chainage markers, and defect logs."),
        ("2. Machine Conflicts: ", "NoOverlap logic prevents double-booking scarce Track Machines and Tower Wagons."),
        ("3. Emergency Disruption: ", "Dynamic What-If engine reschedules around urgent rail flaws in <150ms.")
    ]
    for bold_txt, norm_txt in challenges_data:
        pt = tf3.add_paragraph(); pt.space_after = Pt(3)
        r_b = pt.add_run(); r_b.text = bold_txt; r_b.font.bold = True; r_b.font.size = Pt(9.8); r_b.font.color.rgb = RGBColor(15, 23, 42)
        r_n = pt.add_run(); r_n.text = norm_txt; r_n.font.size = Pt(9.5); r_n.font.color.rgb = RGBColor(30, 41, 59)

    # ----------------------------------------------------
    # COLUMN 2 (RIGHT): Width = 5.8 in, Left = 6.8 in
    # ----------------------------------------------------
    # 4. Use Cases Card
    c4 = add_clean_white_card(slide, Inches(6.8), Inches(1.15), Inches(5.8), Inches(1.88), RGBColor(2, 132, 199))
    tf4 = c4.text_frame; tf4.word_wrap = True; tf4.margin_left = tf4.margin_right = Inches(0.2); tf4.margin_top = Inches(0.12)
    p = tf4.paragraphs[0]; p.text = "🚆  Use Cases:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = RGBColor(3, 105, 161); p.space_after = Pt(3)
    usecases_data = [
        ("1. Section Controllers: ", "1-click automated corridor block plans replacing 3–5 days of manual phone calls."),
        ("2. Civil/P-Way (TMS): ", "Prioritizes urgent IMR rail flaw welds and deep screening tamping blocks."),
        ("3. Traction (TDMS): ", "Synchronizes OHE cantilever overhauls and power isolation with track closures."),
        ("4. S&T (SMMS): ", "Co-schedules axle counter testing and point machine calibration into Mega Blocks.")
    ]
    for bold_txt, norm_txt in usecases_data:
        pt = tf4.add_paragraph(); pt.space_after = Pt(2)
        r_b = pt.add_run(); r_b.text = bold_txt; r_b.font.bold = True; r_b.font.size = Pt(9.8); r_b.font.color.rgb = RGBColor(15, 23, 42)
        r_n = pt.add_run(); r_n.text = norm_txt; r_n.font.size = Pt(9.5); r_n.font.color.rgb = RGBColor(30, 41, 59)

    # 5. Operational Potential Card
    c5 = add_clean_white_card(slide, Inches(6.8), Inches(3.15), Inches(5.8), Inches(1.88), RGBColor(22, 163, 74))
    tf5 = c5.text_frame; tf5.word_wrap = True; tf5.margin_left = tf5.margin_right = Inches(0.2); tf5.margin_top = Inches(0.12)
    p = tf5.paragraphs[0]; p.text = "📊  Operational Potential:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = RGBColor(21, 128, 61); p.space_after = Pt(3)
    potential_data = [
        ("1. Availability Gain: ", "Elevates corridor asset availability from 91.2% to 96.6%+, unlocking new paths."),
        ("2. Downtime Compression: ", "Multi-department Shadow Blocks cut cumulative closures by up to 40%."),
        ("3. Punctuality Boost: ", "Eliminates cascading train detentions and unplanned speed restrictions."),
        ("4. Digital Governance: ", "100% digital audit trail from maintenance requisition to final section clearance.")
    ]
    for bold_txt, norm_txt in potential_data:
        pt = tf5.add_paragraph(); pt.space_after = Pt(2)
        r_b = pt.add_run(); r_b.text = bold_txt; r_b.font.bold = True; r_b.font.size = Pt(9.8); r_b.font.color.rgb = RGBColor(15, 23, 42)
        r_n = pt.add_run(); r_n.text = norm_txt; r_n.font.size = Pt(9.5); r_n.font.color.rgb = RGBColor(30, 41, 59)

    # 6. Supporting Facts Card (Prominent Highlight Card)
    c6 = add_clean_white_card(slide, Inches(6.8), Inches(5.15), Inches(5.8), Inches(1.85), RGBColor(14, 165, 233))
    c6.line.width = Pt(2.0)
    tf6 = c6.text_frame; tf6.word_wrap = True; tf6.margin_left = tf6.margin_right = Inches(0.2); tf6.margin_top = Inches(0.12)
    p = tf6.paragraphs[0]; p.text = "⭐  Supporting Facts for Feasibility & Viability"; p.font.size = Pt(12.5); p.font.bold = True; p.font.color.rgb = RGBColor(2, 132, 199); p.space_after = Pt(4)
    facts_data = [
        ("➔ CAG Railway Audit: ", "Studies indicate up to 30–35% of sanctioned blocks are underutilized due to decentralized manual coordination between departments."),
        ("➔ Network Scale: ", "Coordinates across 68,000+ route km & 13,000+ daily trains, recovering thousands of train delay hours annually."),
        ("➔ Proven Benchmark: ", "NDLS–ALJN pilot achieved 100% critical task completion with 4 Mega Blocks in under 0.1 seconds.")
    ]
    for bold_txt, norm_txt in facts_data:
        pt = tf6.add_paragraph(); pt.space_after = Pt(3)
        r_b = pt.add_run(); r_b.text = bold_txt; r_b.font.bold = True; r_b.font.size = Pt(9.6); r_b.font.color.rgb = RGBColor(15, 23, 42)
        r_n = pt.add_run(); r_n.text = norm_txt; r_n.font.size = Pt(9.3); r_n.font.color.rgb = RGBColor(30, 41, 59)

    out_path = r"Presentation\Slide5_Feasibility_Editable.pptx"
    prs.save(out_path)
    # Also save to root directory for easy access
    prs.save(r"Slide5_Feasibility_Editable.pptx")
    print(f"[+] Slide 5 generated successfully: {out_path}")


def build_slide6_impact_and_benefits():
    """Builds Slide 6: Benefits of AI Block Planning / Impact with clean high-contrast white cards."""
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    apply_slide_dark_background(slide)

    # Slide Header
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.733), Inches(0.65))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = 0
    p = tf_t.paragraphs[0]
    p.text = "🎯 Impact and Benefits of AI Block Planning"
    p.font.name = "Segoe UI"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255) # Crisp White Title

    # ----------------------------------------------------
    # COLUMN 1 (LEFT): Width = 5.7 in, Left = 0.8 in
    # ----------------------------------------------------
    # 1. Top Card: 5 Pillars of Benefits
    c_left_top = add_clean_white_card(slide, Inches(0.8), Inches(1.15), Inches(5.7), Inches(2.35), RGBColor(234, 88, 12))
    tf_lt = c_left_top.text_frame; tf_lt.word_wrap = True; tf_lt.margin_left = tf_lt.margin_right = Inches(0.2); tf_lt.margin_top = Inches(0.12)
    p = tf_lt.paragraphs[0]; p.text = "🚆  Benefits of AI Block Planning Architecture"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = RGBColor(194, 65, 12); p.space_after = Pt(8)

    # Inner Pill Row 1
    p_pills1 = tf_lt.add_paragraph(); p_pills1.space_after = Pt(4)
    p_pills1.text = "🔵 Operational  |  🔺 Economical  |  ⚡ Technological"
    p_pills1.font.bold = True; p_pills1.font.size = Pt(11); p_pills1.font.color.rgb = RGBColor(3, 105, 161)

    # Inner Pill Row 2
    p_pills2 = tf_lt.add_paragraph(); p_pills2.space_after = Pt(8)
    p_pills2.text = "🛡️ Safety & Social  |  🌿 Environmental"
    p_pills2.font.bold = True; p_pills2.font.size = Pt(11); p_pills2.font.color.rgb = RGBColor(21, 128, 61)

    p_desc = tf_lt.add_paragraph()
    p_desc.text = "Delivers unified multi-dimensional returns across corridor asset availability, track worker safety, locomotive fuel savings, and punctuality assurance."
    p_desc.font.size = Pt(9.8); p_desc.font.color.rgb = RGBColor(71, 85, 105)

    # 2. Bottom Card: Potential Impact on Target Audience (WHITE CARD - PREVIOUSLY INVISIBLE!)
    c_left_bottom = add_clean_white_card(slide, Inches(0.8), Inches(3.62), Inches(5.7), Inches(3.38), RGBColor(2, 132, 199))
    tf_lb = c_left_bottom.text_frame; tf_lb.word_wrap = True; tf_lb.margin_left = tf_lb.margin_right = Inches(0.2); tf_lb.margin_top = Inches(0.14)
    p = tf_lb.paragraphs[0]; p.text = "👥  Potential Impact on the Target Audience:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = RGBColor(2, 132, 199); p.space_after = Pt(6)

    audience_data = [
        ("• Section Controllers: ", "1-click automated corridor block plans replacing 3–5 days of chaotic manual phone calls."),
        ("• Maintenance Field Staff: ", "Guaranteed synchronized Mega Blocks with zero last-minute cancellations or gang idle time."),
        ("• Passenger Operations: ", "Zero delay for Rajdhani / Vande Bharat trains via strict 15-min statutory headway buffers."),
        ("• Freight Operations: ", "Frees dedicated nocturnal track paths, accelerating goods rake turnaround and revenue.")
    ]
    for bold_txt, norm_txt in audience_data:
        pt = tf_lb.add_paragraph(); pt.space_after = Pt(4)
        r_b = pt.add_run(); r_b.text = bold_txt; r_b.font.bold = True; r_b.font.size = Pt(10.2); r_b.font.color.rgb = RGBColor(15, 23, 42)
        r_n = pt.add_run(); r_n.text = norm_txt; r_n.font.size = Pt(9.8); r_n.font.color.rgb = RGBColor(30, 41, 59)

    # ----------------------------------------------------
    # COLUMN 2 (RIGHT): 5 Evenly Stacked White Cards
    # Width = 5.8 in, Left = 6.8 in, Height = 1.10 in each, Gap = 0.08 in
    # ----------------------------------------------------
    right_cards = [
        ("🔵 Operational:", [
            "• Increases corridor asset availability from 91.2% to 96.6%+.",
            "• Multi-department Shadow Blocks cut cumulative track closures by up to 40%."
        ], RGBColor(2, 132, 199)),

        ("🔺 Economical:", [
            "• Saves crores annually by eliminating locomotive idling fuel and overtime gang hours.",
            "• Accelerates freight rake turnaround, boosting network freight revenue paths."
        ], RGBColor(225, 29, 72)),

        ("⚡ Technological:", [
            "• Pioneers Google OR-Tools CP-SAT optimization within Indian Railways CRIS systems.",
            "• Sub-100ms algorithmic latency enables live What-If constraint recalculations."
        ], RGBColor(147, 51, 234)),

        ("🛡️ Safety & Social:", [
            "• Prioritizes urgent IMR/OBS rail flaws and OHE defects to prevent derailments.",
            "• Eliminates unexpected passenger train detentions at outer signals."
        ], RGBColor(202, 138, 4)),

        ("🌿 Environmental:", [
            "• Reduces diesel locomotive idling at red signals, cutting direct CO2 emissions.",
            "• Optimizes train momentum, lowering traction power peak surge demands."
        ], RGBColor(22, 163, 74))
    ]

    start_y = 1.15
    card_h = 1.10
    gap = 0.08

    for i, (head, points, b_col) in enumerate(right_cards):
        y_pos = start_y + i * (card_h + gap)
        c_right = add_clean_white_card(slide, Inches(6.8), Inches(y_pos), Inches(5.8), Inches(card_h), b_col)
        tf_r = c_right.text_frame; tf_r.word_wrap = True; tf_r.margin_left = tf_r.margin_right = Inches(0.18); tf_r.margin_top = Inches(0.08)
        
        p = tf_r.paragraphs[0]; p.text = head; p.font.size = Pt(11.5); p.font.bold = True; p.font.color.rgb = b_col; p.space_after = Pt(2)
        for pt_txt in points:
            p_pt = tf_r.add_paragraph(); p_pt.space_after = Pt(1)
            p_pt.text = pt_txt; p_pt.font.size = Pt(9.4); p_pt.font.color.rgb = RGBColor(30, 41, 59)

    out_path = r"Presentation\Slide6_Impact_and_Benefits_Editable.pptx"
    prs.save(out_path)
    # Also save to root directory for easy access
    prs.save(r"Slide6_Impact_and_Benefits_Editable.pptx")
    print(f"[+] Slide 6 generated successfully: {out_path}")


if __name__ == "__main__":
    build_slide5_feasibility_viability()
    build_slide6_impact_and_benefits()
