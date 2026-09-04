import os
from PIL import Image, ImageDraw, ImageFont

def create_transparent_architecture_png():
    # Width and Height for high-res output
    width = 2400
    height = 1400
    
    # Create pure RGBA image with 100% transparent background (0, 0, 0, 0)
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Try loading clean Windows system font
    try:
        font_title = ImageFont.truetype("segoeui.ttf", 26)
        font_bold = ImageFont.truetype("segoeuib.ttf", 22)
        font_main = ImageFont.truetype("segoeui.ttf", 20)
        font_small = ImageFont.truetype("segoeui.ttf", 16)
        font_bullet = ImageFont.truetype("segoeui.ttf", 17)
        font_emoji = ImageFont.truetype("seguiemj.ttf", 24)
        font_train = ImageFont.truetype("seguiemj.ttf", 36)
    except Exception:
        font_title = ImageFont.load_default()
        font_bold = font_main = font_small = font_bullet = font_emoji = font_train = ImageFont.load_default()

    # Color Palette
    BORDER_LAYER = (100, 116, 139, 255)     # Slate-500
    TEXT_LAYER = (226, 232, 240, 255)       # Slate-200
    
    CARD_BG = (15, 23, 42, 240)             # Slate-900 with strong opacity for text legibility
    CARD_BORDER = (71, 85, 105, 255)        # Slate-600
    CARD_TEXT = (248, 250, 252, 255)        # White
    
    ARROW_COLOR = (56, 189, 248, 255)       # Sky-400
    
    # Helper to draw rounded box
    def draw_box(x1, y1, x2, y2, bg=CARD_BG, border=CARD_BORDER, radius=10, border_w=2):
        draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=bg, outline=border, width=border_w)

    # Helper to draw clean arrow
    def draw_arrow(points, color=ARROW_COLOR, width=4, head_size=12):
        for i in range(len(points) - 1):
            draw.line([points[i], points[i+1]], fill=color, width=width)
        # Arrowhead at the last segment
        p_prev = points[-2]
        p_end = points[-1]
        dx = p_end[0] - p_prev[0]
        dy = p_end[1] - p_prev[1]
        
        if dx > 0: # right
            head = [(p_end[0], p_end[1]), (p_end[0]-head_size, p_end[1]-head_size//2), (p_end[0]-head_size, p_end[1]+head_size//2)]
        elif dx < 0: # left
            head = [(p_end[0], p_end[1]), (p_end[0]+head_size, p_end[1]-head_size//2), (p_end[0]+head_size, p_end[1]+head_size//2)]
        elif dy > 0: # down
            head = [(p_end[0], p_end[1]), (p_end[0]-head_size//2, p_end[1]-head_size), (p_end[0]+head_size//2, p_end[1]-head_size)]
        else: # up
            head = [(p_end[0], p_end[1]), (p_end[0]-head_size//2, p_end[1]+head_size), (p_end[0]+head_size//2, p_end[1]+head_size)]
        draw.polygon(head, fill=color)

    # ==========================================
    # 1. LAYER OUTLINES (100% Transparent interior)
    # ==========================================
    # Data Layer
    draw.rounded_rectangle([680, 50, 1720, 420], radius=8, fill=None, outline=BORDER_LAYER, width=2)
    draw.text((710, 65), "Data & Ingestion Layer", fill=TEXT_LAYER, font=font_title)

    # FastAPI Layer
    draw.rounded_rectangle([980, 520, 1900, 870], radius=8, fill=None, outline=BORDER_LAYER, width=2)
    draw.text((1010, 535), "FastAPI Service Layer", fill=TEXT_LAYER, font=font_title)

    # Presentation Layer
    draw.rounded_rectangle([50, 950, 1260, 1150], radius=8, fill=None, outline=BORDER_LAYER, width=2)
    draw.text((80, 965), "Presentation & Dispatch Layer", fill=TEXT_LAYER, font=font_title)

    # Engine Layer
    draw.rounded_rectangle([1320, 950, 2350, 1320], radius=8, fill=None, outline=BORDER_LAYER, width=2)
    draw.text((1350, 965), "Constraint Programming Engine", fill=TEXT_LAYER, font=font_title)

    # Train Graphic top-left
    draw.text((490, 135), "🚋 🚆 🚂", fill=TEXT_LAYER, font=font_train)

    # ==========================================
    # 2. INNER NODES / BOXES
    # ==========================================
    # Layer 1: Data Ingestion Nodes
    # COA Node
    draw_box(710, 115, 1180, 205, bg=(11, 20, 42, 245), border=(56, 189, 248, 255))
    draw.text((740, 142), "📊  COA Real-Time Train Feed", fill=CARD_TEXT, font=font_bold)

    # TMS Node
    draw_box(1220, 115, 1690, 205, bg=(11, 20, 42, 245), border=(56, 189, 248, 255))
    draw.text((1250, 142), "⚙️  TMS / SMMS / TDMS Task APIs", fill=CARD_TEXT, font=font_bold)

    # Database Node (Cylinder Gradient look)
    draw_box(920, 265, 1480, 385, bg=(3, 105, 161, 245), border=(56, 189, 248, 255), radius=16, border_w=3)
    draw.text((950, 305), "🪶", fill=(255,255,255,255), font=font_emoji)
    draw.text((1010, 290), "SQLite / PostgreSQL", fill=(255,255,255,255), font=font_bold)
    draw.text((1035, 330), "(WAL Mode Enabled)", fill=(224,242,254,255), font=font_main)
    draw.text((1415, 305), "🐘", fill=(255,255,255,255), font=font_emoji)

    # Layer 2: FastAPI Nodes
    # FastAPI Gateway
    draw_box(1020, 580, 1460, 665, bg=(4, 40, 18, 245), border=(34, 197, 94, 255))
    draw.text((1050, 605), "⚡  FastAPI Async REST API", fill=(255,255,255,255), font=font_bold)

    # Scorer Engine
    draw_box(1120, 715, 1450, 805, bg=CARD_BG, border=CARD_BORDER)
    draw.text((1150, 742), "Priority Scorer Engine", fill=CARD_TEXT, font=font_bold)

    # Spatial Conflict Detector
    draw_box(1490, 715, 1860, 805, bg=CARD_BG, border=CARD_BORDER)
    draw.text((1510, 742), "Spatial-Temporal Conflict Detector", fill=CARD_TEXT, font=font_bold)

    # Layer 3: Presentation Nodes
    # D3 Stringline
    draw_box(80, 1015, 440, 1105, bg=CARD_BG, border=(249, 115, 22, 255))
    draw.text((105, 1042), "🟠  D3.js Stringline (Marey) Chart", fill=CARD_TEXT, font=font_main)

    # Weekly Calendar
    draw_box(470, 1015, 840, 1105, bg=CARD_BG, border=CARD_BORDER)
    draw.text((495, 1042), "📅  Weekly Block Calendar & Gantt", fill=CARD_TEXT, font=font_main)

    # PTW Form
    draw_box(870, 1015, 1230, 1105, bg=CARD_BG, border=CARD_BORDER)
    draw.text((890, 1042), "📄  Auto-Generated Form 351 PTW Notice", fill=CARD_TEXT, font=font_small)

    # Layer 4: CP-SAT Engine Nodes
    # Main Solver Node
    draw_box(1460, 1010, 2210, 1085, bg=CARD_BG, border=(56, 189, 248, 255))
    draw.text((1580, 1030), "🧩  Google OR-Tools CP-SAT Solver", fill=(56, 189, 248, 255), font=font_bold)

    # Hard Constraints Node
    draw_box(1350, 1125, 1810, 1265, bg=CARD_BG, border=CARD_BORDER)
    draw.text((1370, 1145), "Hard Constraints Validator", fill=(56, 189, 248, 255), font=font_bold)
    draw.text((1370, 1180), "• NoOverlap (Machines & Tracks)", fill=TEXT_LAYER, font=font_bullet)
    draw.text((1370, 1215), "• Zero Train-Block Collision", fill=(34, 197, 94, 255), font=font_bold)

    # Soft Constraints Node
    draw_box(1860, 1125, 2320, 1265, bg=CARD_BG, border=CARD_BORDER)
    draw.text((1880, 1145), "Soft Constraints & Objective", fill=(216, 180, 254, 255), font=font_bold)
    draw.text((1880, 1180), "• Maximize High-Priority Completion", fill=TEXT_LAYER, font=font_bullet)
    draw.text((1880, 1215), "• Shadow Block Bonus", fill=TEXT_LAYER, font=font_bullet)

    # ==========================================
    # 3. CONNECTING ARROWS
    # ==========================================
    # Data feeds to DB
    draw_arrow([(945, 205), (945, 235), (1200, 235), (1200, 265)])
    draw_arrow([(1455, 205), (1455, 235), (1200, 235), (1200, 265)])

    # DB down to FastAPI
    draw_arrow([(1200, 385), (1200, 580)])

    # FastAPI to Scorer & Conflict Detector
    draw_arrow([(1240, 665), (1240, 690), (1285, 690), (1285, 715)])
    draw_arrow([(1240, 665), (1240, 690), (1675, 690), (1675, 715)])

    # FastAPI down to Presentation items
    draw_arrow([(1020, 625), (260, 625), (260, 1015)])
    draw_arrow([(1020, 625), (655, 625), (655, 1015)])
    draw_arrow([(1100, 665), (1100, 1015)])

    # Scorer & Detector to Solver Engine
    draw_arrow([(1675, 805), (1675, 1010)])
    draw_arrow([(1285, 805), (1285, 880), (1675, 880)])

    # Solver internal connections
    draw_arrow([(1580, 1085), (1580, 1125)])
    draw_arrow([(2090, 1085), (2090, 1125)])

    # Engine feedback back to calendar & top
    draw_arrow([(1350, 1195), (655, 1195), (655, 1105)])
    draw_arrow([(2320, 1195), (2370, 1195), (2370, 480), (1260, 480), (1260, 520)])

    # Save PNG
    output_path = r"c:\Users\kvish\OneDrive\Desktop\railway-planner\architecture_transparent.png"
    img.save(output_path, "PNG")
    print(f"Pure transparent PNG created successfully: {output_path}")

if __name__ == "__main__":
    create_transparent_architecture_png()
