# Lente Apple HIG — cómo se combina con la marca Asuskf

La skill **`apple-design`** (instalada en `.claude/skills/apple-design/`, origen en su `ORIGEN.md`) aporta la **revisión de UI**
basada en las Human Interface Guidelines de Apple y una lente de oficio de diseño. Esta marca la usa así:

- **La marca decide la identidad** (paleta, tipografías, logo, tono): manda este SKILL.md.
- **Las HIG deciden la usabilidad** (jerarquía, legibilidad, objetivos táctiles, modo oscuro, accesibilidad, movimiento, gráficas):
  manda `apple-design`. Si chocan, se resuelve a favor de la accesibilidad y se documenta en el CHANGELOG.

## Cuándo invocarla

Antes de entregar cualquier pantalla, página o tablero de marca Asuskf (sitio de consulta, dashboard, landing), pedir una revisión con
`apple-design` (o `/apple-design`). Seguir su método: cargar `references/hig-lookup.md`, el conjunto de siempre (accesibilidad,
layout, tipografía, color, plus `cross-platform.md` porque esto es web) y las páginas del caso.

## Páginas HIG que más aplican a esta marca

| Tema de la marca | Página en `apple-design/references/hig/` | Secciones |
|---|---|---|
| Oro como acento, verde/rojo como estado | `color.md` | Best practices · Inclusive color |
| Tema oscuro por defecto + tema claro | `dark-mode.md` | Best practices · Dark Mode colors |
| Playfair + Roboto + Roboto Mono | `typography.md` | Ensuring legibility · Conveying hierarchy · Using custom fonts |
| Gráficas de rendimiento, heatmap | `charts.md`, `charting-data.md` | Marks · Axes · Color · Enhancing the accessibility of a chart |
| Gauge de precisión | `gauges.md` | Anatomy · Best practices |
| Tablas de trades / matriz | `lists-and-tables.md` | Best practices · Style |
| Botón dorado "Copiar Portafolio" | `buttons.md` | Best practices · Style · Role |
| Barra translúcida con blur | `materials.md` | Standard materials |
| Aparición `reveal`, hover | `motion.md` | Best practices · Providing feedback |
| Jerarquía del hero y grid | `layout.md` | Visual hierarchy · Adaptability |
| Contraste, daltonismo, movimiento reducido | `accessibility.md` | Vision · Cognitive |
| Uso del logo/insignia | `branding.md` | Best practices |

## Traducción a reglas de esta marca (en nuestras palabras)

1. **Contenido primero:** el oro marca lo importante; si todo es dorado, nada lo es. Oro ≤ ~10 % de la superficie.
2. **Objetivos táctiles ≥ 44 px** (`--ak-hit-min`) en botones, chips y filas clicables.
3. **Contraste:** texto ≥ 4.5:1 (cuerpo) y ≥ 3:1 (texto grande y marcas de gráfica). Por eso existe `--ak-gold-ink` en el tema claro.
4. **El color nunca es la única señal:** ganancia/pérdida con signo o flecha; heatmap con el número; estados con texto ("✔ cumple").
5. **Respetar `prefers-reduced-motion`:** los tokens de duración caen a 0 (ya está en `colors_and_type.css`).
6. **Tipografía escalable:** tamaños con `clamp()` y unidades relativas; nada de texto en imágenes.
7. **Materiales:** el blur de la barra superior solo sobre contenido que se desplaza; nunca blur sobre texto que hay que leer.
8. **Coherencia de plataforma:** en web, patrones web (enlaces subrayados al pasar, foco visible `:focus-visible`), no imitar controles de iOS.
