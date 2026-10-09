# Gráficas y visualización de datos — Asuskf Investing

Método: el de la skill `dataviz` (forma → color por función → validar → marcas → hover → accesibilidad). Aquí solo van los
**parámetros de marca** que ese método consume. Validación hecha el 2026-10-08 con `dataviz/scripts/validate_palette.js`.

## Parámetros de marca

| Parámetro | Oscuro (sobre `--ak-surface` #111E1A) | Claro (sobre #FFFFFF) |
|---|---|---|
| Categórico, orden fijo | `--ak-series-1` #A8862A oro · `-2` #3D8BD4 azul · `-3` #C96B45 terracota · `-4` #A77FD6 violeta | #A8862A · #2F78C4 · #C05F36 · #8A5CC9 |
| Validación (pares adyacentes) | ✔ banda de luminosidad, croma, CVD ΔE ≥ 20, visión normal ≥ 20, contraste ≥ 3:1 | ✔ todo; CVD ΔE ≥ 21, contraste ≥ 3:1 |
| Todos los pares (dispersión, burbujas, mapas, small multiples) | **máximo 2 series**: oro + azul. Oro y terracota se confunden (ΔE 2.0 deutan) → con 3+ series, facetar | igual |
| Secuencial (magnitud) | una sola tonalidad: oro (`--ak-gold-deep` → `--ak-gold-light`) o azul | igual |
| Divergente (rendimiento) | rojo `--ak-heat-loss*` ↔ neutro `--ak-heat-neutral` ↔ verde `--ak-heat-gain*` **con el número en la celda** | tokens claros |
| Estado (reservado) | `--ak-gain` #4CAF70 · `--ak-loss` #E57373 — solo ganancia/pérdida, siempre con signo o ▲▼ | #1F7A45 · #B3403F |
| Rejilla / ejes | `--ak-grid` · `--ak-axis` (Roboto, 11px) | idem claro |
| Sombreado de periodos | `--ak-band` (p. ej. años "buena empresa") | idem |

> **Por qué el oro de serie no es el oro de marca:** #D4AF37 tiene luminosidad OKLCH 0.77 y en fondo oscuro queda fuera de la banda
> de series (0.48–0.67); se lee como "resaltado", no como una serie más. El oro de marca se reserva para títulos, KPI destacados y el
> sombreado de periodos; las líneas usan #A8862A.

## Reglas

1. **Un eje por gráfica.** Dos magnitudes distintas → dos gráficas o índice base 100.
2. **Color por entidad, no por rango:** filtrar no repinta a las sobrevivientes.
3. Verde/rojo **solo** para ganancia/pérdida (y el heatmap). Nunca como serie categórica.
4. Líneas de 2 px, extremos redondeados; marcadores de 8 px solo al pasar el mouse; barras con 2 px de separación del fondo.
5. Leyenda siempre con ≥ 2 series y etiqueta directa al final de cada línea (≤ 4 series). Texto en colores de texto, nunca en el color de la serie.
6. Hover por defecto: cruz + tooltip con todas las series en esa X; el valor en Roboto Mono **antes** de la etiqueta.
7. Tabla de datos como vista alternativa (el aqua/terracota claro necesita ese respaldo de accesibilidad).
8. Línea de referencia (umbral, PER 15x, ROIC 15 %) punteada en `--ak-axis` con etiqueta corta.
9. Gauge (como el del sitio): arco gris `--ak-surface-2`, relleno oro, valor en Roboto Mono 700 al centro; animar solo si no hay `prefers-reduced-motion`.
10. Cifras grandes (KPI) en Roboto Mono 700 tracking −1px; ganancia/pérdida con su color **y** signo.

## matplotlib (notebooks)

```python
import matplotlib.pyplot as plt
plt.style.use(".claude/skills/brand-guidelines-investing-asuskf/assets/tokens/asuskf-dark.mplstyle")   # o asuskf-light
```
Para que use Roboto, registrar los TTF una vez por sesión:
```python
from matplotlib import font_manager as fm
for f in ("roboto.ttf", "roboto-mono.ttf", "playfair-display.ttf"):
    fm.fontManager.addfont(f".claude/skills/brand-guidelines-investing-asuskf/assets/fonts/{f}")
```

## SVG propio (como `src/web/fintkg.js`)

Mapear las series a `var(--ak-series-n)` y los sombreados a `var(--ak-band)`; no escribir hex en el JS.
