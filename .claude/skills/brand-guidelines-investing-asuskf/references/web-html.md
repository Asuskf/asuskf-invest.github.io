# Web / HTML — implementación Asuskf Investing

Todo HTML de marca es **autocontenido**: fuentes en base64 (o rutas locales a `assets/fonts/`), logo como `<img>` desde archivo,
tokens copiados de `assets/tokens/colors_and_type.css`. **Nada de Google Fonts ni CDN** (el sitio público los usa; los entregables no).

## 1. Fuentes

```python
import base64, pathlib
F = pathlib.Path(".claude/skills/brand-guidelines-investing-asuskf/assets/fonts")
def face(familia, archivo, estilo="normal", pesos="100 900"):
    b64 = base64.b64encode((F / archivo).read_bytes()).decode()
    return (f"@font-face{{font-family:'{familia}';src:url(data:font/woff2;base64,{b64}) format('woff2');"
            f"font-weight:{pesos};font-style:{estilo};font-display:swap}}")
CSS_FUENTES = "\n".join([
    face("Playfair Display", "playfair-display.woff2", pesos="400 900"),
    face("Playfair Display", "playfair-display-italic.woff2", "italic", "400 900"),
    face("Roboto", "roboto.woff2"), face("Roboto", "roboto-italic.woff2", "italic"),
    face("Roboto Mono", "roboto-mono.woff2", pesos="100 700"),
])
```

En un sitio de varias páginas (como `outputs/sitio/`), copiar los `.woff2` a `assets/fonts/` del sitio y usar
`src:url(fonts/roboto.woff2)` en lugar de base64: el navegador los guarda en caché una vez.

## 2. Tokens y tema

Pegar el contenido de `colors_and_type.css` en el `<style>` (o enlazarlo). Tema por atributo:

```html
<html lang="es" data-theme="dark">   <!-- default: oscuro, como el sitio -->
<section data-theme="light">…</section>   <!-- documento/impresión -->
```

Para respetar la preferencia del sistema sin pisar la elección explícita del usuario:

```css
@media (prefers-color-scheme: light) { :root:not([data-theme]) { /* copiar el bloque [data-theme="light"] */ } }
```

## 3. Logo (desde archivo, nunca redibujado)

```python
logo = base64.b64encode(pathlib.Path(".../assets/logos/asuskf-badge-128.png").read_bytes()).decode()
html = f'<img class="ak-logo" src="data:image/png;base64,{logo}" alt="Asuskf Investing">'
```
```css
.ak-logo{height:42px;width:auto;border-radius:var(--ak-radius-pill);border:1.5px solid var(--ak-gold)}
.ak-wordmark{font-family:var(--ak-font-heading);font-weight:700;font-size:20px;color:var(--ak-gold-ink);letter-spacing:1px}
```

La palabra "Asuskf Investing" junto a la insignia es **texto en Playfair Display** (así está en el sitio): eso sí se escribe; la
insignia circular **no** se redibuja nunca. Favicon: `asuskf-badge-32.png` / `-64.png`.

## 4. Componentes base (equivalentes del sitio)

