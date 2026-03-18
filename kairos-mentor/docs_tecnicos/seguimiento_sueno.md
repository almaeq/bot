 Cómo hacer un seguimiento de las sesiones de sueño

    Esta guía es compatible con la versión 1.1.0-alpha11 de Health Connect.

Health Connect proporciona un tipo de datos de sesión de sueño para almacenar información sobre el sueño de un usuario, como una sesión nocturna o una siesta diurna. El tipo de datos SleepSessionRecord se usa para representar estas sesiones.

Las sesiones permiten que los usuarios midan el rendimiento basado en el tiempo durante un período, como la frecuencia cardíaca continua o los datos de ubicación.

Las sesiones SleepSessionRecord contienen datos que registran las etapas del sueño, como AWAKE, SLEEPING y DEEP.

Los datos de subtipo son aquellos que "pertenecen" a una sesión y solo son significativos cuando se leen con una sesión principal. Por ejemplo, la fase del sueño.

Por otro lado, los datos asociados hacen referencia a los datos que se registran de forma independiente, pero que se encuentran dentro del período de una sesión. Por ejemplo, si un usuario registra su frecuencia cardíaca durante su sesión de sueño, los datos de frecuencia cardíaca serían datos asociados. A diferencia de los datos de subtipo, que forman parte del registro de sesión, los datos asociados constan de registros independientes, cada uno con su propio UUID.
Cómo verificar la disponibilidad de Health Connect

Antes de intentar usar Health Connect, tu app debe verificar que esté disponible en el dispositivo del usuario. Es posible que Health Connect no esté preinstalado en todos los dispositivos o que esté inhabilitado. Puedes verificar la disponibilidad con el método HealthConnectClient.getSdkStatus().
Cómo verificar la disponibilidad de Health Connect

Según el estado que devuelva getSdkStatus(), puedes guiar al usuario para que instale o actualice Health Connect desde Google Play Store si es necesario.
Disponibilidad de funciones

No hay una marca de disponibilidad de funciones para este tipo de datos.
Permisos necesarios

El acceso a la sesión de sueño está protegido por los siguientes permisos:

    android.permission.health.READ_SLEEP
    android.permission.health.WRITE_SLEEP

Para agregar la función de sesión de sueño a tu app, comienza por solicitar permisos para el tipo de datos SleepSession.

Este es el permiso que debes declarar para poder escribir una sesión de sueño:

<application>
  <uses-permission
android:name="android.permission.health.WRITE_SLEEP" />
...
</application>

Para leer la sesión de sueño, debes solicitar los siguientes permisos:

<application>
  <uses-permission
android:name="android.permission.health.READ_SLEEP" />
...
</application>

Solicita permisos al usuario

Después de crear una instancia de cliente, tu app debe solicitarle permisos al usuario. Los usuarios deben poder otorgar o rechazar permisos en cualquier momento.

Para hacerlo, crea un conjunto de permisos para los tipos de datos necesarios. Primero, asegúrate de que los permisos del conjunto se declaren en tu manifiesto de Android.

