# Procedencia de la marca (descargada el 2026-10-08)

| Origen | Archivo en la skill | Bytes | SHA-256 (16) |
|---|---|---|---|
| https://asuskf.github.io/asuskf-invest.github.io/ | `assets/source/sitio/index.html` | 15,600 | `a98125ead4b32362…` |
| https://asuskf.github.io/asuskf-invest.github.io/assets/css/style.css | `assets/source/sitio/style.css` | 24,428 | `f672f952cf4feb56…` |
| https://asuskf.github.io/asuskf-invest.github.io/assets/js/main.js | `assets/source/sitio/main.js` | 6,832 | `73061c4177f4e1cd…` |
| https://asuskf.github.io/asuskf-invest.github.io/assets/images/logo.png | `assets/logos/asuskf-badge.png` | 381,959 | `881c1d0d1749eb0e…` |
| https://asuskf.github.io/asuskf-invest.github.io/assets/images/banner.png | `assets/banner/asuskf-banner.png` | 175,723 | `6b4ef4c0da118cd7…` |
| https://github.com/google/fonts/raw/main/ofl/playfairdisplay/PlayfairDisplay[wght].ttf | `assets/fonts/playfair-display.ttf` | 300,724 | `c40f2293766a503b…` |
| https://github.com/google/fonts/raw/main/ofl/playfairdisplay/PlayfairDisplay-Italic[wght].ttf | `assets/fonts/playfair-display-italic.ttf` | 278,688 | `a5e26dc5e2e77fb2…` |
| https://github.com/google/fonts/raw/main/ofl/roboto/Roboto[wdth,wght].ttf | `assets/fonts/roboto.ttf` | 488,584 | `d7598e12c5dbef09…` |
| https://github.com/google/fonts/raw/main/ofl/roboto/Roboto-Italic[wdth,wght].ttf | `assets/fonts/roboto-italic.ttf` | 530,944 | `9725a847af6b460f…` |
| https://github.com/google/fonts/raw/main/ofl/robotomono/RobotoMono[wght].ttf | `assets/fonts/roboto-mono.ttf` | 183,700 | `66a80e79d17e4c7c…` |

- `sitio/` es una copia del sitio público (index.html, style.css, main.js) tal como estaba el 2026-10-08. Es la **referencia** de la que
  salen los tokens; no se edita. Si el sitio cambia, se vuelve a descargar y se actualizan los tokens (ver CHANGELOG.md).
- Fuentes: Google Fonts (github.com/google/fonts), licencia SIL OFL 1.1; los `OFL-*.txt` viajan con ellas. Los `.woff2` son subconjuntos
  latinos (+ ▲ ▼ ✔ ✖ Δ − €) generados con `pyftsubset` a partir de los `.ttf`.
- Logo y banner: archivos originales del sitio; los tamaños 256/128/64/32 son reducciones del original (sin redibujar).
  **Ambos contienen la marca de eToro (un tercero)**: se usan tal cual, sin recortar ni editar, y nunca para sugerir respaldo de eToro.
