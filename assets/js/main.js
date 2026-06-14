// =========================================
// DATOS CENTRALIZADOS
// =========================================
const matrixData = [
    ["2026", "1.84%", "0.46%", "-5.80%", "11.69%", "9.95%", "-2.96%", "", "", "", "", "", "", "14.85%"],
    ["2025", "1.96%", "-1.47%", "-6.58%", "0.79%", "5.60%", "6.49%", "1.81%", "1.05%", "4.55%", "3.23%", "-0.93%", "0.81%", "17.96%"],
    ["2024", "1.11%", "4.45%", "1.42%", "-5.78%", "7.31%", "6.28%", "-0.33%", "2.14%", "2.33%", "-1.34%", "2.58%", "-2.26%", "18.60%"],
    ["2023", "9.76%", "-1.07%", "6.28%", "-0.06%", "5.56%", "5.71%", "2.80%", "-2.33%", "-6.89%", "-2.02%", "12.75%", "5.77%", "40.59%"],
    ["2022", "-1.20%", "-3.79%", "2.90%", "-10.50%", "-1.13%", "-8.90%", "11.90%", "-5.71%", "-12.04%", "6.41%", "5.46%", "-7.19%", "-23.78%"]
];

// =========================================
// FUNCIONES GLOBALES
// =========================================
const calcularRetornoTotal = () => {
    const totales = matrixData.map(row => parseFloat(row[13].replace('%', '')));
    let retorno = 1;
    totales.forEach(t => { retorno *= (1 + t / 100); });
    return ((retorno - 1) * 100).toFixed(2) + '%';
};

const cargarMatrizLocal = () => {
    const tbody = document.querySelector('.matriz-table tbody');
    if (!tbody) return;
    tbody.innerHTML = '';

    matrixData.forEach(row => {
        const tr = document.createElement('tr');
        row.forEach((valorTexto, index) => {
            const td = document.createElement('td');
            td.textContent = valorTexto;

            if (index > 0) {
                if (valorTexto === '') {
                    td.classList.add('bg-neutral');
                } else {
                    const val = parseFloat(valorTexto.replace('%', ''));
                    if (val > 0) {
                        td.classList.add('bg-positive');
                        if (val > 7) td.classList.add('bg-positive-strong');
                    } else if (val < 0) {
                        td.classList.add('bg-negative');
                        if (val < -7) td.classList.add('bg-negative-strong');
                    } else {
                        td.classList.add('bg-neutral');
                    }
                    if (index === 13) td.classList.add('col-total');
                }
            }
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });
};

const inicializarGauge = () => {
    const gaugeFill = document.getElementById('gauge-fill');
    if (!gaugeFill) return;
    const totalLength = 126;
    gaugeFill.style.strokeDasharray = `0 ${totalLength}`;
    gaugeFill.style.strokeDashoffset = '0';
};

const animarTacometro = (porcentaje) => {
    const gaugeFill = document.getElementById('gauge-fill');
    const gaugeText = document.getElementById('win-rate-text');
    const needle = document.getElementById('gauge-needle');

    if (!gaugeFill || !gaugeText || !needle) return;

    const totalLength = 126;
    const value = (porcentaje / 100) * totalLength;
    gaugeFill.style.transition = 'stroke-dasharray 1.5s cubic-bezier(0.22, 1, 0.36, 1)';
    gaugeFill.style.strokeDasharray = `${value} ${totalLength}`;

    // Giro directo de 0 a 180 grados
    const rotation = (porcentaje / 100) * 180;
    
    // FORZAR EL EJE DE ROTACIÓN EXACTO DEL SVG
    needle.style.transformOrigin = '50px 52px';
    needle.style.transform = `rotate(${rotation}deg)`;

    let current = 0;
    const step = porcentaje / 60; 
    const timer = setInterval(() => {
        current = Math.min(current + step, porcentaje);
        gaugeText.textContent = current.toFixed(2) + '%';
        if (current >= porcentaje) clearInterval(timer);
    }, 25);
};
const inicializarModal = () => {
    const modal = document.getElementById("imageModal");
    const img = document.querySelector(".infographic-img.clickable");
    const modalImg = document.getElementById("imgModalOutput");
    const captionText = document.getElementById("caption");
    const spanCerrar = document.querySelector(".close-modal");

    if (!modal) return;

    if (img) {
        img.onclick = function () {
            modal.style.display = "block";
            modalImg.src = this.src;
            captionText.innerHTML = this.alt;
        };
    }

    if (spanCerrar) {
        spanCerrar.onclick = () => modal.style.display = "none";
    }

    window.addEventListener('click', (event) => {
        if (event.target === modal) modal.style.display = "none";
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
        }
    });
};

// =========================================
// INICIALIZACIÓN DOM
// =========================================
document.addEventListener('DOMContentLoaded', () => {
    cargarMatrizLocal();

    // KPI Dashboard
    const ytdRow = matrixData[0];
    const ytdValue = ytdRow[ytdRow.length - 1]; 
    const ytdDisplay = document.getElementById('ytd-display');
    if (ytdDisplay) {
        const ytdNum = parseFloat(ytdValue.replace('%', ''));
        ytdDisplay.textContent = (ytdNum > 0 ? '+' : '') + ytdValue;
        ytdDisplay.classList.add(ytdNum >= 0 ? 'positive' : 'negative');
    }

    // Retorno Hero
    const heroTotal = document.getElementById('hero-total-return');
    if (heroTotal) {
        const total = calcularRetornoTotal();
        const num = parseFloat(total);
        heroTotal.textContent = (num > 0 ? '+' : '') + total;
    }

    inicializarGauge();
    setTimeout(() => animarTacometro(97.96), 600);

    // Smooth Scroll
    document.querySelectorAll('nav ul li a[href^="#"]').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const offsetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - 70;
                window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
            }
        });
    });

    // Scroll Reveal
    const revealOptions = { threshold: 0.10, rootMargin: "0px 0px -30px 0px" };
    const revealOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);
    
    document.querySelectorAll('.reveal').forEach(el => revealOnScroll.observe(el));

    inicializarModal();
});