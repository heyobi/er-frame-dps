#!/usr/bin/env python3
"""Bar chart of the first table in results/rankings.md (top 15) -> results/top15_flat.png"""
import sys, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

src = sys.argv[1] if len(sys.argv) > 1 else "results/rankings.md"
out = sys.argv[2] if len(sys.argv) > 2 else "results/top15_flat.png"
rows = []
for line in open(src):
    if line.startswith("### ") and rows:
        break
    m = re.match(r"\| (\d+) \| (.+?) \| (\w[\w ]*?) \| (.+?) \| ([\d,]+) \|", line)
    if m:
        rows.append((f"{m[2]} ({m[3]}, {m[4]})", int(m[5].replace(",", ""))))
rows = rows[:15][::-1]
INK, MUTED, BAR, BG = "#1d1c1a", "#8a877f", "#a8461f", "#ffffff"
fig, ax = plt.subplots(figsize=(9, 6.2), dpi=150)
fig.patch.set_facecolor(BG)
ax.barh([r[0] for r in rows], [r[1] for r in rows], color=BAR, height=0.62)
for i, (_, v) in enumerate(rows):
    ax.text(v + 12, i, f"{v:,}", va="center", fontsize=9, color=INK)
ax.set_xlabel("Light-attack DPS vs flat defense 130 (rune level 150, best spread per weapon)", color=MUTED, fontsize=9)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color("#e3e1db")
ax.tick_params(axis="y", length=0, labelsize=9, colors=INK)
ax.tick_params(axis="x", colors=MUTED, labelsize=8)
ax.grid(axis="x", color="#eeece7", linewidth=0.8)
ax.set_axisbelow(True)
ax.set_xlim(0, max(r[1] for r in rows) * 1.1)
fig.tight_layout()
fig.savefig(out, facecolor=BG)
print(out)
