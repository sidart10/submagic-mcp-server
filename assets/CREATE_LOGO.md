# Quick Logo Creation Guide

## Option 1: Use AI (FASTEST - 2 minutes)

### DALL-E / ChatGPT

Go to https://chat.openai.com and use this prompt:

```
Create a simple, modern logo for a video editing AI software called "Submagic MCP Server". 
The logo should be 400x400 pixels, featuring a video camera or play button icon with 
magical sparkles. Use a purple and white color scheme (#9333EA purple, white text/icons). 
Minimalist design, professional, tech-forward. Square format, centered composition.
```

**Then**: Download, save as `logo.png` in this directory.

---

## Option 2: Use Canva (EASY - 5 minutes)

### Steps:

1. Go to https://www.canva.com
2. Click "Create a design" → "Custom size" → 400 x 400 pixels
3. Add a background:
   - Select "Elements" → Search "gradient"
   - Choose purple gradient or use solid color: #9333EA
4. Add an icon:
   - Search "video camera" or "play button" or "magic wand"
   - Drag to center, make it white color
   - Size: ~250x250 pixels
5. (Optional) Add text:
   - Add "S" or "SM" in large white font
   - Center it
6. Download as PNG
7. Save as `logo.png` in this directory

---

## Option 3: Simple Text Logo (QUICKEST - 1 minute)

If you just want to test everything first:

1. Go to https://www.canva.com
2. Create 400x400 design
3. Purple background (#9333EA)
4. Add white "S" or "SM" text, centered
5. Download PNG
6. Name it `logo.png`

You can always update it later once your server gains traction!

---

## Option 4: Use This Pre-Made Template

Go to: https://www.canva.com/design/DAFxExample/edit

(Or search Canva templates for "tech logo 400x400")

---

## Verification

Once you have `logo.png`:

```bash
# Check file size
file logo.png
# Should say: PNG image data, 400 x 400

# Test URL
git add assets/logo.png
git commit -m "Add marketplace logo"
git push

# Your logo URL will be:
# https://raw.githubusercontent.com/sidart10/submagic-mcp-server/main/assets/logo.png
```

---

## Color Recommendations

**Primary Colors:**
- Purple: `#9333EA` or `#7C3AED`
- Pink accent: `#EC4899`
- White: `#FFFFFF`

**Alternative:**
- Orange: `#FF6B35`
- Blue: `#004E89`
- Black: `#000000`

---

## Don't Overthink It!

Your first logo doesn't need to be perfect. The most important thing is:
- ✅ 400x400 pixels
- ✅ PNG format
- ✅ Recognizable
- ✅ Professional enough

You can update it anytime after publishing!

