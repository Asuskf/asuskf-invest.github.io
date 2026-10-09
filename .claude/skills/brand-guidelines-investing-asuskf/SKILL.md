---
name: brand-guidelines-investing-asuskf
description: Identidad visual de Asuskf Investing (inversión cuantitativa e IA) para el repositorio FinTKG y el sitio público asuskf-invest.github.io — paleta bosque profundo + oro metálico, Playfair Display / Roboto / Roboto Mono, insignia circular, verde/rojo solo para ganancia/pérdida, heatmap de rendimientos, KPI en mono, temas oscuro y claro, paleta de gráficas validada para daltonismo, más la lente de revisión de UI de Apple HIG (skill apple-design). Úsala siempre que se cree o reestilice algo con la marca Asuskf o "asuskf invest" — el sitio público asuskf-invest.github.io, el sitio de consulta de FinTKG (outputs/sitio), dashboards, páginas HTML, gráficas de notebooks, Excel, PDF o presentaciones — o cuando pidan "ponlo con la marca de asuskf", "colores de asuskf", "estilo del sitio asuskf-invest", "revisa el diseño con las guías de Apple".
---

# Asuskf Investing — Guía de identidad visual

> **Versión** 1.2 · **Fecha** 2026-10-08 · **Alcance:** repositorio FinTKG y sitio público asuskf-invest.github.io · historial en `CHANGELOG.md`.
>
> **Canon de origen = el sitio público** https://asuskf.github.io/asuskf-invest.github.io/ (copia del 2026-10-08 en
> `assets/source/sitio/`, procedencia y SHA-256 en `assets/source/FUENTES.md`). Esta skill es su **exportación para agentes**:
> convierte el CSS del sitio en tokens, agrega un tema claro validado, una paleta de gráficas validada y las reglas de uso.
> Si el sitio cambia, se vuelve a descargar y se actualizan los tokens; el sitio gana.
>
> Estructura tomada de la guía de Kin (`brand-guidelines-kin`); la lente de usabilidad viene de la skill **`apple-design`**
> (Apple Human Interface Guidelines), instalada en `.claude/skills/apple-design/`.

## AUTORIDAD DE ARCHIVOS

**Nivel 1 — canon**
- `SKILL.md` (este archivo) — reglas.
- `assets/tokens/colors_and_type.css` — **fuente única** de color, tipografía, espacio, radio y movimiento.
- `assets/logos/`, `assets/banner/`, `assets/fonts/` — archivos oficiales (logo y banner = originales del sitio).
- `references/*.md` — código por formato.

**Nivel 2 — generados (no editar a mano; regenerar)**
- `assets/tokens/tokens.json`, `asuskf-dark.mplstyle`, `asuskf-light.mplstyle` ← `scripts/exportar_tokens.py`.
- `assets/quick-reference/Asuskf_Brand_Cheatsheet.html` ← `assets/quick-reference/build_cheatsheet.py`.

## REGLAS DURAS (cada violación bloquea la entrega)

1. **Sin colores escritos a mano.** Nada de `#hex`/`rgb()` literales en entregables: `var(--ak-…)` o `tokens.json`.
2. **Sin px sueltos** cuando existe token (espacio, radio, tamaños de texto).
3. **Sin fuentes externas.** Solo Playfair Display, Roboto y Roboto Mono **locales** (`assets/fonts/`). Nada de Google Fonts/CDN,
   aunque el sitio público los use.
4. **Sin imports de internet.** Todo entregable funciona sin conexión.
5. **El logo nunca se redibuja.** La insignia circular se coloca **desde archivo** (`assets/logos/`), en proporción original, con su
   borde dorado. No se recorta, recolorea, vectoriza ni "aproxima". Si ningún archivo sirve, se deja el espacio vacío y se avisa.
6. **Marca de tercero:** la insignia y el banner incluyen la marca de **eToro**. Se usan tal cual, sin editar, y **nunca** para sugerir
   que eToro respalda o produce un contenido. En piezas que no son sobre el perfil de eToro, usar solo el nombre "Asuskf Investing".
7. **Verde/rojo son estado, no decoración:** solo para ganancia/pérdida y heatmaps, siempre acompañados de signo, flecha o número.
8. **Toda cifra financiera en Roboto Mono** (tabulares). Signo menos real (−, U+2212).
9. **Aviso legal** en todo entregable con cifras de inversión: es información/análisis, **no recomendación de inversión**; rendimientos
   pasados no garantizan resultados futuros. **No inventar cifras.**

## Temas — oscuro por defecto, claro para documentos

