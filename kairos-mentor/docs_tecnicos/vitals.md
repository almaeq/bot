 Desarrolla experiencias de signos vitales con Health Connect

Nota: Esta guía es compatible con la versión 1.1.0 de Health Connect.

Si quieres crear una app que administre los signos vitales del usuario, puedes usar Health Connect para realizar las siguientes acciones:

    Leer datos vitales, como la presión arterial, la frecuencia cardíaca y la temperatura corporal, de otras apps
    Escribe los datos de signos vitales que registran tu app o los dispositivos conectados
    Supervisar tendencias y proporcionar estadísticas de salud basadas en datos de signos vitales

En esta guía, se describe cómo trabajar con los tipos de datos de signos vitales, incluidos los permisos, los flujos de trabajo de lectura y escritura, y las prácticas recomendadas.
Descripción general: Cómo crear un monitor de signos vitales integral

Para crear una experiencia integral de seguimiento de signos vitales con Health Connect, sigue estos pasos principales:

    Solicitar los permisos adecuados para los tipos de datos de signos vitales
    Escribir datos vitales con registros como BloodPressureRecord, HeartRateRecord y otros registros vitales
    Lectura de datos vitales para mostrarlos, analizarlos o sincronizarlos
    Usa el procesamiento por lotes para leer y escribir datos de manera eficiente.

Este flujo de trabajo permite la interoperabilidad con otras apps de Health Connect y verifica el acceso a los datos controlado por el usuario.
Antes de comenzar

Antes de implementar las funciones de métricas vitales, haz lo siguiente:

    Integra Health Connect con la dependencia adecuada.
    Crea una instancia de HealthConnectClient.
    Verifica que tu app implemente flujos de permisos en tiempo de ejecución basados en los Permisos de Salud.

Conceptos clave

Los datos de signos vitales en Health Connect se representan con varios tipos de registros, cada uno correspondiente a una medición fisiológica específica. A diferencia de las sesiones de entrenamiento, los signos vitales suelen registrarse como datos puntuales o basados en intervalos.
Tipos de datos de signos vitales

Los datos de signos vitales se representan con tipos de registros individuales. Entre los tipos más comunes, se incluyen los siguientes:

    BloodPressureRecord: Representa una sola lectura de presión arterial, incluida la presión sistólica y diastólica, y la posición del cuerpo.
    HeartRateRecord: Representa una serie de mediciones de la frecuencia cardíaca.
    RestingHeartRateRecord: Representa una sola medición de la frecuencia cardíaca en reposo.
    BodyTemperatureRecord: Representa una sola lectura de temperatura corporal, incluida la ubicación de la medición.
    BloodGlucoseRecord: Representa una sola medición de glucemia, incluida la relación con la comida y la fuente de la muestra.
    OxygenSaturationRecord: Representa una sola lectura de saturación de oxígeno en sangre.
    RespiratoryRateRecord: Representa una sola medición de la frecuencia respiratoria.

Para obtener una lista completa de los tipos de datos, consulta Tipos de datos de Health Connect.
Consideraciones de desarrollo

Los datos de signos vitales pueden ser sensibles, y es posible que las apps deban escribir datos en respuesta a las mediciones de los sensores o a la entrada del usuario, o bien sincronizar datos desde un backend. Los permisos son fundamentales para controlar los datos de signos vitales.
Permisos

Tu app debe solicitar los permisos pertinentes de Health Connect antes de leer o escribir datos de signos vitales. Los permisos comunes para los signos vitales incluyen la presión arterial, la frecuencia cardíaca, la temperatura corporal, la glucemia, la saturación de oxígeno y la frecuencia respiratoria. Se incluye lo siguiente:

    Presión arterial: Permisos de lectura y escritura para BloodPressureRecord.
    Ritmo cardíaco: Permisos de lectura y escritura para HeartRateRecord.
    Frecuencia cardíaca en reposo: Permisos de lectura y escritura para RestingHeartRateRecord.
    Temperatura corporal: Permisos de lectura y escritura para BodyTemperatureRecord.
    Glucemia: Permisos de lectura y escritura para BloodGlucoseRecord.
    Saturación de oxígeno: Permisos de lectura y escritura para OxygenSaturationRecord.
    Frecuencia respiratoria: Permisos de lectura y escritura para RespiratoryRateRecord.

