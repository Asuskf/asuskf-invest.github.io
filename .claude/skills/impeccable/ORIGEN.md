# Origen de esta skill

- Repositorio: https://github.com/pbakaus/impeccable · commit `18e751118ba64aeab59a2076c0efde12db73e08d` (2026-10-08) · skill v4.5.1, motor 0.1.12.
- Instalada el 2026-10-08 a pedido del usuario copiando `.claude/skills/impeccable/` y `.claude/agents/impeccable-*.md`
  (opción manual del README). Licencia Apache 2.0 (`LICENSE`).
- **No instalado:** los hooks de `.claude/settings.json` del repositorio (ejecutan el detector tras cada edición) y el binario del
  motor (`scripts/impeccable` lo descarga de GitHub Releases a `~/.impeccable/bin/` la primera vez que se usa, con verificación SHA-256).
  Sin el binario la skill usa su modo documentado "Launcher unavailable".
- Para la instalación completa (motor + hooks): `npx impeccable install --providers=claude --scope=project`.
