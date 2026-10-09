// =========================================
// FUENTE DE DATOS
// La tabla #matriz de index.html es la fuente única: de ella salen los colores del
// heatmap, el YTD, el retorno acumulado y la fecha "Datos hasta". Así los buscadores
// y asistentes de IA (que no ejecutan JS) leen las mismas cifras que los usuarios.
// =========================================
const MENOS = '−';   // signo menos real (regla de marca)
const MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
const ORGANIZACION = 'https://asuskf.github.io/asuskf-invest.github.io/#organization';
const reducirMovimiento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
document.documentElement.classList.add('js');

// "−2.26%", "-2.26%" o "-2.26" → -2.26 ; celda vacía → null
const leerPorcentaje = (texto) => {
    const limpio = texto.trim().replace(MENOS, '-').replace('%', '').replace(',', '.');
    return limpio === '' ? null : parseFloat(limpio);
};

const formatearPorcentaje = (valor, { signo = false, decimales = 2 } = {}) => {
    const absoluto = Math.abs(valor).toFixed(decimales) + '%';
    if (valor < 0) return MENOS + absoluto;
    return (signo && valor > 0 ? '+' : '') + absoluto;
};

const escribir = (selector, texto) => {
    document.querySelectorAll(selector).forEach(el => { el.textContent = texto; });
};

const leerMatriz = () => [...document.querySelectorAll('#matriz tbody tr')].map(tr => ({
    anio: tr.cells[0].textContent.trim(),
    meses: [...tr.cells].slice(1, 13),
    total: tr.cells[13]
}));

// =========================================
// MATRIZ (heatmap)
// Pasos por magnitud (tokens --ak-heat-*): weak |x| < 1 % · normal 1–7 % · strong > 7 %.
// =========================================
const pasoCalor = (valor) => {
    const magnitud = Math.abs(valor);
    return magnitud < 1 ? 'weak' : magnitud > 7 ? 'strong' : 'normal';
};

const pintarMatriz = (filas) => {
    filas.forEach(({ meses, total }) => {
        [...meses, total].forEach(td => {
            const valor = leerPorcentaje(td.textContent);
            if (td === total) td.classList.add('col-total');
            if (valor === null || valor === 0) {
                td.classList.add('heat-neutral');
                return;
            }
            td.textContent = formatearPorcentaje(valor, { signo: true });
            td.classList.add(`heat-${valor > 0 ? 'gain' : 'loss'}-${pasoCalor(valor)}`);
        });
    });
};

// =========================================
// KPIs (YTD, retorno acumulado, fecha de datos)
// =========================================
const actualizarKpis = (filas) => {
    if (!filas.length) return;
    const actual = filas[0];

    const ytd = leerPorcentaje(actual.total.textContent);
    if (ytd !== null) {
        escribir('[data-kpi="ytd-year"]', actual.anio);
        document.querySelectorAll('[data-kpi="ytd"]').forEach(el => {
            el.textContent = formatearPorcentaje(ytd, { signo: true });
            el.classList.toggle('positive', ytd >= 0);
            el.classList.toggle('negative', ytd < 0);
        });
    }

    const totales = filas.map(f => leerPorcentaje(f.total.textContent)).filter(v => v !== null);
    const acumulado = (totales.reduce((acc, t) => acc * (1 + t / 100), 1) - 1) * 100;
    escribir('[data-kpi="total"]', formatearPorcentaje(Math.trunc(acumulado), { signo: true, decimales: 0 }));
    escribir('[data-kpi="period"]', `${filas[filas.length - 1].anio}–${actual.anio}`);
    const mesesPublicados = filas.reduce((n, f) => n + f.meses.filter(td => leerPorcentaje(td.textContent) !== null).length, 0);
    escribir('[data-kpi="months"]', String(mesesPublicados));

    const ultimoMes = actual.meses.findLastIndex(td => leerPorcentaje(td.textContent) !== null);
    if (ultimoMes >= 0) {
        document.querySelectorAll('[data-kpi="updated"]').forEach(el => {
            el.textContent = `${MESES[ultimoMes]} de ${actual.anio}`;
            el.setAttribute('datetime', `${actual.anio}-${String(ultimoMes + 1).padStart(2, '0')}`);
        });
    }
};

