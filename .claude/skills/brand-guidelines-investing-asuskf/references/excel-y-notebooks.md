# Excel, notebooks y PDF — Asuskf Investing

Los colores salen de `assets/tokens/tokens.json` (generado desde el CSS). Nunca hex literales en el código.

## Excel (openpyxl) — p. ej. `src/hoja.py`

```python
import json, pathlib
from openpyxl.styles import Font, PatternFill, Alignment
T = json.loads(pathlib.Path(".claude/skills/brand-guidelines-investing-asuskf/assets/tokens/tokens.json").read_text(encoding="utf-8"))
C = T["light"]                          # Excel se imprime y se lee sobre blanco: tema CLARO
hx = lambda v: v.lstrip("#").upper()

cabecera = dict(font=Font(name="Roboto", bold=True, color="FFFFFF"),            # texto blanco sobre verde insignia (12:1)
                fill=PatternFill("solid", fgColor=hx(C["brand-green"])),
                alignment=Alignment(wrap_text=True, vertical="center"))
eyebrow  = Font(name="Roboto", bold=True, color=hx(C["gold-ink"]), size=9)     # oro TINTA, nunca oro de marca como texto
numero   = Font(name="Roboto Mono", color=hx(C["text"]))
ganancia = Font(name="Roboto Mono", color=hx(C["gain"]), bold=True)
perdida  = Font(name="Roboto Mono", color=hx(C["loss"]), bold=True)
fila_alt = PatternFill("solid", fgColor=hx(C["surface-2"]))
```

- Encabezado: verde insignia + blanco; congelar paneles y autofiltro.
- Cifras en Roboto Mono, formato `0.0%` / `#,##0` / `+0.0%;−0.0%` para rendimientos (signo siempre visible).
- Ganancia/pérdida: color de estado **y** signo; heatmaps con escala de color condicional usando `heat-*` del tema claro.
- Si el equipo que abre el Excel no tiene Roboto instalado, Excel cae a su fuente por defecto: es aceptable; no incrustar.
- Hoja "Léeme" con el aviso legal (no es recomendación de inversión; rendimientos pasados no garantizan futuros).

## Notebooks (matplotlib)

`plt.style.use(".../asuskf-dark.mplstyle")` para análisis en pantalla; `asuskf-light.mplstyle` para lo que se exporta a PDF o se
imprime. Registrar las fuentes con `font_manager.addfont` (ver `charts.md`). Títulos de figura a la izquierda, en oro tinta.

## PDF (HTML → Imprimir → Guardar como PDF)

Tema **claro** (`data-theme="light"`), banda superior en `--ak-brand-green` con la insignia (desde archivo) y el nombre en Playfair
Display blanco; cuerpo Roboto; cifras Roboto Mono; pie con aviso legal en `.ak-legal` y número de página. Márgenes de 16 mm.
