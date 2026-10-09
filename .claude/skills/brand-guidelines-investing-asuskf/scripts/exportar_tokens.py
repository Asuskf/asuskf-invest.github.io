"""Genera, desde assets/tokens/colors_and_type.css (la ÚNICA fuente), los tokens para Python:

    assets/tokens/tokens.json            {"dark": {...}, "light": {...}, "type": {...}}  → Excel (openpyxl), PDF, scripts
    assets/tokens/asuskf-dark.mplstyle   estilo de matplotlib para notebooks (tema oscuro del sitio)
    assets/tokens/asuskf-light.mplstyle  estilo de matplotlib para documentos e impresión

    python .claude/skills/brand-guidelines-investing-asuskf/scripts/exportar_tokens.py

Nunca editar a mano los archivos generados: cambiar el CSS y volver a correr este script.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
CSS = SKILL / "assets" / "tokens" / "colors_and_type.css"
OUT = SKILL / "assets" / "tokens"


def bloques(css: str) -> dict[str, dict[str, str]]:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out: dict[str, dict[str, str]] = {}
    for sel, cuerpo in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        sel = " ".join(sel.split())
        clave = "light" if 'data-theme="light"' in sel else "dark" if 'data-theme="dark"' in sel else "base" if sel == ":root" else None
        if clave is None:
            continue
        for k, v in re.findall(r"--ak-([\w-]+)\s*:\s*([^;]+);", cuerpo):
            out.setdefault(clave, {})[k] = " ".join(v.split())
    return out


def mplstyle(t: dict[str, str], base: dict[str, str]) -> str:
    hexa = lambda v: v.lstrip("#") if v.startswith("#") else "888888"
    ciclo = ", ".join(f"'{hexa(t[f'series-{i}'])}'" for i in range(1, 5))
    return f"""# Generado por scripts/exportar_tokens.py desde colors_and_type.css — no editar a mano.
figure.facecolor: {hexa(t['bg'])}
axes.facecolor: {hexa(t['surface'])}
savefig.facecolor: {hexa(t['bg'])}
axes.edgecolor: {hexa(t['axis'])}
axes.labelcolor: {hexa(t['text'])}
axes.titlecolor: {hexa(t['gold-ink'])}
axes.titleweight: bold
axes.titlesize: 13
axes.titlelocation: left
axes.spines.top: False
axes.spines.right: False
axes.grid: True
axes.grid.axis: y
grid.color: {hexa(t['axis'])}
grid.alpha: 0.18
grid.linewidth: 0.6
axes.prop_cycle: cycler('color', [{ciclo}])
lines.linewidth: 2
lines.solid_capstyle: round
patch.edgecolor: {hexa(t['surface'])}
xtick.color: {hexa(t['axis'])}
ytick.color: {hexa(t['axis'])}
xtick.labelcolor: {hexa(t['text-muted'])}
ytick.labelcolor: {hexa(t['text-muted'])}
text.color: {hexa(t['text'])}
legend.frameon: False
legend.labelcolor: {hexa(t['text'])}
font.family: sans-serif
font.sans-serif: Roboto, DejaVu Sans
font.monospace: Roboto Mono, DejaVu Sans Mono
font.size: 10
figure.dpi: 110
"""


if __name__ == "__main__":
    b = bloques(CSS.read_text(encoding="utf-8"))
    dark, light, base = b["dark"], {**b["dark"], **b["light"]}, b.get("base", {})
    (OUT / "tokens.json").write_text(json.dumps({"dark": dark, "light": light, "type": base}, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "asuskf-dark.mplstyle").write_text(mplstyle(dark, base), encoding="utf-8")
    (OUT / "asuskf-light.mplstyle").write_text(mplstyle(light, base), encoding="utf-8")
    print(f"tokens: oscuro {len(dark)} · claro {len(b['light'])} (resto heredado) · tipo/espacio {len(base)} → tokens.json, *.mplstyle")
