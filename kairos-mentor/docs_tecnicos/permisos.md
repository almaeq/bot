Permisos de salud de Android: orientación y preguntas frecuentes

En esta página, se proporciona orientación detallada y se responden preguntas frecuentes sobre el uso de permisos de Android que acceden a datos sensibles de salud y fitness. Entre estos permisos se incluyen, sin limitaciones, los siguientes:

A. Permisos de Health Connect: Health Connect proporciona una forma centralizada y estandarizada para que las apps almacenen y compartan datos de salud y fitness, a la vez que mantienen la privacidad y seguridad de los usuarios. Permite que las apps soliciten acceso a tipos de datos específicos en lugar de permisos amplios, lo que brinda más transparencia y control. Estos son algunos ejemplos de permisos de Health Connect:

    android.permission.health.READ_HEART_RATE

    android.permission.health.READ_BLOOD_PRESSURE

Puedes encontrar más información sobre Health Connect, incluido cómo comenzar a usar esta plataforma, en nuestra página para desarrolladores de Health Connect. Para obtener detalles sobre los permisos de salud, consulta la página sobre permisos de salud de Android.

B. Sensores corporales: Android también proporciona permisos para acceder a los datos directamente desde sensores corporales incorporados, como monitores de frecuencia cardíaca, pulsioxímetros y sensores de temperatura cutánea. (Con android.permission.BODY_SENSORS o, a partir de Android 16, permisos más detallados de android.permission.health.*, como android.permission.health.READ_HEART_RATE).

Para obtener más información sobre la transición, consulta el artículo sobre cambios en el comportamiento: apps que tienen como objetivo Android 16 o versiones posteriores.

C. Entre otros permisos pertinentes, se incluyen los siguientes:

    Permisos específicos relacionados con la salud, como READ_HEALTH_DATA_IN_BACKGROUND y READ_HEALTH_DATA_HISTORY

    Los permisos estándar de Android (por ejemplo, Ubicación, Cámara, Micrófono, Bluetooth, Ejecución en segundo plano) que se usan en una app de salud para recopilar o inferir información de salud sensible también están sujetos a los principios básicos que se describen aquí (consentimiento del usuario, minimización de datos, limitación de propósito y seguridad) y a la política de Datos del Usuario

Acceso y uso de datos: requisitos y orientación

El acceso y el uso de los permisos de salud están sujetos a los siguientes principios clave. Se aplican independientemente de si los datos provienen de Health Connect, de sensores corporales o de otros permisos pertinentes de salud, bienestar y fitness, y complementan los requisitos completos de las políticas de Datos del Usuario y Apps de salud.

    El acceso de tu app a los datos de salud y fitness obtenidos a través de los permisos de Android debe estar directamente relacionado con la prestación de un beneficio claro para el usuario dentro del alcance de los casos de uso aprobados que se detallan en esta guía.

    Debes cumplir con todos los requisitos detallados de consentimiento, solicitudes de permisos de tiempo de ejecución y divulgación destacada que se describen en la política de Datos del Usuario de Google Play.

    Únicamente solicita permisos y accede a tipos de datos que admitan las funciones de salud específicas que ofreces para el usuario. No solicites un acceso más amplio de lo necesario.

    Mantén una política de privacidad completa y precisa a la que se pueda acceder fácilmente desde la app y la ficha de Play Store. La política debe explicar claramente lo siguiente:

    Qué datos de salud y fitness recopila tu app y a cuáles accede

    Cómo se usan, almacenan y, posiblemente, divulgan los datos (incluido con cualquier tercero)

    Tus políticas de retención y eliminación de datos

    Tus prácticas de seguridad

