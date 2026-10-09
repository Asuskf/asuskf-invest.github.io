# Historial — brand-guidelines-investing-asuskf

## 1.2 · 2026-10-08
- Instalada en el repositorio del sitio público (`asuskf-invest.github.io/.claude/skills/`) junto con `apple-design`; descripción y
  alcance ampliados a ese repositorio.
- Aplicada al sitio: `assets/css/tokens.css` = copia de `colors_and_type.css`, `style.css` solo con `var(--ak-…)`, fuentes locales
  `.woff2` (sin Google Fonts), signo menos real, verde/rojo solo como estado (gauge en oro), aviso de "no es recomendación de inversión",
  objetivos táctiles de 44 px, foco visible y `prefers-reduced-motion` (lente Apple HIG).
- Excepción aprobada por el usuario: el gauge de precisión del sitio mantiene el degradado rojo → oro → verde original
  (variables `--gauge-*` en `style.css`). Preguntas frecuentes como acordeón exclusivo (`<details name="faq">`).

## 1.1 · 2026-10-08
- Aplicada al sitio FinTKG (`outputs/sitio`): tokens y fuentes locales copiados por `src/sitio.py`, `src/web/fintkg.css` reescrito solo
  con `var(--ak-…)`, tema claro/oscuro, hero de marca con cifras reales, signo menos real en cifras y textos; verificado en navegador.
- Sección de portabilidad y empaquetado `.skill` para compartir (sin `apple-design`, que se instala aparte).

## 1.0 · 2026-10-08
- Creación a pedido del usuario: marca de **Asuskf Investing** para el repositorio FinTKG, a partir del sitio público
  https://asuskf.github.io/asuskf-invest.github.io/ (copia en `assets/source/sitio/`), con la estructura de `brand-guidelines-kin`
  y la lente de usabilidad de la skill `apple-design` (https://github.com/dickwu/apple-design-skill, commit 904b0ee).
- Tokens (`colors_and_type.css`): tema oscuro = CSS del sitio; tema claro nuevo (marfil, oro tinta #7A5F0E por contraste);
  estados ganancia/pérdida y heatmap del sitio, con versión clara; escala tipográfica, espacio, radio y movimiento.
- Paleta de gráficas validada con `dataviz/validate_palette.js` (oscuro y claro): oro serie #A8862A, azul, terracota, violeta;
  dispersión limitada a 2 series.
- Fuentes locales (Playfair Display, Roboto, Roboto Mono; OFL 1.1) en TTF variable + woff2 subconjunto latino.
- Logo y banner originales; tamaños 256/128/64/32. Nota de marca de tercero (eToro).
- Generados: `tokens.json`, `asuskf-dark/light.mplstyle` (`scripts/exportar_tokens.py`) y `Asuskf_Brand_Cheatsheet.html`
  (`assets/quick-reference/build_cheatsheet.py`), verificado en navegador (claro/oscuro, escritorio y 375 px).