```css
body{background:var(--ak-bg);color:var(--ak-text);font:var(--ak-fs-body)/var(--ak-lh-body) var(--ak-font-body);-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:var(--ak-font-heading);color:var(--ak-gold-ink)}
.ak-nav{position:sticky;top:0;display:flex;justify-content:space-between;align-items:center;padding:var(--ak-space-3) var(--ak-space-7);
  background:var(--ak-nav-bg);backdrop-filter:blur(12px);border-bottom:1px solid var(--ak-border)}
.ak-nav a{color:var(--ak-text);font-size:var(--ak-fs-small);text-transform:uppercase;letter-spacing:var(--ak-track-nav);font-weight:500;text-decoration:none}
.ak-nav a:hover,.ak-nav a[aria-current=page]{color:var(--ak-gold-ink)}
.ak-eyebrow{font-size:var(--ak-fs-eyebrow);text-transform:uppercase;letter-spacing:var(--ak-track-eyebrow);color:var(--ak-gold-ink);font-weight:500}
.ak-btn{display:inline-flex;align-items:center;min-height:var(--ak-hit-min);padding:0 22px;border-radius:var(--ak-radius);background:var(--ak-gold);
  color:var(--ak-on-gold);font-weight:700;font-size:var(--ak-fs-small);text-transform:uppercase;letter-spacing:1px;text-decoration:none;border:0;
  transition:background-color var(--ak-dur) var(--ak-ease),transform var(--ak-dur-fast) var(--ak-ease),box-shadow var(--ak-dur) var(--ak-ease)}
.ak-btn:hover{background:var(--ak-gold-light);transform:translateY(-1px);box-shadow:var(--ak-glow-gold)}
.ak-btn:focus-visible{outline:2px solid var(--ak-gold-light);outline-offset:3px}
.ak-btn--ghost{background:transparent;color:var(--ak-gold-ink);border:1px solid var(--ak-border-hover)}
.ak-card{background:var(--ak-surface);border:1px solid var(--ak-border);border-radius:var(--ak-radius);padding:var(--ak-space-5);box-shadow:var(--ak-shadow);
  transition:border-color var(--ak-dur),box-shadow var(--ak-dur)}
.ak-card:hover{border-color:var(--ak-border-hover);box-shadow:var(--ak-shadow-hover)}
.ak-card h3{font-family:var(--ak-font-body);font-size:var(--ak-fs-label);text-transform:uppercase;letter-spacing:var(--ak-track-label);color:var(--ak-gold-ink)}
.ak-kpi{font-family:var(--ak-font-mono);font-size:var(--ak-fs-kpi);font-weight:700;letter-spacing:-1px;color:var(--ak-text-strong);font-variant-numeric:tabular-nums}
.ak-kpi--gain{color:var(--ak-gain)} .ak-kpi--loss{color:var(--ak-loss)}
.ak-badge{display:inline-block;padding:2px 8px;border-radius:var(--ak-radius-sm);font-size:var(--ak-fs-label);font-weight:700;letter-spacing:.5px}
.ak-badge--gain{background:var(--ak-gain-bg);color:var(--ak-gain)} .ak-badge--loss{background:var(--ak-loss-bg);color:var(--ak-loss)}
.ak-num{font-family:var(--ak-font-mono);font-variant-numeric:tabular-nums}
.ak-legal{font-size:var(--ak-fs-micro);color:var(--ak-text-muted);font-style:italic}
.ak-divider{height:1px;background:linear-gradient(90deg,var(--ak-gold),transparent);border:0}   /* único degradado permitido: filete */
.reveal{opacity:0;transform:translateY(24px);transition:opacity var(--ak-dur-reveal) var(--ak-ease),transform var(--ak-dur-reveal) var(--ak-ease)}
.reveal.active{opacity:1;transform:none}
```

## 5. Cifras financieras

- Siempre `.ak-num` (Roboto Mono, tabulares), alineadas a la derecha en tablas.
- Signo explícito: `+12.4 %` / `−3.1 %` (signo menos U+2212, no guion). Ganancia/pérdida lleva **color + signo** (o ▲/▼):
  nunca solo color.
- Porcentajes con espacio fino o normal antes de `%` de forma consistente en todo el entregable.

## 6. Heatmap de rendimientos (matriz mes × año, como el sitio)

```css
.ak-heat td{font-family:var(--ak-font-mono);font-size:12px;text-align:center;padding:6px}
.ak-heat td:first-child{font-family:var(--ak-font-heading);font-weight:700;color:var(--ak-text);text-align:left}
.ak-heat th{color:var(--ak-gold-ink);font-size:var(--ak-fs-label);text-transform:uppercase;letter-spacing:.5px}
.ak-heat .g2{background:var(--ak-heat-gain-strong);color:var(--ak-heat-gain-strong-ink)}
.ak-heat .g1{background:var(--ak-heat-gain);color:var(--ak-heat-gain-ink)}
.ak-heat .n {background:var(--ak-heat-neutral);color:var(--ak-text-muted)}
.ak-heat .l1{background:var(--ak-heat-loss);color:var(--ak-heat-loss-ink)}
.ak-heat .l2{background:var(--ak-heat-loss-strong);color:var(--ak-heat-loss-strong-ink)}
```
El valor numérico va **dentro de cada celda** (el rojo/verde no es legible para todos con daltonismo).

## 7. Aviso legal

Todo entregable con cifras de inversión lleva, en `.ak-legal`, que es análisis/información y **no recomendación de inversión**, y que
rendimientos pasados no garantizan resultados futuros. No inventar cifras: cada número sale de una fuente o cálculo trazable.