A continuación, se muestra un ejemplo de cómo solicitar permisos para la presión arterial, la frecuencia cardíaca y la temperatura corporal:

Después de crear una instancia de cliente, tu app debe solicitarle permisos al usuario. Los usuarios deben poder otorgar o rechazar permisos en cualquier momento.

Para hacerlo, crea un conjunto de permisos para los tipos de datos necesarios. Primero, asegúrate de que los permisos del conjunto se declaren en tu manifiesto de Android.

```bash
// Create a set of permissions for required data types
val PERMISSIONS =
    setOf(
  HealthPermission.getReadPermission(BloodPressureRecord::class),
  HealthPermission.getWritePermission(BloodPressureRecord::class),
  HealthPermission.getReadPermission(HeartRateRecord::class),
  HealthPermission.getWritePermission(HeartRateRecord::class),
  HealthPermission.getReadPermission(BodyTemperatureRecord::class),
  HealthPermission.getWritePermission(BodyTemperatureRecord::class)
)
```

Usa getGrantedPermissions para ver si tu app ya tiene otorgados los permisos necesarios. De lo contrario, usa createRequestPermissionResultContract para solicitarlos. Se mostrará la pantalla de permisos de Health Connect.

```bash
// Create the permissions launcher
val requestPermissionActivityContract = PermissionController.createRequestPermissionResultContract()

val requestPermissions = registerForActivityResult(requestPermissionActivityContract) { granted ->
  if (granted.containsAll(PERMISSIONS)) {
    // Permissions successfully granted
  } else {
    // Lack of required permissions
  }
}

suspend fun checkPermissionsAndRun(healthConnectClient: HealthConnectClient) {
  val granted = healthConnectClient.permissionController.getGrantedPermissions()
  if (granted.containsAll(PERMISSIONS)) {
    // Permissions already granted; proceed with inserting or reading data
  } else {
    requestPermissions.launch(PERMISSIONS)
  }
}
```

Dado que los usuarios pueden otorgar o revocar permisos en cualquier momento, tu app debe verificar los permisos cada vez antes de usarlos y controlar las situaciones en las que se pierden los permisos.

Para solicitar permisos, llama a la función checkPermissionsAndRun:

if (!granted.containsAll(PERMISSIONS)) {
    requestPermissions.launch(PERMISSIONS)
    // Check if required permissions are not granted, and return
  }
// Permissions already granted; proceed with inserting or reading data

Si solo necesitas solicitar permisos para un solo tipo de datos, como la presión arterial, incluye solo ese tipo de datos en tu conjunto de permisos:

El acceso a la presión arterial está protegido por los siguientes permisos:

    android.permission.health.READ_BLOOD_PRESSURE
    android.permission.health.WRITE_BLOOD_PRESSURE

Para agregar la función de presión arterial a tu app, comienza por solicitar permisos para el tipo de datos BloodPressureRecord.

Este es el permiso que debes declarar para poder escribir la presión arterial:

<application>
  <uses-permission
android:name="android.permission.health.WRITE_BLOOD_PRESSURE" />
...
</application>

Para leer la presión arterial, debes solicitar los siguientes permisos:

<application>
  <uses-permission
android:name="android.permission.health.READ_BLOOD_PRESSURE" />
...
</application>

Escribe datos vitales

En esta sección, se describe cómo escribir datos de signos vitales en Health Connect. Por lo general, los datos de signos vitales se escriben como registros individuales. Si escribes varios registros a la vez, como cuando sincronizas desde un sensor o un backend, usa el procesamiento por lotes.
Práctica recomendada: Usa IDs de cliente. Cuando crees registros, establece un metadata.clientRecordId. Esta es la forma más eficaz de evitar duplicados durante los reintentos de sincronización. Consulta las Prácticas recomendadas para ver un ejemplo de código.

Ejemplo de cómo escribir un BloodPressureRecord:

```bash
suspend fun writeBloodPressureRecord(healthConnectClient: HealthConnectClient) {
    val record = BloodPressureRecord(
        time = Instant.now(),
        zoneOffset = ZoneOffset.UTC,
        systolic = Pressure.millimetersOfMercury(120.0),
        diastolic = Pressure.millimetersOfMercury(80.0),
        bodyPosition = BloodPressureRecord.BODY_POSITION_SITTING_DOWN,
        measurementLocation = BloodPressureRecord.MEASUREMENT_LOCATION_LEFT_WRIST
    )
    healthConnectClient.insertRecords(listOf(record))
}
```

