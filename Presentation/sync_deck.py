import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def update_full_deck():
    # Import functions or build all slides
    from build_slide4_technical_approach import build_slide4_technical_approach
    from build_slide6_research_references import build_slide6_research_references
    from generate_full_sih_deck import create_full_sih_deck
    
    create_full_sih_deck()
    print("Full deck synchronized successfully!")

if __name__ == "__main__":
    update_full_deck()
