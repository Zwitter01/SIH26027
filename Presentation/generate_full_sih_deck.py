import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_full_sih_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors
    DARK_BLUE = RGBColor(15, 23, 42)
    NAVY_ACCENT = RGBColor(2, 132, 199)
    TEXT_DARK = RGBColor(30, 41, 59)
    CARD_BG_LIGHT = RGBColor(248, 250, 252)
    CARD_BORDER_BLUE = RGBColor(2, 132, 199)

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    t_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(2.2))
    tf1 = t_box.text_frame; tf1.word_wrap = True
    p = tf1.paragraphs[0]; p.text = "AI-Powered Automatic Block Planning to Maximize Asset Availability for Train Operations on Indian Railways"
    p.font.name = "Segoe UI"; p.font.size = Pt(26); p.font.bold = True; p.font.color.rgb = DARK_BLUE; p.space_after = Pt(12)
    p_sub = tf1.add_paragraph(); p_sub.text = "Smart India Hackathon (SIH 2026) • Problem Statement ID: SIH26027 • Ministry of Railways"
    p_sub.font.name = "Segoe UI"; p_sub.font.size = Pt(14); p_sub.font.color.rgb = NAVY_ACCENT; p_sub.font.bold = True

    card1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(3.6), Inches(5.4), Inches(3.0))
    card1.fill.solid(); card1.fill.fore_color.rgb = CARD_BG_LIGHT; card1.line.color.rgb = CARD_BORDER_BLUE; card1.line.width = Pt(1.5)
    tf_c1 = card1.text_frame; tf_c1.word_wrap = True
    p = tf_c1.paragraphs[0]; p.text = "📌 Project Overview"; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT; p.space_after = Pt(8)
    for k, v in [
        ("Theme: ", "Infrastructure & Transportation / Smart Vehicles"),
        ("Category: ", "Software Edition"),
        ("Organization: ", "Ministry of Railways (Indian Railways)"),
        ("Target Corridor: ", "NDLS–ALJN Mainline (131.2 km High-Density Network)")
    ]:
        p_pt = tf_c1.add_paragraph(); p_pt.space_after = Pt(4)
        r_b = p_pt.add_run(); r_b.text = k; r_b.font.bold = True; r_b.font.size = Pt(11); r_b.font.color.rgb = DARK_BLUE
        r_n = p_pt.add_run(); r_n.text = v; r_n.font.size = Pt(11); r_n.font.color.rgb = TEXT_DARK

    card2 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.6), Inches(5.5), Inches(3.0))
    card2.fill.solid(); card2.fill.fore_color.rgb = CARD_BG_LIGHT; card2.line.color.rgb = CARD_BORDER_BLUE; card2.line.width = Pt(1.5)
    tf_c2 = card2.text_frame; tf_c2.word_wrap = True
    p = tf_c2.paragraphs[0]; p.text = "👥 Team Details (Team CODEX)"; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT; p.space_after = Pt(8)
    for m in [
        "• Team Leader: [Name] (Optimization Core & CP-SAT Engine)",
        "• Member 2: [Name] (Frontend & D3.js Visualizations)",
        "• Member 3: [Name] (Data Integration & Database Architect)",
        "• Member 4: [Name] (Railways Domain & Operations Analyst)",
        "• Member 5: [Name] (UI/UX & Quality Assurance)",
        "• Member 6: [Name] (Documentation & Compliance)"
    ]:
        p_pt = tf_c2.add_paragraph(); p_pt.text = m; p_pt.font.size = Pt(10.5); p_pt.font.color.rgb = TEXT_DARK; p_pt.space_after = Pt(2)

    # =========================================================================
    # SLIDE 2: PROBLEM UNDERSTANDING & GAPS
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    t_box = slide2.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.7))
    p = t_box.text_frame.paragraphs[0]; p.text = "PROBLEM UNDERSTANDING & OPERATIONAL GAPS"; p.font.size = Pt(26); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    p_cards = [
        ("1. Isolated Departmental Silos", "• Engineering (TMS), Traction (TDMS), and Signalling (SMMS) plan maintenance independently.\n• Corridor availability checked via manual phone calls against COA timetable.\n• Disconnected data leads to uncoordinated block requests.", RGBColor(254, 226, 226), RGBColor(225, 29, 72)),
        ("2. Cumulative Downtime & Delays", "• Same physical track blocked on different days by different departments.\n• Excessive track closures reduce availability to ~91%.\n• Causes sudden temporary speed restrictions (TSRs) and cascading train delays.", RGBColor(254, 243, 199), RGBColor(217, 119, 6)),
        ("3. Manual Planning Bottleneck", "• Section Controllers spend 3–5 days manually coordinating a single weekly program.\n• High cognitive load leads to burst blocks and human sanction errors.\n• 30–35% of sanctioned blocks are underutilized (CAG Audit).", RGBColor(224, 242, 254), RGBColor(2, 132, 199))
    ]
    for i, (title, body, bg_col, border_col) in enumerate(p_cards):
        c_shape = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i*3.95), Inches(1.3), Inches(3.7), Inches(5.6))
        c_shape.fill.solid(); c_shape.fill.fore_color.rgb = bg_col; c_shape.line.color.rgb = border_col; c_shape.line.width = Pt(1.5)
        tf = c_shape.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
        p = tf.paragraphs[0]; p.text = title; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = border_col; p.space_after = Pt(10)
        for line in body.split('\n'):
            p_l = tf.add_paragraph(); p_l.text = line; p_l.font.size = Pt(11); p_l.font.color.rgb = TEXT_DARK; p_l.space_after = Pt(4)

    # =========================================================================
    # SLIDE 3: PROPOSED SOLUTION & INNOVATION
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    t_box = slide3.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.7))
    p = t_box.text_frame.paragraphs[0]; p.text = "PROPOSED SOLUTION & CORE INNOVATION"; p.font.size = Pt(26); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    s_cards = [
        ("🤖 AI-Powered Central Scheduler", "• Ingests maintenance requisitions from TMS, TDMS, and SMMS alongside live COA train slots.\n• Automatically schedules conflict-free weekly and monthly Rolling Block Programs (RBP).\n• Zero human errors in block sanctions with mathematical proof.", Inches(0.8), Inches(1.3), Inches(5.7), Inches(2.6)),
        ("✨ Shadow Block Coordination", "• Actively co-schedules tasks from multiple departments on the same track section.\n• Bundles Track Tamping + OHE Overhaul + Axle Counter Calibration into a single Mega Block.\n• Slashes cumulative corridor downtime by up to 40%.", Inches(6.8), Inches(1.3), Inches(5.7), Inches(2.6)),
        ("⚖️ 4-Factor AI Priority Scorer", "• Evaluates tasks based on Urgency (40%), Safety Impact (30%), Overdue Days (20%), and Section Speed Class (10%).\n• Guarantees high-risk IMR rail fractures are scheduled in the earliest night corridor window.", Inches(0.8), Inches(4.2), Inches(5.7), Inches(2.6)),
        ("🎛️ What-If Constraint Simulator", "• Interactive parameter sliders for train disruption penalty (α), completion weight (β), and shadow bonus (δ).\n• Section controllers can simulate trade-offs and re-optimize the entire division in <0.1 seconds.", Inches(6.8), Inches(4.2), Inches(5.7), Inches(2.6))
    ]
    for title, body, x, y, w, h in s_cards:
        c_shape = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        c_shape.fill.solid(); c_shape.fill.fore_color.rgb = CARD_BG_LIGHT; c_shape.line.color.rgb = CARD_BORDER_BLUE; c_shape.line.width = Pt(1.5)
        tf = c_shape.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
        p = tf.paragraphs[0]; p.text = title; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT; p.space_after = Pt(6)
        for line in body.split('\n'):
            p_l = tf.add_paragraph(); p_l.text = line; p_l.font.size = Pt(11); p_l.font.color.rgb = TEXT_DARK; p_l.space_after = Pt(2)

    # =========================================================================
    # SLIDE 4: TECHNICAL ARCHITECTURE & FLOW
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    t_box = slide4.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.7))
    p = t_box.text_frame.paragraphs[0]; p.text = "TECHNICAL ARCHITECTURE & SYSTEM PIPELINE"; p.font.size = Pt(26); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    arch_layers = [
        ("1. Data & Ingestion Layer", "• TMS (Track Defects) | TDMS (OHE Power Blocks) | SMMS (Signals & Axle Counters) | COA (Live Train Timetable)\n• Local Database: SQLite / PostgreSQL (Configured with WAL Mode for concurrent reads during optimization)", Inches(1.2)),
        ("2. FastAPI Gateway & Service Layer", "• High-performance asynchronous REST API endpoints (/api/optimize, /api/tasks, /api/schedules)\n• 4-Factor AI Priority Scorer & Spatial-Temporal Conflict Detector pre-process all requisitions", Inches(2.6)),
        ("3. Optimization Core (CP-SAT Solver)", "• Google OR-Tools CP-SAT Combinatorial Solver enforces Hard Constraints (NoOverlap on tracks & machines)\n• Multi-Objective Optimization maximizes high-priority completion while rewarding multi-department Shadow Blocks", Inches(4.0)),
        ("4. Presentation & Dispatch Layer", "• Interactive D3.js Stringline (Marey) Diagram | Weekly Multi-Department Calendar Grid & Machinery Gantt Chart\n• Automated Statutory Form 351 Joint Disconnection Notices (Permit-to-Work Memo) with digital sign-offs", Inches(5.4))
    ]
    for title, body, y in arch_layers:
        c_shape = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), Inches(1.2))
        c_shape.fill.solid(); c_shape.fill.fore_color.rgb = CARD_BG_LIGHT; c_shape.line.color.rgb = CARD_BORDER_BLUE; c_shape.line.width = Pt(1.5)
        tf = c_shape.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.15)
        p = tf.paragraphs[0]; p.text = title; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT; p.space_after = Pt(2)
        for line in body.split('\n'):
            p_l = tf.add_paragraph(); p_l.text = line; p_l.font.size = Pt(10); p_l.font.color.rgb = TEXT_DARK; p_l.space_after = Pt(1)

    # =========================================================================
    # SLIDE 5: FEASIBILITY AND VIABILITY (HIGH-CONTRAST WHITE CARDS)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    t_box = slide5.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.7))
    p = t_box.text_frame.paragraphs[0]; p.text = "FEASIBILITY AND VIABILITY"; p.font.size = Pt(26); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    def create_white_card(slide, x, y, w, h, border_col):
        c = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        c.fill.solid(); c.fill.fore_color.rgb = RGBColor(255, 255, 255)
        c.line.color.rgb = border_col; c.line.width = Pt(1.5)
        return c

    # Left Column (X=0.8, W=5.7)
    # 1. Feasibility Card
    c1 = create_white_card(slide5, Inches(0.8), Inches(1.2), Inches(5.7), Inches(1.85), NAVY_ACCENT)
    tf1 = c1.text_frame; tf1.word_wrap = True; tf1.margin_left = tf1.margin_right = Inches(0.18); tf1.margin_top = Inches(0.1)
    p = tf1.paragraphs[0]; p.text = "⚖️ Feasibility:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT; p.space_after = Pt(2)
    for b, n in [
        ("1. Technical: ", "Google OR-Tools CP-SAT solver solves complete corridor plan in <0.06s."),
        ("2. Modular: ", "Layered architecture enables phased rollout from single division to national scale."),
        ("3. Integration: ", "Non-invasive REST webhooks connect to existing CRIS, TMS, SMMS, and COA servers."),
        ("4. Economic: ", "Zero specialized hardware required; runs on existing railway servers.")
    ]:
        p_pt = tf1.add_paragraph(); p_pt.space_after = Pt(2)
        rb = p_pt.add_run(); rb.text = b; rb.font.bold = True; rb.font.size = Pt(9.8); rb.font.color.rgb = DARK_BLUE
        rn = p_pt.add_run(); rn.text = n; rn.font.size = Pt(9.5); rn.font.color.rgb = TEXT_DARK

    # 2. Viability Card
    c2 = create_white_card(slide5, Inches(0.8), Inches(3.15), Inches(5.7), Inches(1.85), NAVY_ACCENT)
    tf2 = c2.text_frame; tf2.word_wrap = True; tf2.margin_left = tf2.margin_right = Inches(0.18); tf2.margin_top = Inches(0.1)
    p = tf2.paragraphs[0]; p.text = "⚙️ Viability:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT; p.space_after = Pt(2)
    for b, n in [
        ("1. Compliance: ", "Built strictly around Indian Railways G&SR Rules and Block Manuals."),
        ("2. Standardized PTW: ", "Auto-generates statutory Form 351 Joint Disconnection Notices."),
        ("3. Scalability: ", "Extensible across all 17 Zonal Railways and 68,000+ route kilometers."),
        ("4. Safety: ", "Mathematical proof of zero train-block collision eliminates human error.")
    ]:
        p_pt = tf2.add_paragraph(); p_pt.space_after = Pt(2)
        rb = p_pt.add_run(); rb.text = b; rb.font.bold = True; rb.font.size = Pt(9.8); rb.font.color.rgb = DARK_BLUE
        rn = p_pt.add_run(); rn.text = n; rn.font.size = Pt(9.5); rn.font.color.rgb = TEXT_DARK

    # 3. Challenges Card
    c3 = create_white_card(slide5, Inches(0.8), Inches(5.1), Inches(5.7), Inches(1.85), RGBColor(217, 119, 6))
    tf3 = c3.text_frame; tf3.word_wrap = True; tf3.margin_left = tf3.margin_right = Inches(0.18); tf3.margin_top = Inches(0.1)
    p = tf3.paragraphs[0]; p.text = "⚠️ Challenges & Mitigations:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = RGBColor(180, 83, 9); p.space_after = Pt(2)
    for b, n in [
        ("1. Data Latency: ", "Pydantic schemas sanitize timestamps, chainage markers, and defect logs."),
        ("2. Machine Conflicts: ", "NoOverlap logic prevents double-booking Track Machines & Tower Wagons."),
        ("3. Emergency Flares: ", "Dynamic What-If engine recalculates optimal bypass schedules in <150ms.")
    ]:
        p_pt = tf3.add_paragraph(); p_pt.space_after = Pt(2)
        rb = p_pt.add_run(); rb.text = b; rb.font.bold = True; rb.font.size = Pt(9.8); rb.font.color.rgb = DARK_BLUE
        rn = p_pt.add_run(); rn.text = n; rn.font.size = Pt(9.5); rn.font.color.rgb = TEXT_DARK

    # Right Column (X=6.8, W=5.7)
    # 4. Use Cases Card
    c4 = create_white_card(slide5, Inches(6.8), Inches(1.2), Inches(5.7), Inches(1.85), NAVY_ACCENT)
    tf4 = c4.text_frame; tf4.word_wrap = True; tf4.margin_left = tf4.margin_right = Inches(0.18); tf4.margin_top = Inches(0.1)
    p = tf4.paragraphs[0]; p.text = "🚆 Use Cases:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT; p.space_after = Pt(2)
    for b, n in [
        ("1. Section Controllers: ", "Automated corridor block windows without manual phone calls."),
        ("2. Civil/P-Way (TMS): ", "Prioritizes urgent IMR rail flaw welds & deep screening tamping blocks."),
        ("3. Traction (TDMS): ", "Synchronizes OHE cantilever overhauls & power isolation with track work."),
        ("4. S&T (SMMS): ", "Co-schedules axle counter calibration and point machine maintenance.")
    ]:
        p_pt = tf4.add_paragraph(); p_pt.space_after = Pt(2)
        rb = p_pt.add_run(); rb.text = b; rb.font.bold = True; rb.font.size = Pt(9.8); rb.font.color.rgb = DARK_BLUE
        rn = p_pt.add_run(); rn.text = n; rn.font.size = Pt(9.5); rn.font.color.rgb = TEXT_DARK

    # 5. Operational Potential Card
    c5 = create_white_card(slide5, Inches(6.8), Inches(3.15), Inches(5.7), Inches(1.85), RGBColor(22, 163, 74))
    tf5 = c5.text_frame; tf5.word_wrap = True; tf5.margin_left = tf5.margin_right = Inches(0.18); tf5.margin_top = Inches(0.1)
    p = tf5.paragraphs[0]; p.text = "📊 Operational Potential:"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = RGBColor(21, 128, 61); p.space_after = Pt(2)
    for b, n in [
        ("1. Availability Gain: ", "Elevates corridor asset availability from 91.2% to 96.6%+."),
        ("2. Downtime Cut: ", "Multi-department Shadow Blocks cut cumulative closures by up to 40%."),
        ("3. Punctuality Boost: ", "Eliminates cascading train detentions and emergency speed restrictions."),
        ("4. Digital Audit: ", "100% digital audit trail from requisition to track clearance.")
    ]:
        p_pt = tf5.add_paragraph(); p_pt.space_after = Pt(2)
        rb = p_pt.add_run(); rb.text = b; rb.font.bold = True; rb.font.size = Pt(9.8); rb.font.color.rgb = DARK_BLUE
        rn = p_pt.add_run(); rn.text = n; rn.font.size = Pt(9.5); rn.font.color.rgb = TEXT_DARK

    # 6. Bottom Right Highlight Box
    c6 = create_white_card(slide5, Inches(6.8), Inches(5.1), Inches(5.7), Inches(1.85), RGBColor(14, 165, 233))
    c6.line.width = Pt(2.0)
    tf6 = c6.text_frame; tf6.word_wrap = True; tf6.margin_left = tf6.margin_right = Inches(0.18); tf6.margin_top = Inches(0.1)
    p = tf6.paragraphs[0]; p.text = "⭐ Supporting Facts for Feasibility & Viability"; p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT; p.space_after = Pt(2)
    for cp in [
        "➔ CAG Railway Audit: 30–35% of sanctioned blocks underutilized due to manual coordination.",
        "➔ Network Scale: Coordinates across 68,000+ route km & 13,000+ trains, recovering delay hours.",
        "➔ Proven Benchmark: NDLS–ALJN pilot achieved 100% completion with 4 Mega Blocks in <0.1s."
    ]:
        p_pt = tf6.add_paragraph(); p_pt.text = cp; p_pt.font.size = Pt(9.3); p_pt.font.color.rgb = TEXT_DARK; p_pt.space_after = Pt(2)

    # =========================================================================
    # SLIDE 6: RESEARCH AND REFERENCES (MATCHING SAARTHI WINNING FORMAT)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    t_box = slide6.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.7), Inches(0.7))
    p = t_box.text_frame.paragraphs[0]; p.text = "RESEARCH AND REFERENCES"; p.font.size = Pt(28); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # Top Left: References
    ref_box = slide6.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(5.2), Inches(3.2))
    tf_ref = ref_box.text_frame; tf_ref.word_wrap = True; tf_ref.margin_left = tf_ref.margin_right = tf_ref.margin_top = 0
    p = tf_ref.paragraphs[0]; p.text = "❖ References & Research:"; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT; p.space_after = Pt(6)
    
    ref_data = [
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
    for cat, l_list in ref_data:
        p_c = tf_ref.add_paragraph(); p_c.text = cat; p_c.font.size = Pt(11); p_c.font.bold = True; p_c.font.color.rgb = DARK_BLUE; p_c.space_before = Pt(3); p_c.space_after = Pt(1)
        for lnk in l_list:
            p_l = tf_ref.add_paragraph(); p_l.text = "➤ " + lnk; p_l.font.size = Pt(9.5); p_l.font.color.rgb = TEXT_DARK; p_l.space_after = Pt(1)

    # Bottom Left: Working Prototype Model Placeholder
    proto_card = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.55), Inches(5.2), Inches(2.45))
    proto_card.fill.solid(); proto_card.fill.fore_color.rgb = RGBColor(240, 249, 255); proto_card.line.color.rgb = NAVY_ACCENT; proto_card.line.width = Pt(1.5)
    tf_p = proto_card.text_frame; tf_p.word_wrap = True; tf_p.margin_left = tf_p.margin_right = Inches(0.2); tf_p.margin_top = Inches(0.15)
    p = tf_p.paragraphs[0]; p.text = "💻 Working Base Prototype Model (Local Server: 127.0.0.1:8000)"; p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT; p.space_after = Pt(4)
    p_d = tf_p.add_paragraph(); p_d.text = "• Live CP-SAT Optimizer solves 131.2 km corridor (NDLS–ALJN) in 0.06s.\n• Features D3.js Stringline Diagram, Weekly Block Calendar Grid, and 4 Coordinated Shadow Blocks.\n\n[PASTE YOUR RUNNING PROTOTYPE SCREENSHOT HERE]"; p_d.font.size = Pt(10); p_d.font.color.rgb = TEXT_DARK

    # Right: Comparison Table
    head_box = slide6.shapes.add_textbox(Inches(6.3), Inches(1.15), Inches(6.2), Inches(0.4))
    p = head_box.text_frame.paragraphs[0]; p.text = "❖ Comparison with Existing Systems:"; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = NAVY_ACCENT

    table_shape = slide6.shapes.add_table(rows=8, cols=5, left=Inches(6.3), top=Inches(1.6), width=Inches(6.2), height=Inches(5.4))
    table = table_shape.table
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(1.1)
    table.columns[2].width = Inches(1.0)
    table.columns[3].width = Inches(0.95)
    table.columns[4].width = Inches(0.95)

    headers = ["Feature", "Our AI System\n(SIH26027)", "Manual Plan\n(BDMS)", "Standalone\nCOA", "TMS/TDMS\nStandalone"]
    for col_idx, h_text in enumerate(headers):
        cell = table.cell(0, col_idx); cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(15, 23, 42) if col_idx == 1 else RGBColor(226, 232, 240)
        p = cell.text_frame.paragraphs[0]; p.text = h_text; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(9.5); p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255) if col_idx == 1 else DARK_BLUE

    rows_data = [
        ("Multi-Dept Shadow Blocking", "☑️ Yes (Auto)", "❌ No", "❌ No", "❌ No"),
        ("4-Factor AI Priority Ranking", "☑️ Yes (AI)", "❌ No", "❌ No", "❌ (Basic)"),
        ("Zero Train Conflict Guarantee", "☑️ Yes (Hard)", "❌ (Prone)", "❌ (Manual)", "❌ No"),
        ("Night Window (01:00-05:00) Sync", "☑️ Yes (Auto)", "❌ (Manual)", "❌ No", "❌ No"),
        ("Sub-100ms Optimization Latency", "☑️ Yes (0.06s)", "❌ (3-5 Days)", "❌ No", "❌ No"),
        ("Live 'What-If' Parameter Sliders", "☑️ Yes (Live)", "❌ No", "❌ No", "❌ No"),
        ("Statutory Form 351 PTW Memo", "☑️ Yes (1-Click)", "❌ (Manual)", "❌ No", "❌ No"),
    ]
    for row_idx, r_c in enumerate(rows_data, start=1):
        for col_idx, val in enumerate(r_c):
            cell = table.cell(row_idx, col_idx); cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(224, 242, 254) if col_idx == 1 else (RGBColor(248, 250, 252) if row_idx % 2 == 1 else RGBColor(255, 255, 255))
            p = cell.text_frame.paragraphs[0]; p.text = val
            p.alignment = PP_ALIGN.LEFT if col_idx == 0 else PP_ALIGN.CENTER
            p.font.size = Pt(9.5)
            if col_idx == 1:
                p.font.bold = True; p.font.color.rgb = RGBColor(3, 105, 161)
            elif "☑️" in val:
                p.font.bold = True; p.font.color.rgb = RGBColor(22, 163, 74)
            elif "❌" in val:
                p.font.color.rgb = RGBColor(225, 29, 72)
            else:
                p.font.color.rgb = TEXT_DARK

    output_path = r"c:\Users\kvish\OneDrive\Desktop\railway-planner\SIH26027_Full_Presentation_Editable.pptx"
    prs.save(output_path)
    print(f"Master presentation updated with Slide 6 Research & References: {output_path}")

if __name__ == "__main__":
    create_full_sih_deck()
