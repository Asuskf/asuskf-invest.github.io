"""Genera Asuskf_Brand_Cheatsheet.html (autocontenido: tokens, fuentes y logo incrustados; sin internet).

    python .claude/skills/brand-guidelines-investing-asuskf/assets/quick-reference/build_cheatsheet.py

Nivel 2: no editar el HTML a mano; cambiar tokens/este script y volver a correr. Los datos de la gráfica y del heatmap son
ILUSTRATIVOS (se rotulan así): no son rendimientos reales.
"""
from __future__ import annotations

import base64
import json
import re
from pathlib import Path

SKILL = Path(__file__).resolve().parents[2]
A = SKILL / "assets"
CSS_TOKENS = (A / "tokens" / "colors_and_type.css").read_text(encoding="utf-8")
T = json.loads((A / "tokens" / "tokens.json").read_text(encoding="utf-8"))


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode()


def face(fam: str, f: str, estilo: str = "normal", pesos: str = "100 900") -> str:
    return (f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,{b64(A / 'fonts' / f)}) format('woff2');"
            f"font-weight:{pesos};font-style:{estilo};font-display:swap}}")


FUENTES = "\n".join([face("Playfair Display", "playfair-display.woff2", pesos="400 900"),
                     face("Playfair Display", "playfair-display-italic.woff2", "italic", "400 900"),
                     face("Roboto", "roboto.woff2"), face("Roboto", "roboto-italic.woff2", "italic"),
                     face("Roboto Mono", "roboto-mono.woff2", pesos="100 700")])
LOGO = b64(A / "logos" / "asuskf-badge-128.png")
FAV = b64(A / "logos" / "asuskf-badge-32.png")

SWATCH = [("Bosque 900", "bg"), ("Bosque 950", "bg-deep"), ("Tarjeta", "surface"), ("Elevado", "surface-2"), ("Verde insignia", "brand-green"),
          ("Oro metálico", "gold"), ("Oro claro", "gold-light"), ("Oro profundo", "gold-deep"), ("Oro tinta", "gold-ink"), ("Texto", "text"),
          ("Apagado", "text-muted"), ("Fuerte", "text-strong"), ("Ganancia", "gain"), ("Pérdida", "loss")]
SERIES = [("Serie 1 · oro", "series-1"), ("Serie 2 · azul", "series-2"), ("Serie 3 · terracota", "series-3"), ("Serie 4 · violeta", "series-4")]


def swatches(lista) -> str:
    return "".join(
        f'<div class="sw"><div class="chip" style="background:var(--ak-{k})"></div><b>{n}</b>'
        f'<code>--ak-{k}</code><span class="ak-num hx" data-k="{k}"></span></div>' for n, k in lista)


# gráfica ilustrativa: 3 series, 8 puntos (índice base 100), SVG con tooltips nativos
X = list(range(2018, 2026))
Y = {"series-1": [100, 112, 108, 131, 126, 149, 158, 171], "series-2": [100, 104, 99, 118, 109, 121, 133, 139],
     "series-3": [100, 96, 101, 107, 98, 112, 117, 120]}
NOM = {"series-1": "Estrategia A", "series-2": "Estrategia B", "series-3": "Índice"}
W, H, ML, MR, MT, MB = 560, 240, 44, 96, 12, 28
lo, hi = 90, 180
px = lambda i: ML + i * (W - ML - MR) / (len(X) - 1)
py = lambda v: MT + (hi - v) / (hi - lo) * (H - MT - MB)
svg = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Gráfica ilustrativa: índice base 100">']
for v in range(lo, hi + 1, 30):
    svg.append(f'<line x1="{ML}" x2="{W - MR}" y1="{py(v):.1f}" y2="{py(v):.1f}" stroke="var(--ak-grid)"/>'
               f'<text x="{ML - 6}" y="{py(v) + 4:.1f}" text-anchor="end" class="eje">{v}</text>')
svg.append(f'<line x1="{ML}" x2="{W - MR}" y1="{py(100):.1f}" y2="{py(100):.1f}" stroke="var(--ak-axis)" stroke-dasharray="4 4"/>'
           f'<text x="{ML + 4}" y="{py(100) - 5:.1f}" class="eje">base 100</text>')