La funcionalidad de tu app, la ficha de Play Store y cualquier divulgación en la app relacionada con el acceso a datos de salud deben representar con precisión tus prácticas de datos y el uso previsto.

    Debes implementar medidas de seguridad técnicas, administrativas y físicas sólidas para proteger los datos de salud sensibles de pérdidas y del acceso, uso, divulgación, modificación o destrucción no autorizados. Esto incluye, como mínimo, la encriptación de datos en reposo y en tránsito, controles de acceso sólidos en tus sistemas, prácticas de desarrollo seguras y administración de vulnerabilidades.

    Eres la única parte responsable de identificar y satisfacer todas las leyes, reglamentaciones y estándares de la industria aplicables que se relacionen con los datos de salud en cada región donde se distribuya tu app. Esto incluye, entre otros, requisitos como los siguientes:

    HIPAA en Estados Unidos para la Información de salud protegida (PHI)

    RGPD en Europa en relación con el tratamiento de datos personales y, en particular, el tratamiento de categorías especiales de datos

    Reglamentaciones sobre Software como Dispositivo Médico (SaMD) si tu app cumple con los criterios correspondientes

    Leyes locales de privacidad de los datos y de información de salud

Para obtener una lista completa de los usos prohibidos de los datos de salud y fitness de Android, consulta la sección "Usos prohibidos de los datos de salud y fitness de Android" más abajo.
Casos de uso aprobados para los permisos de salud de Android

El acceso a datos sensibles de salud y fitness a través de permisos de Android se limita estrictamente a las apps que proporcionan un beneficio claro para el usuario en casos de uso específicos y aprobados. Los casos de uso declarados en Play Console deben reflejar con precisión la funcionalidad de tu app que requiere datos de salud y fitness.

En esta sección, se proporcionan descripciones y ejemplos detallados de los casos de uso principales aprobados. Ten en cuenta que la idoneidad de los datos de Health Connect o de los sensores corporales puede variar según la función específica.

Fitness, bienestar y entrenamiento

Recompensas

Bienestar corporativo

Atención médica

Investigación con seres humanos

Juegos integrados sobre salud
Usos prohibidos de los datos de salud y fitness de Android

Debido a la naturaleza sensible de los datos de salud, actividad física y bienestar, ciertos usos están estrictamente prohibidos para proteger la privacidad y la seguridad de los usuarios. Está prohibido usar los datos a los que se accede a través de los permisos de salud de Android (incluidos los de Health Connect, los de sensores corporales y otros permisos pertinentes) para cualquiera de los siguientes fines:
Explotación comercial y publicidad

    Transferir o vender datos de salud o fitness de los usuarios a terceros, como plataformas publicitarias, agentes de datos o cualquier revendedor de información
    Transferir, vender o usar datos de salud y fitness de los usuarios para publicar anuncios, incluida la publicidad personalizada o basada en intereses
    Transferir, vender o usar datos de salud y fitness de los usuarios para determinar la solvencia crediticia o con fines de préstamos
    Divulgar datos de salud a terceros sin el consentimiento informado y explícito del usuario

Aplicaciones no autorizadas o no seguras

    Transferir, vender o usar datos de salud y fitness de los usuarios con cualquier producto o servicio que podría considerarse como un dispositivo médico, a menos que la app de dispositivo médico satisfaga todas las reglamentaciones aplicables, lo que incluye haber obtenido las aprobaciones o los permisos necesarios de los órganos reguladores pertinentes (por ejemplo, la FDA de EE.UU.) para el uso previsto de los datos de salud y fitness, y que el usuario haya otorgado su consentimiento explícito para tal uso
    Transferir, vender o usar datos de salud y fitness de los usuarios para cualquier fin o de cualquier manera que involucre información de salud sensible regida por reglamentaciones de privacidad específicas (por ejemplo, Información de salud protegida en virtud de la HIPAA), a menos que el usuario inicie tales acciones y estas satisfagan todas las leyes y reglamentaciones aplicables
    Usar datos de salud y fitness para desarrollar aplicaciones, entornos o actividades, o para incorporarlos en ellos, cuando se pueda esperar razonablemente que el uso o la falla de los datos de salud causen la muerte, lesiones personales, daños a las personas físicas, daños ambientales o daños a la propiedad
    Acceder a datos obtenidos a partir de permisos de salud de Android con apps sin interfaz gráfica; las apps deben mostrar un ícono claramente identificable en la bandeja de apps, en la configuración en el dispositivo, en íconos de notificaciones, etcétera
    Usar APIs de datos de salud y fitness con apps que sincronicen datos entre plataformas o dispositivos incompatibles
    Usar los permisos de salud de Android para conectarse a aplicaciones, servicios o funciones que estén dirigidos exclusivamente a niños

