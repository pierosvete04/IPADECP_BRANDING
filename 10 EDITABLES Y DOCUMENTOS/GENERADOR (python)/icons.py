"""Set de íconos IPADECP: retícula de 24, trazo de 2, puntas y uniones redondas."""

ICONS = {
    # curso: libro abierto
    "curso": '<path d="M12 6.5C10 5 7 4.5 3 4.5v13c4 0 7 .5 9 2 2-1.5 5-2 9-2v-13c-4 0-7 .5-9 2z"/><path d="M12 6.5v13"/>',
    # módulos: capas apiladas
    "modulos": '<path d="M12 3 2.5 8 12 13l9.5-5z"/><path d="m2.5 12 9.5 5 9.5-5"/><path d="m2.5 16 9.5 5 9.5-5"/>',
    # certificado: hoja con cinta
    "certificado": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M7 8h10M7 11.5h5"/><circle cx="16.5" cy="15.5" r="2.5"/><path d="m15 17.6-.8 3.9 2.3-1.3 2.3 1.3-.8-3.9"/>',
    # código QR
    "qr": '<rect x="3.5" y="3.5" width="6" height="6" rx="1"/><rect x="14.5" y="3.5" width="6" height="6" rx="1"/><rect x="3.5" y="14.5" width="6" height="6" rx="1"/><path d="M14.5 14.5h2.5v2.5M20.5 14.5v.01M14.5 20.5h.01M17.5 20.5h3v-3"/>',
    # verificar: escudo con check
    "verificar": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.3 7.5 9.5 4.3-1.2 7.5-4.9 7.5-9.5V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
    # celular
    "celular": '<rect x="6.5" y="2.5" width="11" height="19" rx="2"/><path d="M10.5 18.5h3"/>',
    # mensaje (WhatsApp sin logotipo de terceros)
    "mensaje": '<path d="M20.5 11.5a8.5 8.5 0 0 1-12.6 7.4L3.5 20.5l1.6-4.2A8.5 8.5 0 1 1 20.5 11.5z"/><path d="M8.5 10.5h7M8.5 13.5h4.5"/>',
    # envío por courier: camión
    "envio": '<path d="M2.5 6.5h11v10h-11z"/><path d="M13.5 9.5h4l3 3.5v3.5h-7"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    # sin horarios: reloj
    "a-tu-ritmo": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    # material editable: documento
    "documento": '<path d="M14 3H6.5A1.5 1.5 0 0 0 5 4.5v15A1.5 1.5 0 0 0 6.5 21h11a1.5 1.5 0 0 0 1.5-1.5V8z"/><path d="M14 3v5h5"/><path d="M8.5 12.5h7M8.5 16h5"/>',
    # presentación
    "presentacion": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v4M8.5 20.5h7"/><path d="m8 12.5 3-3 2.5 2 3-3.5"/>',
    # video de la clase
    "video": '<rect x="2.5" y="5.5" width="13" height="13" rx="2"/><path d="m15.5 10.5 6-3.5v10l-6-3.5"/>',
    # evaluación: lista con checks
    "evaluacion": '<rect x="4.5" y="3.5" width="15" height="18" rx="1.5"/><path d="M9 3.5V2.5h6v1"/><path d="m8 10 1.5 1.5L12 9M8 15.5l1.5 1.5L12 14.5M14.5 10.5h2M14.5 16h2"/>',
    # bibliografía: libros en estante
    "bibliografia": '<path d="M4.5 4v16M8.5 4v16"/><rect x="2.5" y="4" width="8" height="16" rx="1"/><path d="m13 5.5 3.9-1 4 15.5-3.9 1z"/><path d="M2.5 20.5h19"/>',
    # alumno
    "alumno": '<circle cx="12" cy="8" r="4"/><path d="M4 20.5c.8-3.6 4-6 8-6s7.2 2.4 8 6"/>',
    # todo el Perú: pin
    "ubicacion": '<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.5"/>',
    # pago
    "pago": '<rect x="2.5" y="5.5" width="19" height="13" rx="2"/><path d="M2.5 9.5h19M6.5 14.5h4"/>',
    # logro: estrella
    "logro": '<path d="m12 3 2.7 5.6 6.1.8-4.5 4.2 1.1 6.1L12 16.8l-5.4 2.9 1.1-6.1-4.5-4.2 6.1-.8z"/>',
    # descargar certificado
    "descargar": '<path d="M12 3.5v11M7.5 10l4.5 4.5 4.5-4.5"/><path d="M4 16.5v2.5A1.5 1.5 0 0 0 5.5 20.5h13a1.5 1.5 0 0 0 1.5-1.5v-2.5"/>',
    # birrete: graduación
    "birrete": '<path d="M12 4.5 1.5 9.5 12 14.5l10.5-5z"/><path d="M5.5 11.5v4.5c0 1.5 3 3 6.5 3s6.5-1.5 6.5-3v-4.5"/><path d="M22.5 9.5v5"/>',
}

NOMBRES = {
    "curso": "Curso", "modulos": "6 módulos", "certificado": "Certificado", "qr": "Código QR",
    "verificar": "Verificar", "celular": "Desde el celular", "mensaje": "WhatsApp", "envio": "Envío a todo el Perú",
    "a-tu-ritmo": "A tu ritmo", "documento": "Material editable", "presentacion": "Presentación",
    "video": "Video de clase", "evaluacion": "Evaluación", "bibliografia": "Bibliografía", "alumno": "Alumno",
    "ubicacion": "Provincia", "pago": "Pago", "logro": "Logro", "descargar": "Descargar", "birrete": "Graduación",
}

