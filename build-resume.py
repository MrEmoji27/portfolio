# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color

W, H = 595.2756, 841.8898
INK   = Color(0.05098, 0.05098, 0.043137)
PAPER = Color(0.909804, 0.894118, 0.847059)
RED   = Color(0.878431, 0.203922, 0.094118)
YEL   = Color(0.941176, 0.721569, 0.0)
L, R = 46.0, 549.3

F = "build-fonts/"
pdfmetrics.registerFont(TTFont("AB",  F+"archivo-black-latin-400-normal.ttf"))
pdfmetrics.registerFont(TTFont("SM",  F+"space-mono-latin-400-normal.ttf"))
pdfmetrics.registerFont(TTFont("SMB", F+"space-mono-latin-700-normal.ttf"))
pdfmetrics.registerFont(TTFont("SMI", F+"space-mono-latin-400-italic.ttf"))

OUT = "public/zemo-resume.pdf"
c = canvas.Canvas(OUT, pagesize=(W, H))
c.setTitle("zemo — resume"); c.setAuthor("zemo"); c.setSubject("unspecified")

def y(t): return H - t                     # top-down -> pdf
def txt(x, t, s, font, size, col=INK):
    c.setFont(font, size); c.setFillColor(col); c.drawString(x, y(t), s)
def rtxt(t, s, font, size, col=INK):
    c.setFont(font, size); c.setFillColor(col); c.drawRightString(R, y(t), s)
def rect(x0, top, x1, bottom, col):
    c.setFillColor(col); c.rect(x0, y(bottom), x1-x0, bottom-top, stroke=0, fill=1)

# ---- paper
rect(0, 0, W, H, PAPER)

# ---- hero shapes
c.setFillColor(INK); c.setStrokeColor(INK); c.setLineWidth(2.5)
c.circle(525.28, y(64.0), 34.0, stroke=0, fill=1)
p = c.beginPath()
pts = [(289.94,55.49),(396.67,82.10),(400.06,68.51),(293.33,41.90)]
p.moveTo(pts[0][0], y(pts[0][1]))
for px,py in pts[1:]: p.lineTo(px, y(py))
p.close()
c.setFillColor(RED); c.drawPath(p, stroke=1, fill=1)
c.setFillColor(YEL); c.circle(467.28, y(52.0), 16.0, stroke=1, fill=1)

# ---- wordmark
c.setFont("AB", 58)
c.setFillColor(RED); c.drawString(49, y(95), "ZEMO")
c.setFillColor(INK); c.drawString(46, y(92), "ZEMO")

txt(L, 114, "FULL-STACK DEVELOPER — LOCAL-FIRST · ENCRYPTION · MACHINE LEARNING", "SMB", 10.5)
txt(L, 132, "zemo@tuta.com  ·  github.com/MrEmoji27  ·  hyderabad, india  ·  remote-friendly", "SM", 9.0)
rect(L, 144.6, R, 148.0, INK)

def head(t, label):
    rect(L, t-6.5, L+7.0, t+0.5, RED)
    txt(60.0, t, label, "SMB", 10.0)

GAP = 20.0        # was 22.0 — section gap
cur = 174.0

# ---- SUMMARY (3 lines, was 4)
head(cur, "SUMMARY")
cur += 15.0
for line in [
  "computer science undergraduate (class of 2027) who ships complete products end to end — backend,",
  "frontend, mobile, and the ML inside them. i build software that is fast, private, and genuinely",
  "useful. honest, adaptable, and good in a team — currently proving it at a day job.",
]:
    txt(L, cur, line, "SM", 8.6); cur += 12.0
cur -= 12.0

# ---- EXPERIENCE
cur += GAP + 2.0
head(cur, "EXPERIENCE")
cur += 15.0
txt(L, cur, "app development intern — react native", "SMB", 8.8)
rtxt(cur, "dec 2025 — present", "SM", 8.2)
cur += 12.0
txt(L, cur, "building production mobile applications with react native, full-time.", "SM", 8.2)

# ---- EDUCATION
cur += GAP + 2.0
head(cur, "EDUCATION")
cur += 15.0
txt(L, cur, "b.tech — computer science & engineering", "SMB", 8.8)
rtxt(cur, "2023 — 2027", "SM", 8.2)
cur += 12.0
txt(L, cur, "nalla narsimha reddy group of institutions, hyderabad", "SM", 8.2)