¿Cómo solicito acceso a los datos a través de los permisos de salud y fitness?

    Revisa las políticas correspondientes: Revisa y comprende los casos de uso y los requisitos aprobados para acceder a los datos de salud y fitness de los usuarios, compartirlos y protegerlos. Para obtener más información, lee la política de Permisos de Salud de Android y la guía que se menciona en esta página.
    Solicita permisos en Play Console: Cuando envíes tu app a Play Console, solicita los permisos específicos requeridos según los tipos de datos que tu app necesite para ofrecer sus funciones.

Cuando solicites permisos, ten en cuenta lo siguiente:

    Para cada permiso solicitado, proporciona una justificación clara y detallada en la que se explique cómo tu app usará los datos para beneficiar al usuario.
    No debes solicitar acceso a tipos de datos específicos si la app no lo requiere.
    Documenta el propósito de tus solicitudes de acceso con el mayor nivel de detalle posible.
    Solicita la mínima cantidad de tipos de datos necesaria y proporciona un caso de uso válido para cada solicitud.

Si quieres obtener una guía visual para administrar permisos de Salud y fitness, el siguiente video puede resultarte útil.

Ejemplos de una buena justificación:

    Permiso solicitado: Acceso a los datos de actividad física
    Justificación: "Nuestra app ofrece planes de entrenamiento personalizados. El acceso a los datos de actividad física nos permite adaptar las recomendaciones en función de los niveles de actividad actuales de los usuarios, lo que mejora su experiencia de entrenamiento".
    Permiso solicitado (sensores corporales): android.permission.health.READ_HEART_RATE
    Justificación: "Nuestra app ofrece un monitoreo de la frecuencia cardíaca en tiempo real durante los entrenamientos para proporcionar comentarios al usuario y permitirle ajustar la intensidad de su entrenamiento".

Ejemplo de una justificación incompleta:

    Permiso solicitado: Acceso a los datos de actividad física
    Justificación: "Se necesitan para el funcionamiento de la app" (es demasiado amplia y carece de justificación específica).

    Describe las prácticas de privacidad y seguridad: Proporciona una política de privacidad integral que cumpla con los siguientes requisitos:
    Proporciona una descripción general de las prácticas de recopilación, uso y divulgación de datos de tu app. Incluye información sobre qué datos se recopilan, cómo se usan y almacenan, y detalles sobre los controles de los usuarios y las prácticas de divulgación de datos.
    Describe las medidas de seguridad implementadas para proteger los datos del usuario, como encriptación, controles de acceso y evaluaciones de seguridad periódicas.

Todas las solicitudes de acceso a permisos de sensores corporales y salud y fitness estarán sujetas a revisión para garantizar que el uso de estos datos sensibles se ajuste a los casos de uso aprobados.


Si tu solicitud está incompleta o se rechaza, recibirás comentarios a través de Play Console. Estos son algunos de los motivos comunes por los que se rechazan las solicitudes:

    Falta una justificación clara para los permisos solicitados.
    Falta alineación con los casos de uso aprobados.
    No hay suficientes detalles sobre las prácticas de recopilación, uso y divulgación de datos.

Los desarrolladores pueden revisar y volver a enviar sus solicitudes con información adicional o aclaraciones.