ICONS.update({
    "estetoscopio": '<path d="M5.5 3.5v5a4.5 4.5 0 0 0 9 0v-5"/><path d="M4 3.5h3M13 3.5h3"/><path d="M10 13v2.5a4.5 4.5 0 0 0 9 0V13"/><circle cx="19" cy="11" r="2"/>',
    "jeringa": '<path d="m18 2.5 3.5 3.5M19.75 4.25 16 8"/><path d="m14 4 6 6"/><path d="m17 7-9.5 9.5H4.5v-3L14 4"/><path d="m4.5 19.5-2 2M9 9l2 2M6.5 11.5l2 2"/>',
    "pulso": '<path d="M2.5 12h4l2-5 4 10 2.5-5h6.5"/>',
    "cruz-medica": '<path d="M9 3.5h6v5.5h5.5v6H15v5.5H9V15H3.5V9H9z"/>',
    "pastilla": '<rect x="3" y="8" width="18" height="8" rx="4" transform="rotate(-45 12 12)"/><path d="m9.2 9.2 5.6 5.6"/>',
    "laboratorio": '<path d="M9 3.5h6M10 3.5v6L4.8 18.6A1.5 1.5 0 0 0 6.1 21h11.8a1.5 1.5 0 0 0 1.3-2.4L14 9.5v-6"/><path d="M7 15h10"/>',
    "ambulancia": '<path d="M2.5 7.5h11v9h-11z"/><path d="M13.5 10.5h4l3 3v3h-7"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/><path d="M8 9.5v4M6 11.5h4"/>',
    "hospital": '<path d="M4 21V5.5A1.5 1.5 0 0 1 5.5 4h13A1.5 1.5 0 0 1 20 5.5V21"/><path d="M2.5 21h19"/><path d="M12 7.5v5M9.5 10h5"/><path d="M10 21v-4h4v4"/>',
    "calendario": '<rect x="3.5" y="5" width="17" height="15.5" rx="1.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="M8 14h2M14 14h2M8 17h2"/>',
    "correo": '<rect x="2.5" y="5" width="19" height="14" rx="1.5"/><path d="m3 6 9 7 9-7"/>',
    "candado": '<rect x="4.5" y="10.5" width="15" height="10.5" rx="1.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/><path d="M12 14.5v2.5"/>',
    "buscar": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5.5 5.5"/>',
    "clase-en-vivo": '<circle cx="12" cy="12" r="8.5"/><path d="m10 8.5 5.5 3.5-5.5 3.5z"/>',
    "billetera": '<path d="M19 7.5V5.5A1.5 1.5 0 0 0 17.5 4h-12A2.5 2.5 0 0 0 3 6.5v11A2.5 2.5 0 0 0 5.5 20h13a1.5 1.5 0 0 0 1.5-1.5v-11h-14.5"/><path d="M16 13.5h.01"/><path d="M14 11h7v5h-7a2.5 2.5 0 0 1 0-5z"/>',
    "aprobado": '<circle cx="12" cy="12" r="8.5"/><path d="m8 12.5 2.8 2.8L16.5 9.5"/>',
    "telefono": '<path d="M5 3.5h3.5l1.5 4.5-2 1.5a11 11 0 0 0 6.5 6.5l1.5-2 4.5 1.5V19a1.5 1.5 0 0 1-1.5 1.5A16.5 16.5 0 0 1 3.5 5 1.5 1.5 0 0 1 5 3.5z"/>',
    "medalla": '<circle cx="12" cy="14.5" r="5.5"/><path d="m8.5 10.3-3-6.8h4l2.5 5M15.5 10.3l3-6.8h-4l-1.3 2.6"/><path d="m12 12 .9 1.8 2 .3-1.4 1.4.3 2-1.8-1-1.8 1 .3-2-1.4-1.4 2-.3z"/>',
    "mundo": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17"/><path d="M12 3.5c2.3 2.4 3.5 5.2 3.5 8.5s-1.2 6.1-3.5 8.5c-2.3-2.4-3.5-5.2-3.5-8.5s1.2-6.1 3.5-8.5z"/>',
    "personal-de-salud": '<circle cx="12" cy="7" r="3.5"/><path d="M4.5 21c.6-4.4 3.6-7 7.5-7s6.9 2.6 7.5 7"/><path d="M12 15.5v4M10 17.5h4"/>',
    "dni": '<rect x="2.5" y="5" width="19" height="14" rx="1.5"/><circle cx="8.5" cy="11" r="2.2"/><path d="M5 16.5c.5-1.6 1.9-2.5 3.5-2.5s3 .9 3.5 2.5"/><path d="M14.5 10h4M14.5 13.5h3"/>',
})
NOMBRES.update({"estetoscopio": "Estetoscopio", "jeringa": "Jeringa", "pulso": "Pulso", "cruz-medica": "Cruz médica",
    "pastilla": "Farmacia", "laboratorio": "Laboratorio", "ambulancia": "Paramédico", "hospital": "Hospital",
    "calendario": "Calendario", "correo": "Correo", "candado": "Acceso seguro", "buscar": "Buscar",
    "clase-en-vivo": "Reproducir clase", "billetera": "Billetera", "aprobado": "Aprobado", "telefono": "Teléfono",
    "medalla": "Medalla", "mundo": "100 % virtual", "personal-de-salud": "Personal de salud", "dni": "DNI"})


def icon_g(name, color, sw=2.0):
    return (f'<g fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round">{ICONS[name]}</g>')