for i, x in enumerate(X):
    if i % 2 == 0:
        svg.append(f'<text x="{px(i):.1f}" y="{H - 8}" text-anchor="middle" class="eje">{x}</text>')
fin = []
for k, ys in Y.items():
    d = " ".join(f"{'M' if i == 0 else 'L'}{px(i):.1f},{py(v):.1f}" for i, v in enumerate(ys))
    svg.append(f'<path d="{d}" fill="none" stroke="var(--ak-{k})" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    for i, v in enumerate(ys):
        svg.append(f'<circle cx="{px(i):.1f}" cy="{py(v):.1f}" r="9" fill="transparent"><title>{NOM[k]} · {X[i]}: {v}</title></circle>')
    fin.append([py(ys[-1]), NOM[k]])
fin.sort()
for j in range(1, len(fin)):
    fin[j][0] = max(fin[j][0], fin[j - 1][0] + 13)
svg += [f'<text x="{W - MR + 6}" y="{y + 4:.1f}" class="etq">{n}</text>' for y, n in fin]
svg.append("</svg>")

HEAT = [("2024", [1.8, -0.6, 3.2, 0.1, -2.4, 4.9]), ("2025", [-1.1, 2.7, 0.0, -3.8, 1.2, 0.6])]


def celda(v: float) -> str:
    c = "g2" if v >= 3 else "g1" if v > 0.25 else "l2" if v <= -3 else "l1" if v < -0.25 else "n"
    return f'<td class="{c}">{"+" if v > 0 else "−" if v < 0 else ""}{abs(v):.1f}%</td>'


heat = ('<table class="ak-heat"><thead><tr><th></th>' + "".join(f"<th>{m}</th>" for m in ["Ene", "Feb", "Mar", "Abr", "May", "Jun"])
        + "</tr></thead><tbody>" + "".join(f"<tr><td>{a}</td>{''.join(celda(v) for v in vs)}</tr>" for a, vs in HEAT) + "</tbody></table>")

HTML = f"""<!doctype html>
<html lang="es" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Asuskf Brand Cheatsheet</title><link rel="icon" href="data:image/png;base64,{FAV}">
<style>
{FUENTES}
{CSS_TOKENS}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--ak-bg);color:var(--ak-text);font:var(--ak-fs-body)/var(--ak-lh-body) var(--ak-font-body);-webkit-font-smoothing:antialiased}}
h1,h2,h3{{font-family:var(--ak-font-heading);color:var(--ak-gold-ink);margin:0}}
main{{max-width:var(--ak-container);margin:0 auto;padding:var(--ak-space-6) var(--ak-gutter) var(--ak-space-8)}}
.ak-nav{{position:sticky;top:0;z-index:5;display:flex;justify-content:space-between;align-items:center;gap:var(--ak-space-4);flex-wrap:wrap;
 padding:var(--ak-space-3) var(--ak-gutter);background:var(--ak-nav-bg);backdrop-filter:blur(12px);border-bottom:1px solid var(--ak-border)}}
.marca{{display:flex;align-items:center;gap:var(--ak-space-3)}}
.ak-logo{{height:42px;width:auto;border-radius:var(--ak-radius-pill);border:1.5px solid var(--ak-gold)}}
.ak-wordmark{{font-family:var(--ak-font-heading);font-weight:700;font-size:20px;color:var(--ak-gold-ink);letter-spacing:1px}}
.ak-eyebrow{{font-size:var(--ak-fs-eyebrow);text-transform:uppercase;letter-spacing:var(--ak-track-eyebrow);color:var(--ak-gold-ink);font-weight:500}}
.ak-btn{{display:inline-flex;align-items:center;min-height:var(--ak-hit-min);padding:0 22px;border-radius:var(--ak-radius);background:var(--ak-gold);
 color:var(--ak-on-gold);font:700 var(--ak-fs-small) var(--ak-font-body);text-transform:uppercase;letter-spacing:1px;border:0;cursor:pointer;
 transition:background-color var(--ak-dur) var(--ak-ease),transform var(--ak-dur-fast) var(--ak-ease),box-shadow var(--ak-dur) var(--ak-ease)}}
.ak-btn:hover{{background:var(--ak-gold-light);transform:translateY(-1px);box-shadow:var(--ak-glow-gold)}}
.ak-btn:focus-visible{{outline:2px solid var(--ak-gold-light);outline-offset:3px}}
.ak-btn--ghost{{background:transparent;color:var(--ak-gold-ink);border:1px solid var(--ak-border-hover)}}
.ak-card{{background:var(--ak-surface);border:1px solid var(--ak-border);border-radius:var(--ak-radius);padding:var(--ak-space-5);box-shadow:var(--ak-shadow)}}
.ak-card h3{{font:500 var(--ak-fs-label) var(--ak-font-body);text-transform:uppercase;letter-spacing:var(--ak-track-label);color:var(--ak-gold-ink);margin-bottom:var(--ak-space-3)}}
.ak-num{{font-family:var(--ak-font-mono);font-variant-numeric:tabular-nums}}
.ak-kpi{{font:700 var(--ak-fs-kpi) var(--ak-font-mono);letter-spacing:-1px;color:var(--ak-text-strong)}}
.ak-kpi--gain{{color:var(--ak-gain)}}.ak-kpi--loss{{color:var(--ak-loss)}}
.ak-badge{{display:inline-block;padding:2px 8px;border-radius:var(--ak-radius-sm);font-size:var(--ak-fs-label);font-weight:700;letter-spacing:.5px}}
.ak-badge--gain{{background:var(--ak-gain-bg);color:var(--ak-gain)}}.ak-badge--loss{{background:var(--ak-loss-bg);color:var(--ak-loss)}}
.ak-legal{{font-size:var(--ak-fs-micro);color:var(--ak-text-muted);font-style:italic}}
.ak-divider{{height:1px;width:160px;background:linear-gradient(90deg,var(--ak-gold),transparent);border:0;margin:var(--ak-space-4) 0}}
.hero{{background:var(--ak-brand-green);border-radius:var(--ak-radius);padding:var(--ak-space-7) var(--ak-space-6);margin:var(--ak-space-5) 0}}
.hero h1{{font-size:var(--ak-fs-hero);letter-spacing:4px;color:var(--ak-text-strong);line-height:1.05}}
.hero .sub{{font-weight:300;letter-spacing:2px;color:var(--ak-text)}}
[data-theme="light"] .hero .sub{{color:var(--ak-text-strong)}}
.stats{{display:flex;gap:var(--ak-space-6);flex-wrap:wrap;margin-top:var(--ak-space-5)}}
.stats div{{display:flex;flex-direction:column;border-left:1px solid var(--ak-border);padding-left:var(--ak-space-4)}}
.stats b{{font:700 var(--ak-fs-stat) var(--ak-font-mono);color:var(--ak-text-strong)}}
.stats span{{font-size:var(--ak-fs-micro);text-transform:uppercase;letter-spacing:1.5px;color:var(--ak-text-muted)}}
[data-theme="light"] .hero b,[data-theme="light"] .hero h1{{color:var(--ak-text-strong)}}
section{{margin-top:var(--ak-space-7)}}
section>h2{{font-size:var(--ak-fs-h2);margin:var(--ak-space-2) 0 var(--ak-space-4)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:var(--ak-space-3)}}
.grid2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:var(--ak-space-4)}}
.sw{{background:var(--ak-surface);border:1px solid var(--ak-divider);border-radius:var(--ak-radius);padding:var(--ak-space-3);display:flex;flex-direction:column;gap:2px;font-size:var(--ak-fs-small)}}
.sw .chip{{height:56px;border-radius:var(--ak-radius-sm);border:1px solid var(--ak-divider);margin-bottom:var(--ak-space-2)}}
.sw code{{font-size:var(--ak-fs-label);color:var(--ak-text-muted)}}.sw .hx{{font-size:var(--ak-fs-small);color:var(--ak-text)}}
.tipo p{{margin:var(--ak-space-2) 0}}
.ak-heat{{border-collapse:separate;border-spacing:2px;width:100%}}
.ak-heat td{{font:400 12px var(--ak-font-mono);text-align:center;padding:6px;border-radius:var(--ak-radius-sm)}}
.ak-heat td:first-child{{font:700 14px var(--ak-font-heading);color:var(--ak-text);text-align:left;background:transparent}}
.ak-heat th{{color:var(--ak-gold-ink);font:500 var(--ak-fs-label) var(--ak-font-body);text-transform:uppercase;letter-spacing:.5px}}
.ak-heat .g2{{background:var(--ak-heat-gain-strong);color:var(--ak-heat-gain-strong-ink)}}.ak-heat .g1{{background:var(--ak-heat-gain);color:var(--ak-heat-gain-ink)}}
.ak-heat .n{{background:var(--ak-heat-neutral);color:var(--ak-text-muted)}}
.ak-heat .l1{{background:var(--ak-heat-loss);color:var(--ak-heat-loss-ink)}}.ak-heat .l2{{background:var(--ak-heat-loss-strong);color:var(--ak-heat-loss-strong-ink)}}
.ak-card{{min-width:0}}.desliza{{overflow-x:auto}}svg{{width:100%;max-width:760px;height:auto;display:block}}svg .eje{{font:11px var(--ak-font-body);fill:var(--ak-axis)}}svg .etq{{font:12px var(--ak-font-body);fill:var(--ak-text)}}
.leyenda{{display:flex;gap:var(--ak-space-4);flex-wrap:wrap;font-size:var(--ak-fs-small);margin-bottom:var(--ak-space-2)}}
.leyenda i{{display:inline-block;width:14px;height:3px;border-radius:2px;margin-right:6px;vertical-align:3px}}
ul.reglas{{margin:0;padding-left:var(--ak-space-5)}}ul.reglas li{{margin:var(--ak-space-1) 0}}
.no{{color:var(--ak-loss);font-weight:700}}.si{{color:var(--ak-gain);font-weight:700}}
</style></head><body>
<header class="ak-nav"><div class="marca"><img class="ak-logo" src="data:image/png;base64,{LOGO}" alt="Asuskf Investing"><span class="ak-wordmark">Asuskf Investing</span></div>
<div style="display:flex;gap:var(--ak-space-3);align-items:center"><span class="ak-eyebrow">Brand cheatsheet v1.0</span>
<button class="ak-btn ak-btn--ghost" id="tema" aria-pressed="false">Tema claro</button></div></header>
<main>
<div class="hero"><div class="ak-eyebrow">Inversión cuantitativa e inteligencia artificial</div>
<h1>ASUSKF INVESTING</h1><hr class="ak-divider"><div class="sub">Gestión sistemática · Control de riesgo · Decisiones basadas en datos</div>
<div class="stats"><div><b>+00.0%</b><span>Cifra ejemplo</span></div><div><b>0 años</b><span>Cifra ejemplo</span></div><div><b>AI + Quant</b><span>Metodología</span></div></div>
<p class="ak-legal" style="margin-top:var(--ak-space-4)">Cifras de ejemplo para mostrar el estilo; no son rendimientos reales.</p></div>

<section><div class="ak-eyebrow">02 · Color</div><h2>Paleta de marca</h2>
<div class="grid">{swatches(SWATCH)}</div>
<p class="ak-legal">Proporción: bosque ≈ 85 % · texto 5-10 % · oro ≤ 10 % · verde/rojo solo como estado de ganancia/pérdida.
En tema claro el oro no se usa como texto (1.9:1): se usa el oro tinta (5.5:1).</p></section>

<section><div class="ak-eyebrow">Gráficas</div><h2>Series categóricas (orden fijo, validadas para daltonismo)</h2>
<div class="grid">{swatches(SERIES)}</div></section>

<section class="tipo"><div class="ak-eyebrow">03 · Tipografía</div><h2>Playfair Display · Roboto · Roboto Mono</h2>
<div class="grid2"><div class="ak-card"><h3>Títulos — Playfair Display</h3><p style="font:700 40px/1.1 var(--ak-font-heading);color:var(--ak-gold-ink)">Valor a largo plazo</p>
<p style="font:400 22px var(--ak-font-heading);color:var(--ak-text-strong)">Investment Research · Market Insights</p></div>
<div class="ak-card"><h3>Texto — Roboto</h3><p>Invertimos con análisis cuantitativo y visión macroeconómica para identificar oportunidades con ventaja estadística.
Cuerpo 15 px, interlineado 1.65.</p><p style="font-weight:300;letter-spacing:2px">Subtítulo 300 · tracking 2 px</p></div>
<div class="ak-card"><h3>Cifras — Roboto Mono</h3><div class="ak-kpi ak-kpi--gain">+12.4%</div><div class="ak-kpi ak-kpi--loss">−3.1%</div>
<p class="ak-num" style="color:var(--ak-text-muted)">2026-10-08 · 1,234.56 · 0.87</p></div></div></section>

<section><div class="ak-eyebrow">05 · Componentes</div><h2>Botones, tarjetas, estado</h2>
<div class="grid2"><div class="ak-card"><h3>Botones</h3><div style="display:flex;gap:var(--ak-space-3);flex-wrap:wrap">
<button class="ak-btn">Copiar portafolio</button><button class="ak-btn ak-btn--ghost">Ver insights</button></div>
<p class="ak-legal">Alto mínimo 44 px (Apple HIG) · texto bosque sobre oro (8.7:1) · foco visible.</p></div>
<div class="ak-card"><h3>KPI con estado</h3><div class="ak-kpi">78%</div><div style="margin-top:var(--ak-space-2)"><span class="ak-badge ak-badge--gain">▲ +2.1 pp</span>
<span class="ak-badge ak-badge--loss">▼ −0.8 pp</span></div><p class="ak-legal">Color + signo/flecha: nunca solo color.</p></div>
<div class="ak-card"><h3>Heatmap de rendimientos (ilustrativo)</h3><div class="desliza">{heat}</div><p class="ak-legal">El número va en cada celda: el rojo/verde no es legible para todos.</p></div></div></section>

<section><div class="ak-eyebrow">Gráficas</div><h2>Línea — índice base 100 (datos ilustrativos)</h2>
<div class="ak-card"><div class="leyenda"><span><i style="background:var(--ak-series-1)"></i>Estrategia A</span><span><i style="background:var(--ak-series-2)"></i>Estrategia B</span>
<span><i style="background:var(--ak-series-3)"></i>Índice</span></div>{"".join(svg)}
<p class="ak-legal">Un eje · leyenda + etiqueta directa · pasa el mouse sobre un punto · verde/rojo nunca como serie.</p></div></section>

<section><div class="ak-eyebrow">Reglas</div><h2>Sí / No</h2>
<div class="grid2"><div class="ak-card"><h3>Sí</h3><ul class="reglas"><li><span class="si">✔</span> Tokens <code>var(--ak-…)</code>, fuentes locales</li>
<li><span class="si">✔</span> Insignia desde archivo, con su borde dorado</li><li><span class="si">✔</span> Cifras en Roboto Mono con signo</li>
<li><span class="si">✔</span> Aviso: no es recomendación de inversión</li><li><span class="si">✔</span> Revisión de usabilidad con la skill apple-design</li></ul></div>
<div class="ak-card"><h3>No</h3><ul class="reglas"><li><span class="no">✖</span> Google Fonts o CDN en entregables</li>
<li><span class="no">✖</span> Redibujar, recortar o recolorear la insignia</li><li><span class="no">✖</span> Oro como texto sobre fondo claro</li>
<li><span class="no">✖</span> Usar la marca eToro para insinuar respaldo</li><li><span class="no">✖</span> Inventar cifras o prometer rendimientos</li></ul></div></div></section>
<p class="ak-legal" style="margin-top:var(--ak-space-7)">Asuskf Investing · guía de marca para el repositorio FinTKG · contenido informativo, no es recomendación de inversión.
Rendimientos pasados no garantizan resultados futuros.</p>
</main>
<script>
const T={json.dumps({"dark": T["dark"], "light": T["light"]}, ensure_ascii=False)};
function pinta(){{const t=document.documentElement.dataset.theme;document.querySelectorAll('.hx').forEach(e=>{{e.textContent=(T[t][e.dataset.k]||'').toUpperCase()}})}}
const b=document.getElementById('tema');
b.onclick=()=>{{const h=document.documentElement,l=h.dataset.theme==='dark';h.dataset.theme=l?'light':'dark';b.textContent=l?'Tema oscuro':'Tema claro';b.setAttribute('aria-pressed',l);pinta()}};
pinta();
</script></body></html>"""

ruta = Path(__file__).with_name("Asuskf_Brand_Cheatsheet.html")
ruta.write_text(HTML, encoding="utf-8")
literales = [m for m in re.findall(r"#[0-9a-fA-F]{6}\b", HTML.split("<style>")[1].split("</style>")[0].split(CSS_TOKENS)[-1])]
print(f"{ruta} · {ruta.stat().st_size / 1e3:.0f} KB · hex literales fuera de los tokens: {len(literales)}")