// =========================================
// GAUGE (precisión de trading): anima al entrar en pantalla
// =========================================
const iniciarGauge = () => {
    const gauge = document.querySelector('[data-gauge]');
    if (!gauge) return;
    const porcentaje = parseFloat(gauge.dataset.gauge);
    const relleno = gauge.querySelector('.gauge-fill');
    const aguja = gauge.querySelector('.gauge-needle');
    const texto = gauge.querySelector('.gauge-value');
    const LARGO = 126;   // longitud del arco (π · 40)

    const pintar = (p) => {
        relleno.style.strokeDasharray = `${(p / 100) * LARGO} ${LARGO}`;
        aguja.style.transform = `rotate(${(p / 100) * 180}deg)`;
    };
    texto.textContent = formatearPorcentaje(porcentaje);
    if (reducirMovimiento || !('IntersectionObserver' in window)) return;   // el CSS ya lo muestra completo

    relleno.style.transition = aguja.style.transition = 'none';   // volver a 0 sin animar
    pintar(0);
    relleno.getBoundingClientRect();
    relleno.style.transition = aguja.style.transition = '';
    texto.textContent = formatearPorcentaje(0);
    const animar = () => {
        pintar(porcentaje);
        const inicio = performance.now();
        const DURACION = 1500;
        const paso = (ahora) => {
            const t = Math.min((ahora - inicio) / DURACION, 1);
            texto.textContent = formatearPorcentaje(porcentaje * (1 - Math.pow(1 - t, 3)));
            if (t < 1) requestAnimationFrame(paso);
        };
        requestAnimationFrame(paso);
    };
    new IntersectionObserver((entradas, observador) => {
        if (!entradas.some(e => e.isIntersecting)) return;
        observador.disconnect();
        setTimeout(animar, 300);
    }, { threshold: 0.5 }).observe(gauge);
};

// =========================================
// DATOS ESTRUCTURADOS DE VIDEO (desde las tarjetas [data-video-id])
// =========================================
const publicarVideos = () => {
    const videos = [...document.querySelectorAll('[data-video-id]')].map(card => {
        const id = card.dataset.videoId;
        const fecha = card.querySelector('.video-meta time[datetime]');
        return {
            '@type': 'VideoObject',
            name: card.querySelector('.video-title')?.textContent.trim(),
            description: card.querySelector('.sub-text')?.textContent.trim(),
            thumbnailUrl: [`https://i.ytimg.com/vi/${id}/maxresdefault.jpg`, `https://i.ytimg.com/vi/${id}/hqdefault.jpg`],
            uploadDate: fecha?.getAttribute('datetime'),
            duration: card.dataset.duration,
            url: card.querySelector('a[href]')?.href,
            embedUrl: `https://www.youtube.com/embed/${id}`,
            inLanguage: 'es',
            publisher: { '@id': ORGANIZACION, name: 'Asuskf Investing' }
        };
    }).filter(v => v.name && v.uploadDate);
    if (!videos.length) return;

    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.textContent = JSON.stringify({ '@context': 'https://schema.org', '@graph': videos });
    document.head.appendChild(script);
};

// =========================================
// MEDICIÓN DE CTAs (lista para GA4 o Google Tag Manager; no hace nada si no están instalados)
// =========================================
const medirCtas = () => {
    document.addEventListener('click', (evento) => {
        const cta = evento.target.closest('[data-cta]');
        if (!cta) return;
        const datos = { cta_id: cta.dataset.cta, link_url: cta.href };
        if (typeof window.gtag === 'function') window.gtag('event', 'cta_click', datos);
        else if (Array.isArray(window.dataLayer)) window.dataLayer.push({ event: 'cta_click', ...datos });
    });
};

// =========================================
// PREGUNTAS FRECUENTES: al abrir una, se cierran las demás.
// <details name="faq"> ya lo hace en navegadores actuales; esto cubre los anteriores.
// =========================================
const iniciarAcordeon = () => {
    if ('name' in HTMLDetailsElement.prototype) return;
    const items = document.querySelectorAll('.faq-item');
    items.forEach(item => item.addEventListener('toggle', () => {
        if (item.open) items.forEach(otro => { if (otro !== item) otro.open = false; });
    }));
};

// =========================================
// APARICIÓN AL HACER SCROLL
// Solo para lo que está bajo el pliegue al cargar: sin JS, o si algo falla, todo queda visible.
// =========================================
const iniciarReveal = () => {
    if (reducirMovimiento || !('IntersectionObserver' in window)) return;
    const pendientes = [...document.querySelectorAll('.reveal')]
        .filter(el => el.getBoundingClientRect().top > window.innerHeight);
    const observador = new IntersectionObserver((entradas) => {
        entradas.forEach(entrada => {
            if (!entrada.isIntersecting) return;
            entrada.target.classList.remove('reveal-pending');
            observador.unobserve(entrada.target);
        });
    }, { threshold: 0.10, rootMargin: '0px 0px -30px 0px' });
    pendientes.forEach(el => {
        el.classList.add('reveal-pending');
        observador.observe(el);
    });
};

// =========================================
// INICIALIZACIÓN
// =========================================
const filas = leerMatriz();
pintarMatriz(filas);
actualizarKpis(filas);
iniciarGauge();
publicarVideos();
medirCtas();
iniciarAcordeon();
iniciarReveal();
