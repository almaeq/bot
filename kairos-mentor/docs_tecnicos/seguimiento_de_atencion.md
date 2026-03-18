 Realiza un seguimiento de la atención plena

    Esta guía es compatible con la versión 1.1.0-rc01 de Health Connect.

Health Connect proporciona un tipo de datos de atención plena para medir varios aspectos de la salud mental, como el estrés y la ansiedad. La atención plena es un tipo de dato que forma parte del bienestar general en Health Connect.
Cómo verificar la disponibilidad de Health Connect

Antes de intentar usar Health Connect, tu app debe verificar que esté disponible en el dispositivo del usuario. Es posible que Health Connect no esté preinstalado en todos los dispositivos o que esté inhabilitado. Puedes verificar la disponibilidad con el método HealthConnectClient.getSdkStatus().
Cómo verificar la disponibilidad de Health Connect

Según el estado que devuelva getSdkStatus(), puedes guiar al usuario para que instale o actualice Health Connect desde Google Play Store si es necesario.
Disponibilidad de funciones
Para determinar si el dispositivo de un usuario admite registros de sesiones de mindfulness en Health Connect, verifica la disponibilidad de FEATURE_MINDFULNESS_SESSION en el cliente:

```bash
if (healthConnectClient
     .features
     .getFeatureStatus(
       HealthConnectFeatures.FEATURE_MINDFULNESS_SESSION
     ) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {

  // Feature is available
} else {
  // Feature isn't available
}
```

Consulta Cómo verificar la disponibilidad de funciones para obtener más información.
Permisos necesarios

El acceso a la función de mindfulness está protegido por los siguientes permisos:

    android.permission.health.READ_MINDFULNESS
    android.permission.health.WRITE_MINDFULNESS

Para agregar la función de mindfulness a tu app, comienza por solicitar permisos para el tipo de datos MindfulnessSession.

Este es el permiso que debes declarar para poder escribir datos de mindfulness:

<application>
  <uses-permission
android:name="android.permission.health.WRITE_MINDFULNESS" />
...
</application>

Para leer la actividad de atención plena, debes solicitar los siguientes permisos:

<application>
  <uses-permission
android:name="android.permission.health.READ_MINDFULNESS" />
...
</application>

Solicita permisos al usuario

Después de crear una instancia de cliente, tu app debe solicitarle permisos al usuario. Los usuarios deben poder otorgar o rechazar permisos en cualquier momento.

Para hacerlo, crea un conjunto de permisos para los tipos de datos necesarios. Primero, asegúrate de que los permisos del conjunto se declaren en tu manifiesto de Android.

```bash
// Create a set of permissions for required data types
val PERMISSIONS =
    setOf(
  HealthPermission.getReadPermission(MindfulnessSessionRecord::class),
  HealthPermission.getWritePermission(MindfulnessSessionRecord::class)
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
Información que se incluye en un registro de sesión de mindfulness

Cada registro de sesión de atención plena captura cualquier tipo de sesión de atención plena que realice un usuario, por ejemplo, meditación, respiración y movimiento. El registro también puede incluir notas adicionales sobre la sesión.
Agregaciones admitidas

Los siguientes valores agregados están disponibles para MindfulnessSessionRecord:

    MINDFULNESS_DURATION_TOTAL

Escribir sesión de mindfulness

En el siguiente fragmento de código, se muestra cómo escribir una sesión de atención plena:

```bash
if (healthConnectClient.features.getFeatureStatus(FEATURE_MINDFULNESS_SESSION) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {
        healthConnectClient.insertRecords(listOf(MindfulnessSessionRecord(
            startTime = Instant.now().minus(Duration.ofHours(1)),
            startZoneOffset = ZoneOffset.UTC,
            endTime = Instant.now(),
            endZoneOffset = ZoneOffset.UTC,
            mindfulnessSessionType = MindfulnessSessionRecord.MINDFULNESS_SESSION_TYPE_MEDITATION,
            title = "Lake meditation",
            notes = "Meditation by the lake",
            metadata = Metadata.activelyRecorded(
                clientRecordId = "myid",
                clientRecordVersion = 0.0,
                device = Device(type = Device.TYPE_PHONE)
            ),
        )))
    }
```

Leer sesión de mindfulness

En el siguiente fragmento de código, se muestra cómo leer una sesión de mindfulness dentro de un período:

```bash
Val now = Instant.now()

val records = healthConnectClient.readRecords(
    ReadRecordsRequest(
        recordType = MindfulnessSessionRecord::class,
        timeRangeFilter = TimeRangeFilter.between(
            startTime = now.minus(Duration.ofHours(5)),
            endTime = now
        )
    )
)

// Process the returned records
records.records.forEach { session ->
    println("Mindfulness session:")
    println("Start: ${session.startTime}")
    println("End: ${session.endTime}")
    println("Title: ${session.title}")
    println("Notes: ${session.notes}")
    println("Type: ${session.mindfulnessSessionType}")
}
```