Todos los colores son variables en `:root` / `[data-theme="dark"]` (default, como el sitio) y se sobrescriben en
`[data-theme="light"]`. El **verde insignia** (`--ak-brand-green`) es igual en ambos. En el tema claro el oro **no** se usa como texto
(1.9:1): se usa `--ak-gold-ink` (#7A5F0E, 5.5:1).

---

## 01 — Logo

| Archivo | Uso |
|---|---|
| `assets/logos/asuskf-badge.png` (500 px, fondo transparente) | encabezados grandes, portadas, impresión |
| `asuskf-badge-256.png` · `-128.png` · `-64.png` | web y documentos (128 para la barra superior @2x) |
| `asuskf-badge-32.png` | favicon |
| `assets/banner/asuskf-banner.png` (1584×396) | portada/cabecera ancha (estilo LinkedIn/YouTube); texto encima solo con el velo del §07 |

- **Bloqueo de marca:** insignia (42 px de alto en la barra) + "Asuskf Investing" en Playfair Display 700, 20 px, oro, tracking 1px.
  La palabra se compone en texto; la insignia es siempre la imagen.
- En la barra superior la insignia va recortada en círculo con **borde dorado de 1.5 px** (así está en el sitio).
- **Espacio libre:** al menos ¼ del diámetro de la insignia alrededor.
- **Fondos:** sobre bosque (`--ak-bg`, `--ak-surface`, `--ak-brand-green`) ✔ · sobre marfil/blanco ✔ (la insignia trae su propio
  disco verde) · sobre oro ✖ · sobre fotos complejas ✖.
- **No:** estirar, rotar, cambiar colores, quitar el borde del disco, poner sombra de color, recortar el texto "@ASUSKF" o eToro.

## 02 — Color

### Paleta

| Nombre | Token | Hex | Rol |
|---|---|---|---|
| Bosque 900 | `--ak-bg` | `#0A1714` | fondo de página (tema oscuro) |
| Bosque 950 | `--ak-bg-deep` | `#050D0A` | pie, modales, fondo de infografías |
| Bosque tarjeta | `--ak-surface` | `#111E1A` | tarjetas |
| Bosque elevado | `--ak-surface-2` | `#12211D` | tarjetas elevadas, filas alternas |
| **Verde insignia** | `--ak-brand-green` | `#123D28` | bloques de marca (banner, encabezado de Excel/PDF) |
| **Oro metálico** | `--ak-gold` | `#D4AF37` | acento: títulos, eyebrows, CTA, bordes activos |
| Oro claro | `--ak-gold-light` | `#E8CC6A` | hover |
| Oro profundo | `--ak-gold-deep` | `#B5952F` | pressed |
| Oro tinta (claro) | `--ak-gold-ink` | `#7A5F0E` | texto dorado sobre fondo claro |
| Texto | `--ak-text` | `#C8D4D0` | cuerpo en oscuro |
| Texto apagado | `--ak-text-muted` | `#7A9490` | secundario, etiquetas |
| Blanco | `--ak-text-strong` | `#FFFFFF` | hero, KPI |
| Ganancia | `--ak-gain` | `#4CAF70` (claro `#1F7A45`) | solo estado |
| Pérdida | `--ak-loss` | `#E57373` (claro `#B3403F`) | solo estado |
| Marfil | (claro) `--ak-bg` | `#F5F3EC` | fondo de documento |

### Proporción

**Bosque ≈ 85 %** (superficies) · **texto/grises ≈ 5-10 %** · **oro ≤ 10 %** (el acento: si todo es dorado, nada destaca) ·
verde/rojo de estado solo donde hay datos de rendimiento.

### Contrastes verificados (WCAG, 2026-10-08)

| Par | Ratio | | Par (claro) | Ratio |
|---|---|---|---|---|
| Oro sobre Bosque 900 | 8.7:1 ✔ | | Texto #1C2B27 sobre marfil | 13.3:1 ✔ |
| Texto sobre Bosque 900 | 12.0:1 ✔ | | Apagado #4D625D sobre marfil | 5.9:1 ✔ |
| Apagado sobre Bosque 900 | 5.6:1 ✔ | | **Oro tinta #7A5F0E sobre marfil** | 5.5:1 ✔ |
| Bosque sobre botón oro | 8.7:1 ✔ | | Oro de marca sobre marfil | **1.9:1 ✖ (prohibido como texto)** |
| Ganancia / pérdida sobre Bosque | 6.7 / 6.1 ✔ | | Ganancia / pérdida sobre blanco | 5.4 / 5.6 ✔ |
| Blanco sobre verde insignia | 12.2:1 ✔ | | Texto fuerte #0A1714 sobre marfil | 16.5:1 ✔ |
| Números en celdas del heatmap (8 combinaciones, ambos temas) | 5.5–8.6:1 ✔ | | | |

### Regla del oro como texto

Oro de marca como texto **solo sobre bosque**. Sobre marfil/blanco: `--ak-gold-ink`, o texto en tinta con un filete/acento dorado
cerca (borde inferior, barra lateral). Nunca texto blanco sobre oro: el botón dorado lleva texto bosque (`--ak-on-gold`).

## 03 — Tipografía

| Rol | Familia | Pesos / tratamiento |
|---|---|---|
| Títulos, nombre de marca, encabezados de fila en matrices | **Playfair Display** (serif) | 400/700; h1 de portada en MAYÚSCULAS, tracking 4 px, blanco |
| Texto, navegación, botones, etiquetas | **Roboto** | 300 (subtítulos), 400 (cuerpo, line-height 1.65), 500 (nav, eyebrow), 700 (botones) |
| **Cifras financieras** (KPI, tablas, fechas, %, precios) | **Roboto Mono** | 400/700, tabulares; KPI 700 con tracking −1px |

- **Eyebrow:** Roboto 500, 12 px, MAYÚSCULAS, tracking 3 px, oro (oro tinta en claro).
- **Etiqueta de tarjeta:** Roboto 11 px, MAYÚSCULAS, tracking 1.5 px, oro.
- **Navegación:** Roboto 500, 13 px, MAYÚSCULAS, tracking 1.2 px; hover en oro.
- **Avisos legales:** Roboto 10-11 px itálica, color apagado.
- Archivos: `assets/fonts/*.ttf` (variables; para PPTX/DOCX/matplotlib) y `*.woff2` (subconjunto latino; para HTML). Licencias
  OFL 1.1 en `assets/fonts/OFL-*.txt`, viajan con las fuentes.

## 04 — Imágenes

- Las piezas propias de la marca son ilustraciones **metálicas doradas sobre verde** (toro, oso, maletín, globo, flecha alcista):
  ese es el registro visual. No mezclar con fotos de stock a todo color.
- Miniaturas de video/infografías: dentro de tarjeta con radio 4-6 px, zoom suave al pasar (1.03-1.04), botón de reproducción oro.
- No generar ni redibujar ilustraciones "al estilo" de la insignia para que parezcan oficiales.

## 05 — Componentes (del sitio, normalizados a tokens)

- **Barra superior:** fija, `--ak-nav-bg` con blur 12 px, filete inferior `--ak-border`; logo a la izquierda, enlaces en MAYÚSCULAS,
  CTA dorado a la derecha.
- **Botón primario:** fondo oro, texto bosque, 700, MAYÚSCULAS, radio 6 px, alto ≥ 44 px; hover oro claro + sube 1 px + brillo dorado.
  Secundario: fantasma con borde dorado.
- **Hero:** banner con velo `linear-gradient(100deg, bosque 82 % → 30 % → transparente)`, eyebrow dorado, h1 Playfair blanco en
  MAYÚSCULAS, subtítulo Roboto 300 tracking 2 px, **filete dorado que se desvanece**, fila de 3 KPI separados por filetes verticales.
- **Tarjeta:** `--ak-surface`, borde dorado 20 %, radio 6 px, sombra; hover borde 50 %.
- **KPI:** Roboto Mono 700 grande; positivo en verde, negativo en rojo, con su signo; subtítulo apagado 12 px.
- **Badge de estado:** fondo del color de estado al 10 %, texto del color de estado, radio 3 px.
- **Matriz de rendimientos (heatmap):** primera columna en Playfair, celdas en Roboto Mono con el número visible, escala
  roja-neutra-verde de 5 pasos (`--ak-heat-*`), columna "Total" en negrita.
- **Gauge:** semicírculo, pista oscura, aguja; valor en Roboto Mono 700. Relleno oro por defecto; **en el sitio público el gauge de
  precisión conserva su degradado rojo → oro → verde** (#9A3B3B → oro → #388E3C), excepción a la regla 7 decidida por el usuario (2026-10-08).
- **Lista de operaciones:** fecha en mono apagado; "COMPRA" verde / "VENTA" roja en 11 px 700 (texto + color).
- **Pie:** `--ak-bg-deep`, redes como botones fantasma con icono dorado, aviso legal en itálica.

## 06 — Movimiento

- Aparición `reveal`: opacidad 0→1 y `translateY(24px→0)` en 0.65 s, con retrasos escalonados de 0.08/0.18/0.28 s.
- Hover: 0.2-0.25 s ease; elevación de 1 px como máximo.
- **`prefers-reduced-motion`:** las duraciones caen a 0 (ya está en los tokens). Sin parpadeos ni rotaciones.

## 07 — Layout

- Contenedor máximo **1300 px**, gutter 24 px. Grid de **6 columnas** para tableros (tarjetas de 2, 3 o 6 columnas, como el sitio).
- Secciones con 80 px arriba / 60 px abajo; encabezado de sección centrado: eyebrow + h2 + párrafo apagado (máx. 560 px).
- Radio 6 px en tarjetas/botones, 3 px en badges, 4 px en contenedores de medios.
- Únicos degradados permitidos: el **velo del hero** y el **filete dorado que se desvanece**. Superficies planas en todo lo demás.

## 08 — Principios

1. **Banca privada sobria:** verde bosque profundo + oro metálico + serif clásica → confianza y largo plazo.
2. **Datos primero:** cifras grandes en mono, tablas legibles, el color sirve a los datos.
3. **Oro con mesura:** ≤ 10 % de la superficie; si compite, se quita.
4. **Honestidad:** cada cifra trazable, avisos legales visibles, nunca promesas de rendimiento.
5. **Accesible por diseño:** contraste verificado, color nunca como única señal, movimiento reducido respetado (lente Apple HIG).
6. **Tokens siempre:** nada de valores sueltos.

## 09 — Aplicación por formato

| Produciendo… | Leer |
|---|---|
| HTML / sitio / dashboard (p. ej. `outputs/sitio/` de FinTKG) | `references/web-html.md` + `references/charts.md` |
| Gráficas (SVG propio, matplotlib) | `references/charts.md` |
| Excel (`src/hoja.py`), notebooks, PDF | `references/excel-y-notebooks.md` |
| Revisión de usabilidad / accesibilidad de cualquier pantalla | `references/apple-hig.md` → skill `apple-design` |

**Presentaciones:** no hay plantilla oficial de Asuskf. Si se pide un deck, proponer: portada con el banner y el velo del hero, títulos
en Playfair blanco/oro sobre bosque, contenido en tema claro (marfil) con oro tinta, KPI en Roboto Mono, aviso legal en el pie; y
**confirmar con el usuario antes** de fijarlo como estándar.

**Aplicación al sitio FinTKG (hecha el 2026-10-08):** `src/sitio.py` copia `colors_and_type.css` + `@font-face` locales a
`outputs/sitio/assets/marca.css` y los `.woff2` a `assets/fonts/`; `src/web/fintkg.css` usa solo `var(--ak-…)` (los nombres que usa
el JS de gráficas, `--s1..s3`, `--band`, `--grid`, `--ref`, son alias de los tokens). Tema oscuro por defecto, botón claro/oscuro
recordado en `localStorage`. Encabezado con el nombre "Asuskf Investing" en Playfair (sin insignia, por la regla 6 de eToro). Niveles de
año: excelente/buena = heat-gain, rentable con fallas = oro, débil = heat-loss. Cifras con signo menos real (JS `menos()` y
`sintesis.menos()`). Si cambian los tokens, basta con volver a correr el notebook 05.

### Portabilidad (para compartir la skill)

- Todo lo de la marca viaja en la carpeta: tokens, fuentes (OFL), logo, banner, referencias, scripts y la hoja de referencia rápida.
- Las menciones a FinTKG (`src/sitio.py`, `outputs/sitio`) son **ejemplos de aplicación**: en otro proyecto se ignoran.
- La lente Apple HIG depende de la skill **`apple-design`**, que **no se incluye** (su repositorio no trae licencia y el texto es de
  Apple). Quien la quiera: `npx skills add dickwu/apple-design-skill` o
  `git clone https://github.com/dickwu/apple-design-skill.git ~/.claude/skills/apple-design`.
- `scripts/exportar_tokens.py` y `build_cheatsheet.py` solo usan la biblioteca estándar de Python (las rutas son relativas a la skill).

---

## Referencia rápida

**Nombre:** Asuskf Investing · **Sitio:** asuskf.github.io/asuskf-invest.github.io · **eToro:** @asuskf (marca de tercero en la insignia)
**Paleta:** Bosque `#0A1714` · Tarjeta `#111E1A` · Verde insignia `#123D28` · **Oro `#D4AF37`** · Oro claro `#E8CC6A` · Texto `#C8D4D0` ·
Apagado `#7A9490` · Ganancia `#4CAF70` · Pérdida `#E57373` · (claro: marfil `#F5F3EC`, oro tinta `#7A5F0E`)
**Gráficas:** oro `#A8862A` → azul `#3D8BD4` → terracota `#C96B45` → violeta `#A77FD6` (dispersión: máx. 2)
**Fuentes:** Playfair Display (títulos) · Roboto (texto) · Roboto Mono (cifras) — locales
**Forma:** radio 6 px · contenedor 1300 px · grid 6 columnas · objetivos ≥ 44 px
**Siempre:** aviso de "no es recomendación de inversión" · cifras trazables · color + signo en ganancia/pérdida