```bash
// Create a set of permissions for required data types
val PERMISSIONS =
    setOf(
  HealthPermission.getReadPermission(SleepSessionRecord::class),
  HealthPermission.getWritePermission(SleepSessionRecord::class)
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
Agregaciones admitidas

Los siguientes valores agregados están disponibles para SleepSessionRecord:

    SLEEP_DURATION_TOTAL

Guía general

Estos son algunos lineamientos de las prácticas recomendadas para trabajar con sesiones de sueño en Health Connect.

    Debes usar sesiones para agregar datos de una sesión de sueño específica, o bien para dormir:

```bash
suspend fun writeSleepSession(healthConnectClient: HealthConnectClient) {
    healthConnectClient.insertRecords(
        listOf(
            SleepSessionRecord(
                startTime = Instant.parse("2022-05-10T23:00:00.000Z"),
                startZoneOffset = ZoneOffset.of("-08:00"),
                endTime = Instant.parse("2022-05-11T07:00:00.000Z"),
                endZoneOffset = ZoneOffset.of("-08:00"),
                title = "My Sleep"
            ),
        )
    )
}
```

    Los datos de subtipo deben alinearse en una sesión con marcas de tiempo secuenciales que no se superpongan. Sin embargo, se permiten vacíos.
    Los datos de subtipo no contienen un UUID, pero los datos asociados tienen UUID distintos.
    Las sesiones son útiles si el usuario desea que los datos se asocien con una sesión, y que se haga un seguimiento de ellos como parte de ella, en lugar de grabarla de forma continua.

Sesiones de sueño

Puedes leer o escribir datos de sueño en Health Connect. Los datos de sueño se muestran como una sesión y se pueden dividir en 8 fases del sueño distintas:

    UNKNOWN: No se especifica o se desconoce si el usuario está durmiendo.
    AWAKE: El usuario está despierto en un ciclo de sueño, no durante el día.
    SLEEPING: Descripción del sueño genérica o no detallada.
    OUT_OF_BED: El usuario se levanta de la cama en medio de una sesión de sueño.
    AWAKE_IN_BED: El usuario está despierto en la cama.
    LIGHT: El usuario se encuentra en un ciclo de sueño ligero.
    DEEP: El usuario se encuentra en un ciclo de sueño profundo.
    REM: El usuario se encuentra en un ciclo de sueño REM.

Estos valores representan el tipo de sueño que experimenta un usuario durante un intervalo de tiempo. La escritura sobre fases del sueño es opcional, pero te recomendamos que lo hagas si está disponible.
Cómo registrar sesiones de sueño

El tipo de datos SleepSessionRecord tiene dos partes:

    La sesión general, que abarca toda la duración del sueño
    Fases individuales durante la sesión de sueño, como el sueño ligero o el sueño profundo

A continuación, te mostramos cómo insertar una sesión de sueño sin fases:

```bash
SleepSessionRecord(
      title = "weekend sleep",
      startTime = startTime,
      endTime = endTime,
      startZoneOffset = ZoneOffset.UTC,
      endZoneOffset = ZoneOffset.UTC,
)
```

Sigue estos pasos para agregar fases que abarquen todo el período de una sesión de sueño:

```bash
val stages = listOf(
    SleepSessionRecord.Stage(
        startTime = Instant.parse("2022-05-10T23:00:00.000Z"),
        endTime = Instant.parse("2022-05-11T01:00:00.000Z"),
        stage = SleepSessionRecord.STAGE_TYPE_SLEEPING,
    ),
    SleepSessionRecord.Stage(
        startTime = Instant.parse("2022-05-11T01:00:00.000Z"),
        endTime = Instant.parse("2022-05-11T02:30:00.000Z"),
        stage = SleepSessionRecord.STAGE_TYPE_LIGHT,
    ),
    SleepSessionRecord.Stage(
        startTime = Instant.parse("2022-05-11T02:30:00.000Z"),
        endTime = Instant.parse("2022-05-11T05:00:00.000Z"),
        stage = SleepSessionRecord.STAGE_TYPE_DEEP,
    ),
    SleepSessionRecord.Stage(
        startTime = Instant.parse("2022-05-11T05:00:00.000Z"),
        endTime = Instant.parse("2022-05-11T07:00:00.000Z"),
        stage = SleepSessionRecord.STAGE_TYPE_REM,
    ),
)

SleepSessionRecord(
        title = "weekend sleep",
        startTime = Instant.parse("2022-05-10T23:00:00.000Z"),
        endTime = Instant.parse("2022-05-11T07:00:00.000Z"),
        startZoneOffset = ZoneOffset.of("-08:00"),
        endZoneOffset = ZoneOffset.of("-08:00"),
        stages = stages,
)
```

Cómo leer una sesión de sueño

En cada sesión de sueño que se muestra, debes comprobar si también hay datos disponibles de la fase del sueño:

```bash
suspend fun readSleepSessions(
    healthConnectClient: HealthConnectClient,
    startTime: Instant,
    endTime: Instant
) {
    val response =
        healthConnectClient.readRecords(
            ReadRecordsRequest(
                SleepSessionRecord::class,
                timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
            )
        )
    for (sleepRecord in response.records) {
        // Retrieve relevant sleep stages from each sleep record
        val sleepStages = sleepRecord.stages
    }
}
```

Cómo borrar una sesión de sueño

Así es como se borra una sesión. En este ejemplo, usamos una sesión de sueño:

```bash
suspend fun deleteSleepSession(
    healthConnectClient: HealthConnectClient,
    sleepRecord: SleepSessionRecord,
) {
    val timeRangeFilter = TimeRangeFilter.between(sleepRecord.startTime, sleepRecord.endTime)
    healthConnectClient.deleteRecords(SleepSessionRecord::class, timeRangeFilter)
}
```