Escritura por lotes

Si tu app necesita escribir varios puntos de datos, como sincronizar datos de un dispositivo conectado o un servicio de backend, debes agrupar las escrituras en lotes para mejorar la eficiencia y reducir el consumo de batería. Health Connect puede controlar hasta 1,000 registros en una sola solicitud de escritura.

En el siguiente código, se muestra cómo escribir varios registros en lote a la vez:

```bash
suspend fun writeBatchRecords(healthConnectClient: HealthConnectClient) {
    val bloodPressureRecord = BloodPressureRecord(
        time = Instant.now(),
        zoneOffset = ZoneOffset.UTC,
        systolic = Pressure.millimetersOfMercury(120.0),
        diastolic = Pressure.millimetersOfMercury(80.0),
        bodyPosition = BloodPressureRecord.BODY_POSITION_SITTING_DOWN,
        measurementLocation = BloodPressureRecord.MEASUREMENT_LOCATION_LEFT_WRIST
    )
    val heartRateRecord = HeartRateRecord(
        startTime = Instant.now().minusSeconds(60),
        startZoneOffset = ZoneOffset.UTC,
        endTime = Instant.now(),
        endZoneOffset = ZoneOffset.UTC,
        samples = listOf(HeartRateRecord.Sample(time = Instant.now().minusSeconds(30), beatsPerMinute = 80))
    )
    healthConnectClient.insertRecords(listOf(bloodPressureRecord, heartRateRecord))
}
```

Lectura de datos vitales

Las apps pueden leer los datos vitales para mostrar mediciones, analizar tendencias o sincronizar datos con un servidor externo. Para leer los signos vitales, usa un objeto ReadRecordsRequest con el tipo de registro específico y filtra por un período.

Ejemplo de lectura de datos de BloodPressureRecord:

```bash
suspend fun readBloodPressureRecords(
    healthConnectClient: HealthConnectClient,
    startTime: Instant,
    endTime: Instant
) {
    val response = healthConnectClient.readRecords(
        ReadRecordsRequest(
            recordType = BloodPressureRecord::class,
            timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
        )
    )

    for (record in response.records) {
        // Process each blood pressure record
        val systolic = record.systolic
        val diastolic = record.diastolic
    }
}
```

Si necesitas sincronizar los datos de signos vitales con un servidor de backend o mantener actualizado el almacén de datos de tu app con Health Connect, usa ChangeLogs. Esto te permite recuperar una lista de registros insertados, actualizados o borrados desde un momento específico, lo que es más eficiente que hacer un seguimiento manual de los cambios o leer todos los datos de forma repetida. Para obtener más información, consulta Cómo sincronizar datos con Health Connect.
Prácticas recomendadas

Sigue estos lineamientos para mejorar la confiabilidad de los datos y la experiencia del usuario:

    Frecuencia de escritura y procesamiento por lotes: Para reducir la sobrecarga de entrada/salida y preservar la duración de la batería, agrupa los datos en una sola llamada a insertRecords con lotes de hasta 1,000 registros, en lugar de escribir cada punto de forma individual.
        Seguimiento en vivo: Para obtener actualizaciones frecuentes de los sensores (como los monitores continuos de glucosa o los monitores cardíacos), escribe los datos en lotes a intervalos de hasta 15 minutos para equilibrar las actualizaciones en tiempo real con la eficiencia de la batería.
        Sincronización en segundo plano: Usa WorkManager para escrituras diferidas, como la sincronización de datos desde un dispositivo complementario o un servicio de backend. Intenta establecer un intervalo de 15 minutos para las escrituras por lotes.

    Evita escribir datos duplicados: Usa IDs de cliente Cuando crees registros, establece un metadata.clientRecordId. Health Connect usa este campo para identificar registros únicos. Si intentas escribir un registro con un clientRecordId que ya existe, Health Connect ignorará el duplicado o actualizará el registro existente en lugar de crear uno nuevo. Establecer un metadata.clientRecordId es la forma más eficaz de evitar duplicados durante los reintentos de sincronización o las reinstalaciones de la app.