# ---- SKILLS
cur += GAP + 2.0
head(cur, "SKILLS")
cur += 15.0
SKILLS = [
 ("languages",  "python · typescript · javascript · java · c / c# / c++"),
 ("frontend",   "react · react native / expo · vite · tailwind · html/css · tauri (desktop)"),
 ("backend",    "node.js · fastify · express · fastapi · flask · socket.io · webrtc · sqlite"),
 ("data & ml",  "scikit-learn · pandas · numpy · computer vision · ollama / local llms"),
 ("security",   "end-to-end encryption (tweetnacl) · argon2id · jwt · rate limiting"),
 ("agentic ai", "ai-augmented engineering · working with & orchestrating ai agents (claude)"),
]
for i,(k,v) in enumerate(SKILLS):
    txt(L, cur, k, "SMB", 8.6); txt(138.0, cur, v, "SM", 8.6)
    if i < len(SKILLS)-1: cur += 11.8

# ---- PROJECTS
cur += GAP + 2.4
head(cur, "PROJECTS")
cur += 15.0

PROJECTS = [
 ("Zoro", "— local AI chat app", "github.com/MrEmoji27/zore", False, [
   "terminal-styled chat that runs fully on-device via ollama — streaming, persistent sessions, long-term",
   "memory with pinning & categories, file ingestion. fastapi · react · sqlite"]),
 ("Zolt", "— end-to-end encrypted messenger", "product · beta testers wanted", True, [
   "server is a blind relay that never sees plaintext; history lives only on-device. keys in secure storage,",
   "offline queue with auto-delete, webrtc calls. react native · fastify · tweetnacl"]),
 ("EAILS", "— engagement-aware learning system", "github.com/MrEmoji27/EAILS", False, [
   "tracks student engagement by webcam during video lessons; generates personalised quizzes and adapts",
   "pace. team lead — designed the architecture, wrote the entire codebase. flask · mediapipe/opencv · gemini"]),
 ("Anamnesis", "— private desktop diary", "product · beta testers wanted", True, [
   "text + voice journaling, fully local, with ai-readable export for any model you trust.",
   "tauri · typescript · tiptap"]),
 ("spektr", "— terminal spectrum analyser", "github.com/MrEmoji27/spektr", False, [
   "visualises whatever the system is playing — no file, no api, no service. 27 render modes, 40 themes, a",
   "hash-vetted plugin api, locked 60 fps. shipped to pypi and as a windows exe. python · numpy · textual"]),
 ("F1 Machine Learning", "— 2026 season prediction model", "personal research", False, [
   "gradient-boosted championship forecasts from five seasons of race data, time-series validated,",
   "updated as real races finish. python · scikit-learn · fastf1"]),
 ("Zemo's Vault", "— lab archive for cse students", "shipped", False, [
   "interactive archive of lab experiments — browse year > subject > experiment with code and outputs,",
   "plus an arcade mode of mini-games. react · tailwind"]),
 ("Talk to Zemo", "— personal messaging portal", "launching soon", False, [
   "visitors leave a note and find a reply waiting — no accounts. honeypots, rate limits, jwt admin",
   "console. node · express · sqlite"]),
]
for i,(name, sub, right, red, desc) in enumerate(PROJECTS):
    txt(L, cur, name, "SMB", 9.6)
    txt(L + pdfmetrics.stringWidth(name, "SMB", 9.6) + 8.0, cur, sub, "SMI", 8.2)
    rtxt(cur, right, "SM", 7.6, RED if red else INK)
    cur += 11.4
    txt(L, cur, desc[0], "SM", 8.2)
    cur += 10.6
    txt(L, cur, desc[1], "SM", 8.2)
    if i < len(PROJECTS)-1: cur += 16.1

# ---- CURRENTLY
cur += 18.0
head(cur, "CURRENTLY")
cur += 15.0
txt(L, cur, "building two products toward launch this year — zolt & anamnesis. beta testers wanted.", "SMB", 8.6, RED)
cur += 12.0
txt(L, cur, "open to freelance work now, and junior roles after the internship — remote or hyderabad.", "SM", 8.6)
print("content bottom:", round(cur,1), " footer bar top: 789.9")
assert cur < 782, "content overflows into the footer bar"

# ---- footer
rect(0, 789.9, W, 815.9, INK)
txt(L, 807.89, "ZEMO · RESUME · 2026", "SMB", 8.0, PAPER)
rtxt(807.89, "TESTERS WANTED: ZOLT & ANAMNESIS", "SMB", 8.0, RED)

c.showPage(); c.save()
print("wrote", OUT)
