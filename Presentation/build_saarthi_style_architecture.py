import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR

def generate_saarthi_style_architecture():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Color Palette matching the exact reference style
    DARK_BLUE = RGBColor(15, 23, 42)
    NAVY_ACCENT = RGBColor(2, 132, 199)
    TEXT_DARK = RGBColor(30, 41, 59)
    TEXT_MUTED = RGBColor(71, 85, 105)
    
    BADGE_YELLOW = RGBColor(254, 240, 138)  # #fef08a
    BORDER_YELLOW = RGBColor(202, 138, 4)
    
    BG_CARD_WHITE = RGBColor(255, 255, 255)
    BG_CARD_LIGHT = RGBColor(248, 250, 252)
    BORDER_GRAY = RGBColor(203, 213, 225)
    
    RED_ACCENT = RGBColor(225, 29, 72)
    GREEN_ACCENT = RGBColor(22, 163, 74)
    BLUE_ACCENT = RGBColor(3, 105, 161)
    PURPLE_ACCENT = RGBColor(147, 51, 234)
    ORANGE_ACCENT = RGBColor(234, 88, 12)

    def add_arrow(x1, y1, x2, y2, color=NAVY_ACCENT):
        conn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
        conn.line.color.rgb = color
        conn.line.width = Pt(1.5)

    # =========================================================================
    # TOP HEADER: YELLOW PILL BADGE "System Architecture"
    # =========================================================================
    top_badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), Inches(0.18), Inches(2.7), Inches(0.48))
    top_badge.fill.solid(); top_badge.fill.fore_color.rgb = BADGE_YELLOW
    top_badge.line.color.rgb = BORDER_YELLOW; top_badge.line.width = Pt(1.5)
    p = top_badge.text_frame.paragraphs[0]; p.text = "System Architecture"; p.alignment = PP_ALIGN.CENTER
    p.font.name = "Segoe UI"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # =========================================================================
    # TOP ROW: CLIENT SYSTEM ➔ WEB APP ➔ SERVER ➔ DATABASE & SERVICES
    # =========================================================================
    # 1. Client System (Top Left)
    c_sys = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(0.45), Inches(1.8), Inches(1.05))
    c_sys.fill.solid(); c_sys.fill.fore_color.rgb = BG_CARD_WHITE; c_sys.line.color.rgb = BORDER_GRAY; c_sys.line.width = Pt(1.2)
    tf = c_sys.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]; p.text = "💻 📱 🖥️"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(16)
    p2 = tf.add_paragraph(); p2.text = "Client System\n(Web & Controller Desk)"; p2.alignment = PP_ALIGN.CENTER; p2.font.size = Pt(8.5); p2.font.bold = True; p2.font.color.rgb = DARK_BLUE

    # 2. Web Application (Frontend)
    web_app = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(3.6), Inches(0.65), Inches(1.1), Inches(1.1))
    web_app.fill.solid(); web_app.fill.fore_color.rgb = RGBColor(76, 29, 149); web_app.line.color.rgb = PURPLE_ACCENT; web_app.line.width = Pt(1.5)
    tf = web_app.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]; p.text = "🌐"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(16)
    p2 = tf.add_paragraph(); p2.text = "D3.js Web App"; p2.alignment = PP_ALIGN.CENTER; p2.font.size = Pt(7); p2.font.bold = True; p2.font.color.rgb = RGBColor(255, 255, 255)

    # 3. Server (FastAPI + CP-SAT Core)
    server_node = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.8), Inches(0.65), Inches(1.1), Inches(1.1))
    server_node.fill.solid(); server_node.fill.fore_color.rgb = RGBColor(254, 240, 138); server_node.line.color.rgb = BORDER_YELLOW; server_node.line.width = Pt(1.5)
    tf = server_node.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]; p.text = "⚡ 🧩"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(15)
    p2 = tf.add_paragraph(); p2.text = "FastAPI +\nCP-SAT Solver"; p2.alignment = PP_ALIGN.CENTER; p2.font.size = Pt(6.8); p2.font.bold = True; p2.font.color.rgb = DARK_BLUE

    # 4. Database (Top Right)
    db_node = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.8), Inches(0.65), Inches(1.1), Inches(1.1))
    db_node.fill.solid(); db_node.fill.fore_color.rgb = BLUE_ACCENT; db_node.line.color.rgb = NAVY_ACCENT; db_node.line.width = Pt(1.5)
    tf = db_node.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.2)
    p = tf.paragraphs[0]; p.text = "🗄️ 🐘"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(15)
    p2 = tf.add_paragraph(); p2.text = "SQLite / DB\n(WAL Mode)"; p2.alignment = PP_ALIGN.CENTER; p2.font.size = Pt(6.8); p2.font.bold = True; p2.font.color.rgb = RGBColor(255, 255, 255)

    # 5. External Services Badge (Far Right)
    svc_node = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(11.6), Inches(0.75), Inches(0.9), Inches(0.9))
    svc_node.fill.solid(); svc_node.fill.fore_color.rgb = RED_ACCENT; svc_node.line.color.rgb = RGBColor(190, 18, 60); svc_node.line.width = Pt(1.5)
    tf = svc_node.text_frame; tf.word_wrap = True; tf.margin_top = Inches(0.18)
    p = tf.paragraphs[0]; p.text = "📡 ⚙️"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(13)
    p2 = tf.add_paragraph(); p2.text = "CRIS APIs"; p2.alignment = PP_ALIGN.CENTER; p2.font.size = Pt(6.5); p2.font.bold = True; p2.font.color.rgb = RGBColor(255, 255, 255)

    # Top Connecting Arrows
    add_arrow(2.3, 0.95, 3.6, 0.95)   # Client -> Web App (Client Req/Res)
    add_arrow(4.7, 1.2, 6.8, 1.2)     # Web App -> Server (Server Req/Res)
    add_arrow(7.9, 0.95, 9.8, 0.95)   # Server -> DB (Data Ingestion)
    add_arrow(7.9, 1.2, 11.6, 1.2)    # Server -> Services

    # Top Flow Labels
    lbl1 = slide.shapes.add_textbox(Inches(2.3), Inches(0.68), Inches(1.3), Inches(0.3))
    lbl1.text_frame.paragraphs[0].text = "Client Req/Res"; lbl1.text_frame.paragraphs[0].font.size = Pt(7); lbl1.text_frame.paragraphs[0].font.color.rgb = TEXT_MUTED

    lbl2 = slide.shapes.add_textbox(Inches(5.0), Inches(0.95), Inches(1.5), Inches(0.3))
    lbl2.text_frame.paragraphs[0].text = "Server Req/Res (FastAPI)"; lbl2.text_frame.paragraphs[0].font.size = Pt(7); lbl2.text_frame.paragraphs[0].font.color.rgb = TEXT_MUTED

    lbl3 = slide.shapes.add_textbox(Inches(8.2), Inches(0.68), Inches(1.3), Inches(0.3))
    lbl3.text_frame.paragraphs[0].text = "Data Retrieval"; lbl3.text_frame.paragraphs[0].font.size = Pt(7); lbl3.text_frame.paragraphs[0].font.color.rgb = TEXT_MUTED

    # =========================================================================
    # MIDDLE SECTION: DEPARTMENTAL ROLE ACCESS & RESTRICTED FUNCTIONAL MODULES
    # =========================================================================
    # Middle Outer Container Frame
    mid_frame = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(1.85), Inches(12.33), Inches(4.3))
    mid_frame.fill.solid(); mid_frame.fill.fore_color.rgb = BG_CARD_WHITE
    mid_frame.line.color.rgb = BORDER_GRAY; mid_frame.line.width = Pt(1.5)

    # Middle Title
    m_title = slide.shapes.add_textbox(Inches(3.5), Inches(1.9), Inches(6.0), Inches(0.35))
    p = m_title.text_frame.paragraphs[0]; p.text = "Departmental Role-Based Modules (Restricted Access)"; p.alignment = PP_ALIGN.CENTER
    p.font.name = "Segoe UI"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # ----------------------------------------------------
    # LEFT COLUMN: USER ROLES / STAKEHOLDERS (X = 0.6 in to 2.4 in)
    # ----------------------------------------------------
    roles_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(2.25), Inches(2.2), Inches(3.75))
    roles_box.fill.solid(); roles_box.fill.fore_color.rgb = BG_CARD_LIGHT
    roles_box.line.color.rgb = BORDER_GRAY; roles_box.line.width = Pt(1)
    
    tf_roles = roles_box.text_frame; tf_roles.word_wrap = True; tf_roles.margin_top = Inches(0.08)
    p = tf_roles.paragraphs[0]; p.text = "👤 Stakeholders / Users"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(9.5); p.font.bold = True; p.font.color.rgb = DARK_BLUE
    
    roles_list = [
        ("🚆 Section Controller", "(Sr. DOM / Traffic Desk)"),
        ("🛠️ Civil / P-Way Engr", "(TMS Track Gangs)"),
        ("⚡ Traction / TRD Staff", "(OHE / Power TPC)"),
        ("📡 S&T Signal Inspector", "(SMMS Point Machines)"),
        ("🛡️ Division Admin / DRM", "(System Config & Audit)")
    ]
    for r_title, r_sub in roles_list:
        p_t = tf_roles.add_paragraph(); p_t.space_before = Pt(5)
        p_t.text = r_title; p_t.alignment = PP_ALIGN.CENTER; p_t.font.size = Pt(8.5); p_t.font.bold = True; p_t.font.color.rgb = DARK_BLUE
        p_s = tf_roles.add_paragraph()
        p_s.text = r_sub; p_s.alignment = PP_ALIGN.CENTER; p_s.font.size = Pt(7); p_s.font.color.rgb = TEXT_MUTED

    # ----------------------------------------------------
    # CENTER MATRIX: FUNCTIONAL MODULES (X = 2.9 in to 9.9 in)
    # ----------------------------------------------------
    modules_data = [
        ("🔒 Corridor Block Planning Hub", "🔒 15-min Train Collision Conflict Checker"),
        ("🔒 Multi-Dept Shadow Block Bundler", "🔒 Night Window (01:00-05:00) Synchronizer"),
        ("🔒 4-Factor AI Urgency Priority Scorer", "🔒 Track Tamping & IMR Rail Defect Scheduler"),
        ("🔒 OHE Power Isolation Shutdown Manager", "🔒 S&T Axle Counter Joint Disconnection Memo"),
        ("🔒 Automated Form 351 PTW Sign-Off", "🔒 Live 'What-If' Parameter Sliders (α, β, δ)"),
        ("🔒 Machine Resource (BCM/DTS) Allocator", "🔒 Division Performance & Audit Dashboard")
    ]

    for row_idx, (col1_txt, col2_txt) in enumerate(modules_data):
        y_pos = 2.3 + row_idx * 0.58
        m_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.9), Inches(y_pos), Inches(6.9), Inches(0.48))
        m_box.fill.solid(); m_box.fill.fore_color.rgb = BG_CARD_LIGHT
        m_box.line.color.rgb = BORDER_GRAY; m_box.line.width = Pt(1)
        
        tf_m = m_box.text_frame; tf_m.word_wrap = True; tf_m.margin_top = Inches(0.08)
        p = tf_m.paragraphs[0]
        r1 = p.add_run(); r1.text = col1_txt; r1.font.size = Pt(8.5); r1.font.bold = True; r1.font.color.rgb = DARK_BLUE
        r_sp = p.add_run(); r_sp.text = "          |          "; r_sp.font.size = Pt(8); r_sp.font.color.rgb = BORDER_GRAY
        r2 = p.add_run(); r2.text = col2_txt; r2.font.size = Pt(8.5); r2.font.bold = True; r2.font.color.rgb = DARK_BLUE

    # ----------------------------------------------------
    # RIGHT COLUMN: INTEGRATED RAILWAY APIS / SERVICES
    # ----------------------------------------------------
    svc_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(10.0), Inches(2.25), Inches(2.7), Inches(3.75))
    svc_box.fill.solid(); svc_box.fill.fore_color.rgb = BG_CARD_LIGHT
    svc_box.line.color.rgb = BORDER_GRAY; svc_box.line.width = Pt(1)
    
    tf_svc = svc_box.text_frame; tf_svc.word_wrap = True; tf_svc.margin_top = Inches(0.08)
    p = tf_svc.paragraphs[0]; p.text = "🔌 External Services & APIs"; p.alignment = PP_ALIGN.CENTER; p.font.size = Pt(9.5); p.font.bold = True; p.font.color.rgb = DARK_BLUE
    
    apis_list = [
        ("🏢 CRIS Cloud Infrastructure", "Secure REST Webhooks"),
        ("📊 COA Live Train Timetable", "Real-Time Schedule Feed"),
        ("⚙️ TMS Track Defect API", "Civil Flaws & Rail Data"),
        ("⚡ TDMS Traction System", "25kV OHE Power Feeds"),
        ("📡 SMMS Signal Fault System", "Interlocking Data"),
        ("📄 BDMS 2.0 Integration", "Digital Block Disconnections")
    ]
    for a_t, a_d in apis_list:
        p_at = tf_svc.add_paragraph(); p_at.space_before = Pt(4)
        p_at.text = a_t; p_at.alignment = PP_ALIGN.CENTER; p_at.font.size = Pt(8); p_at.font.bold = True; p_at.font.color.rgb = NAVY_ACCENT
        p_ad = tf_svc.add_paragraph()
        p_ad.text = a_d; p_ad.alignment = PP_ALIGN.CENTER; p_ad.font.size = Pt(6.8); p_ad.font.color.rgb = TEXT_MUTED

    # Access Legend Badge
    leg_badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), Inches(5.85), Inches(3.7), Inches(0.32))
    leg_badge.fill.solid(); leg_badge.fill.fore_color.rgb = BADGE_YELLOW
    leg_badge.line.color.rgb = BORDER_YELLOW; leg_badge.line.width = Pt(1)
    p = leg_badge.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    p.text = "🔒 Full Controller Access      🔑 Departmental Access"; p.font.size = Pt(8); p.font.bold = True; p.font.color.rgb = DARK_BLUE

    # =========================================================================
    # BOTTOM SECTION: COMMON DASHBOARD MODULES (ALL USERS)
    # =========================================================================
    bot_frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(6.25), Inches(12.33), Inches(1.05))
    bot_frame.fill.solid(); bot_frame.fill.fore_color.rgb = RGBColor(248, 250, 252)
    bot_frame.line.color.rgb = BORDER_GRAY; bot_frame.line.width = Pt(1.5)

    common_modules = [
        ("📈", "D3 Stringline\nChart"),
        ("📅", "Weekly Block\nCalendar Grid"),
        ("⏱️", "Gantt Machinery\nTimeline"),
        ("⚡", "Live Asset\nAvailability (96.6%)"),
        ("📄", "Form 351 PTW\nViewer"),
        ("🚨", "Real-Time\nSafety Alerts")
    ]
    for i, (icon, label) in enumerate(common_modules):
        x_c = 0.8 + i * 2.0
        c_badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x_c), Inches(6.35), Inches(1.75), Inches(0.85))
        c_badge.fill.solid(); c_badge.fill.fore_color.rgb = BG_CARD_WHITE
        c_badge.line.color.rgb = BORDER_GRAY; c_badge.line.width = Pt(1)
        
        tf_c = c_badge.text_frame; tf_c.word_wrap = True; tf_c.margin_top = Inches(0.04)
        p_ic = tf_c.paragraphs[0]; p_ic.text = icon; p_ic.alignment = PP_ALIGN.CENTER; p_ic.font.size = Pt(13)
        p_lb = tf_c.add_paragraph(); p_lb.text = label; p_lb.alignment = PP_ALIGN.CENTER; p_lb.font.size = Pt(7); p_lb.font.bold = True; p_lb.font.color.rgb = DARK_BLUE

    output_path = r"c:\Users\kvish\OneDrive\Desktop\railway-planner\System_Architecture_Saarthi_Style_Editable.pptx"
    prs.save(output_path)
    print(f"Saarthi-style Full System Architecture PPTX created: {output_path}")

if __name__ == "__main__":
    generate_saarthi_style_architecture()