```bash
    val record = BloodPressureRecord(
        time = Instant.now(),
        zoneOffset = ZoneOffset.UTC,
        systolic = Pressure.millimetersOfMercury(120.0),
        diastolic = Pressure.millimetersOfMercury(80.0),
        bodyPosition = BloodPressureRecord.BODY_POSITION_SITTING_DOWN,
        measurementLocation = BloodPressureRecord.MEASUREMENT_LOCATION_LEFT_WRIST,
        metadata = Metadata(
            // Use a unique ID from your own database
            clientRecordId = "bp_20240101_user123"
        )
    )
```

    Verifica los datos existentes: Antes de sincronizar los datos, consulta Health Connect para ver si ya existen registros dentro del período de sincronización y evitar duplicados o sobrescribir datos más recientes.

    Proporciona explicaciones claras para los permisos: Usa el flujo de Permission.createIntent para explicar por qué tu app necesita acceder a los datos de salud, por ejemplo, "Para supervisar tus tendencias de presión arterial y proporcionar estadísticas".

    Alinea las marcas de tiempo con las mediciones: Verifica que las marcas de tiempo de los registros reflejen con precisión cuándo se tomaron las mediciones. En el caso de los datos de intervalo, como HeartRateRecord, verifica que startTime y endTime sean correctos.

Prueba

Para verificar la exactitud de los datos y garantizar una experiencia del usuario de alta calidad, sigue estas estrategias de prueba y consulta la documentación oficial sobre cómo probar los principales casos de uso.
Herramientas de verificación

    Health Connect Toolbox: Usa esta app complementaria para inspeccionar registros de forma manual, borrar datos de prueba y simular cambios en la base de datos. Es la mejor manera de verificar que tus registros se almacenen correctamente.
    Pruebas de unidades con FakeHealthConnectClient: Usa la biblioteca de pruebas para verificar cómo tu app controla los casos extremos, como la revocación de permisos o las excepciones de la API, sin necesidad de un dispositivo físico.

Lista de verificación de calidad
Confirma los registros en Health Connect: Abre la app de Health Connect y navega a Datos y acceso para verificar que los registros aparezcan con los valores esperados.
Leer datos de otras apps: Prueba la capacidad de tu app para leer los vitals escritos por otras apps y verificar la compatibilidad del ecosistema. Consulta Cómo leer los datos de Vitals.
Equilibra la frecuencia de escritura: Supervisa el uso de la batería si escribes con frecuencia. Las escrituras frecuentes proporcionan un alto nivel de detalle, pero pueden aumentar el consumo de batería.
Arquitectura típica

Por lo general, una implementación de métricas esenciales incluye lo siguiente:
Componente 	Administra
Controlador de signos vitales 	Lógica de procesamiento por lotes de lectura de sensores o entradas
Capa del repositorio (encapsula las operaciones de Health Connect): 	Insertar registros de signos vitales
Leer registros de signos vitales
Capa de la IU (pantallas): 	Lecturas en vivo
Datos históricos
Gráficos y tendencias
Solución de problemas
Síntoma 	Causa posible 	Resolución
Faltan tipos de datos (por ejemplo, presión arterial) 	Faltan permisos de escritura o los filtros de tiempo son incorrectos. 	Verifica que hayas solicitado y que el usuario haya otorgado el permiso de tipo de datos específico. Verifica que tu ReadRecordsRequest use un TimeRangeFilter que abarque el período de medición. Consulta Permisos.
No se pueden escribir los registros 	Unidades o valores incorrectos fuera del rango válido. 	Health Connect valida los valores de los registros. Por ejemplo, los valores de presión arterial deben estar dentro de un rango fisiológicamente plausible. Consulta la documentación del tipo de datos para conocer los rangos y las unidades válidos.
Aparecen registros duplicados 	Falta clientRecordId 	Asigna un clientRecordId único en el Metadata de cada registro. Esto permite que Health Connect realice la eliminación de duplicados si los mismos datos se escriben dos veces durante un reintento de sincronización. Consulta las prácticas recomendadas.
Pasos comunes de depuración

    Verifica el estado del permiso: Siempre llama a getPermissionStatus() antes de intentar una operación de lectura o escritura. Los usuarios pueden revocar los permisos en la configuración del sistema en cualquier momento.

