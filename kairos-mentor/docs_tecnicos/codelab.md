 Crea una integración completa con Health Connect
Acerca de este codelab
schedule
90 minutos
subject
Última actualización: 15 de octubre de 2025
account_circle
Escrito por Wei-Chen Chen
1. Introducción

e4a4985ad1cdae8b.png
¿Qué es Health Connect?

Health Connect es una plataforma de datos de salud destinada a desarrolladores de apps para Android. Proporciona una única interfaz consolidada para acceder a los datos de salud y actividad física de los usuarios y un comportamiento funcional coherente en todos los dispositivos. Con Health Connect, los usuarios tienen un almacenamiento seguro de datos de salud y actividad física en el dispositivo, con control total y transparencia en el acceso.
¿Cómo funciona Health Connect?

Health Connect admite más de 50 categorías y tipos de datos de salud y actividad física comunes, incluidos actividad, sueño, nutrición, medidas corporales y datos vitales, como frecuencia cardíaca y presión arterial.

Cómo funciona Health Connect

Con el permiso del usuario, los desarrolladores pueden leer y escribir datos en Health Connect de forma segura a través de esquemas estandarizados y comportamiento de la API. Los usuarios obtienen control total sobre su configuración de privacidad, con controles granulares para ver qué apps solicitan acceso a los datos en cualquier momento. Los datos de Health Connect se almacenan en el dispositivo y se encriptan. Los usuarios también obtienen la posibilidad de desactivar el acceso o borrar los datos que no deseen en sus dispositivos y de priorizar una fuente de datos sobre otra cuando usen varias apps.
Arquitectura de Health Connect

arquitectura

A continuación, se explican los aspectos clave y los componentes de la arquitectura de Health Connect:

    App cliente: Para integrarse con Health Connect, la app cliente vincula el SDK a su app de salud y fitness. Esto proporciona una plataforma de API para interactuar con la API de Health Connect.
    Kit de desarrollo de software: El SDK permite que la app cliente se comunique con el APK de Health Connect.
    APK de Health Connect: Este es el APK que implementa Health Connect. Contiene los componentes de administración de permisos y de administración de datos. El APK de Health Connect se pone a disposición directamente en el dispositivo del usuario, por lo que se centra en el dispositivo y no en la cuenta.
    Administración de permisos: Health Connect incluye una interfaz de usuario a través de la cual las apps solicitan permiso al usuario para mostrar datos. También proporciona una lista de los permisos de los usuarios existentes. Esto les permite a los usuarios administrar el acceso que les concedieron o rechazaron a varias aplicaciones.
    Administración de datos: Health Connect proporciona una interfaz de usuario con una descripción general de los datos registrados, ya sean el recuento de pasos, la velocidad del ciclismo, la frecuencia cardíaca y otros tipos de datos admitidos.

Qué compilarás

En este codelab, compilarás una app de salud y fitness simple integrada en Health Connect. Tu app hará lo siguiente:

    Obtendrá y verificará los permisos del usuario para acceder a los datos.
    Escribirá datos en Health Connect.
    Leerá datos agregados de Health Connect.

Qué aprenderás

    Cómo configurar tu entorno para admitir el desarrollo de la integración de Health Connect
    Cómo obtener permisos y ejecutar verificaciones de permisos
    Cómo aportar datos de salud y actividad física a la plataforma de Health Connect
    Cómo beneficiarse del almacenamiento de datos en el dispositivo
    Cómo validar tu app con las herramientas para desarrolladores que brinda Google

Requisitos

    La versión estable más reciente de Android Studio
    Dispositivo móvil Android con la versión 28 (Pie) o posterior del SDK de Android

2. Prepárate
Prepara la app de Health Connect

La app de Health Connect es responsable de controlar todas las solicitudes que envía tu aplicación a través del SDK de Health Connect. Estas solicitudes incluyen almacenar datos y administrar su acceso de lectura y escritura.

El acceso a Health Connect depende de la versión de Android instalada en el teléfono. En las siguientes secciones, se describe cómo controlar varias versiones recientes de Android.
Android 14

A partir de Android 14 (nivel de API 34), Health Connect forma parte del framework de Android. Como esta versión de Health Connect es un módulo del framework, no se requiere configuración.
Android 13 y versiones anteriores

En Android 13 (nivel de API 33) y versiones anteriores, Health Connect no forma parte del framework de Android. Por lo tanto, debes instalar la app de Health Connect desde Google Play Store. Escanea el código QR para instalar Health Connect.

633ed0490a74595d.png
Obtén el código de muestra

Comienza por clonar el código fuente de GitHub:

git clone https://github.com/android/android-health-connect-codelab.git

El directorio de ejemplo contiene los códigos start y finished para este codelab. En la vista Project de Android Studio, encontrarás dos módulos:

    start: Es el código de partida para este proyecto, en el que realizarás cambios para completar el codelab.
    finished: Es el código completo de este codelab, que se usa para verificar tu trabajo.

Nota: En cualquier momento, puedes ejecutar cualquiera de los módulos en Android Studio si realizas cambios en la configuración de ejecución en la barra de herramientas.
Explora el código de inicio

La app de ejemplo del codelab tiene IUs básicas compiladas por Jetpack Compose con las siguientes pantallas:

    WelcomeScreen: Es la página de destino de la app que muestra diferentes mensajes, según la disponibilidad de Health Connect, ya sea que esté instalada o no, o no sea compatible.
    PrivacyPolicyScreen: Explica el uso de permisos de la app, que se muestra cuando el usuario hace clic en el vínculo de la política de privacidad en el diálogo de permisos de Health Connect.
    InputReadingsScreen: Demuestra cómo leer y escribir registros de peso simples.
    ExerciseSessionScreen: El lugar en el que los usuarios insertan y enumeran las sesiones de ejercicio. Cuando el usuario hace clic en el registro, se lo dirige a ExerciseSessionDetailScreen para que muestre más datos asociados con la sesión.
    DifferentialChangesScreen: Demuestra cómo obtener un token de cambios y cambios nuevos de Health Connect.

HealthConnectManager almacena todas las funciones que interactúan con Health Connect. En este codelab, te guiaremos paso a paso para que completes las funciones esenciales. Las cadenas <!-- TODO: dentro de la compilación start tienen las secciones correspondientes de este codelab, en las que se proporcionan códigos de muestra para que los insertes en el proyecto.

Comencemos por agregar Health Connect al proyecto.
Agrega el SDK cliente de Health Connect

Para comenzar a usar el SDK de Health Connect, debes agregar una dependencia al archivo build.gradle. Para encontrar la versión más reciente de Health Connect, consulta la versión de la biblioteca de Jetpack.

dependencies {
    // Add a dependency of Health Connect SDK
    implementation "androidx.health.connect:connect-client:1.1.0-alpha11"
}

Nota: El proyecto start del codelab agregó la dependencia. Este paso es solo para tus propias referencias de desarrollo de apps.
Declara la visibilidad de Health Connect

Para interactuar con Health Connect dentro de la app, declara el nombre del paquete de Health Connect en el archivo AndroidManifest.xml:

<!-- TODO: declare Health Connect visibility -->
<queries>
   <package android:name="com.google.android.apps.healthdata" />
</queries>

Ejecuta el proyecto de inicio

Una vez que esté todo listo, ejecuta el proyecto start. En este punto, deberías ver la pantalla de bienvenida que indica que Health Connect está instalado en el dispositivo y un panel lateral del menú. Agregaremos las funciones para interactuar con Health Connect en secciones posteriores.

8f063e5b305189.png fd39f325f5c19e5d.png

Nota: Para proteger tus datos, Health Connect requiere que bloquees el teléfono con un PIN, un patrón o una contraseña. Ve a Configuración en el teléfono para establecer un bloqueo de pantalla y acceder a Health Connect.
3. Control de permisos

Health Connect recomienda a los desarrolladores restringir las solicitudes de permisos a los tipos de datos que se usan en la app. Las solicitudes de permisos generales reducen la confianza del usuario en la app. Si se deniega un permiso más de dos veces, tu app se bloquea. Como resultado, las solicitudes de permisos dejarán de aparecer.

Para los fines de este codelab, solo necesitamos los siguientes permisos:

    Sesión de ejercicio
    Frecuencia cardíaca
    Pasos
    Total de calorías quemadas
    Peso

Cómo declarar permisos

Se debe declarar cada tipo de datos que tu app lea o escriba con un permiso en AndroidManifest.xml. A partir de la versión 1.0.0-alpha10, Health Connect usa el formato de declaración de permisos estándar de Android.

Para declarar los permisos de los tipos de datos requeridos, usa los elementos <uses-permission> y asígnales sus respectivos nombres con los permisos. Anídalos dentro de las etiquetas <manifest>. Para obtener la lista completa de permisos y sus tipos de datos correspondientes, consulta la lista de tipos de datos.

<!-- TODO: Required to specify which Health Connect permissions the app can request -->
  <uses-permission android:name="android.permission.health.READ_HEART_RATE"/>
  <uses-permission android:name="android.permission.health.WRITE_HEART_RATE"/>
  <uses-permission android:name="android.permission.health.READ_STEPS"/>
  <uses-permission android:name="android.permission.health.WRITE_STEPS"/>
  <uses-permission android:name="android.permission.health.READ_EXERCISE"/>
  <uses-permission android:name="android.permission.health.WRITE_EXERCISE"/>
  <uses-permission android:name="android.permission.health.READ_TOTAL_CALORIES_BURNED"/>
  <uses-permission android:name="android.permission.health.WRITE_TOTAL_CALORIES_BURNED"/>
  <uses-permission android:name="android.permission.health.READ_WEIGHT"/>
  <uses-permission android:name="android.permission.health.WRITE_WEIGHT"/>

Declara un filtro de intents en AndroidManifest.xml para controlar el intent que explica cómo tu app usa esos permisos. La app necesita controlar este intent y mostrar una política de privacidad en la que se describen cómo se usan y manejan los datos del usuario. Este intent se envía a la app una vez que el usuario presiona el vínculo de la política de privacidad, en el diálogo de permisos de Health Connect.

<!-- TODO: Add intent filter to handle permission rationale intent -->
<!-- Permission handling for Android 13 and before -->
<intent-filter>
  <action android:name="androidx.health.ACTION_SHOW_PERMISSIONS_RATIONALE" />
</intent-filter>

<!-- Permission handling for Android 14 and later -->
<intent-filter>
  <action android:name="android.intent.action.VIEW_PERMISSION_USAGE"/>
  <category android:name="android.intent.category.HEALTH_PERMISSIONS"/>
</intent-filter>

Ahora vuelve a abrir la app para ver los permisos declarados. Haz clic en Settings en el panel lateral del menú para ir a la pantalla de configuración de Health Connect. Luego, haz clic en App permissions, donde deberías ver Health Connect Codelab en la lista. Haz clic en Health Connect Codelab para mostrar una lista de los tipos de datos para el acceso de lectura y escritura en esa app.

fbed69d871f92178.png 1b9c7764c1dbdfac.png
Solicita permisos

Además de dirigir a los usuarios directamente a la configuración de Health Connect para administrar los permisos, también puedes solicitar permisos de tu app a través de las APIs de Health Connect. Ten en cuenta que los usuarios pueden cambiar los permisos en cualquier momento, por lo que debes asegurarte de que tu app verifique si hay permisos necesarios disponibles. En el proyecto de codelab, revisamos y enviamos solicitudes de permisos antes de leer o escribir datos.

HealthConnectClient es un punto de entrada a la API de Health Connect. En HealthConnectManager.kt, obtén una instancia de HealthConnectClient.

private val healthConnectClient by lazy { HealthConnectClient.getOrCreate(context) }

Para iniciar el diálogo de solicitud de permisos dentro de tu aplicación, primero, compila un conjunto de permisos para los tipos de datos obligatorios. Solo debes solicitar permisos para los tipos de datos que usas.

Por ejemplo, en la pantalla para registrar peso, solo debes otorgar permisos de lectura y escritura para el elemento Weight. Creamos un conjunto de permisos en InputReadingsViewModel.kt como se muestra en el siguiente código.

  val permissions = setOf(
    HealthPermission.getReadPermission(WeightRecord::class),
    HealthPermission.getWritePermission(WeightRecord::class),
  )

Luego, verifica si los permisos se otorgaron antes de iniciar la solicitud de permiso. En HealthConnectManager.kt, usa getGrantedPermissions para verificar si se otorgó el permiso de los tipos de datos necesarios. Para iniciar la solicitud de permiso, debes crear un ActivityResultContract con PermissionController.createRequestPermissionResultContract(), que debería iniciarse cuando no se otorguen los permisos necesarios.

  suspend fun hasAllPermissions(permissions: Set<String>): Boolean {
    return healthConnectClient.permissionController.getGrantedPermissions().containsAll(permissions)
  }

  fun requestPermissionsActivityContract(): ActivityResultContract<Set<String>, Set<String>> {
    return PermissionController.createRequestPermissionResultContract()
  }

En la app de ejemplo del codelab, es posible que veas el botón Request permissions en la pantalla si no otorgaste los permisos a los tipos de datos necesarios. Haz clic en Request permissions para abrir el diálogo del permiso de Health Connect. Otorga los permisos necesarios y vuelve a la app del codelab.

a0eb27cea376e56f.png 4752973f6b0b8d56.png
4. Escribe datos

Comencemos a escribir registros en Health Connect. Para escribir un registro de peso, crea un objeto WeightRecord con el valor de entrada de peso. Ten en cuenta que el SDK de Health Connect admite varias clases de unidades. Por ejemplo, usa Mass.kilograms(weightInput) para establecer el peso de los usuarios en kilogramos.

Todos los datos que se escriban en Health Connect deben especificar información de desfase de zona. Especificar la información de desfase de zona mientras se escriben datos permite contar con información de zona horaria cuando se leen datos en Health Connect.

Después de crear el registro de peso, usa healthConnectClient.insertRecords para escribir los datos en Health Connect.

/**
* TODO: Writes [WeightRecord] to Health Connect.
*/
suspend fun writeWeightInput(weightInput: Double) {
   val time = ZonedDateTime.now().withNano(0)
   val weightRecord = WeightRecord(
       metadata = Metadata.manualEntry(),
       weight = Mass.kilograms(weightInput),
       time = time.toInstant(),
       zoneOffset = time.offset
   )
   val records = listOf(weightRecord)
   try {
      healthConnectClient.insertRecords(records)
      Toast.makeText(context, "Successfully insert records", Toast.LENGTH_SHORT).show()
   } catch (e: Exception) {
      Toast.makeText(context, e.message.toString(), Toast.LENGTH_SHORT).show()
   }
}

Ahora ejecutemos la app. Haz clic en Record weight y, luego, ingresa un nuevo registro de peso en kilogramos. Para verificar si se registró correctamente el peso en Health Connect, abre la app de Health Connect en Configuración y ve a Datos y acceso > Medidas corporales > Peso > Ver todas las entradas. Deberías ver el nuevo registro de peso escrito de Health Connect Codelab.
Cómo escribir sesiones de ejercicio

Una sesión es un intervalo de tiempo durante el cual un usuario realiza una actividad. Una sesión de ejercicio en Health Connect puede incluir cualquier actividad, desde correr hasta jugar bádminton. Las sesiones permiten que los usuarios midan el rendimiento basado en el tiempo. Estos datos registran una variedad de muestras instantáneas que se miden durante un período, por ejemplo, las muestras de frecuencia cardíaca continua o de ubicaciones cuando se realiza una actividad.

En el siguiente ejemplo, se muestra cómo escribir una sesión de ejercicio. Usa healthConnectClient.insertRecords para insertar varios registros de datos asociados con una sesión. La solicitud de inserción de este ejemplo incluye ExerciseSessionRecord con ExerciseType, StepsRecord con el recuento de pasos, TotalCaloriesBurnedRecord con Energy y una serie de muestras de HeartRateRecord.

  /**
   * TODO: Writes an [ExerciseSessionRecord] to Health Connect.
   */
  suspend fun writeExerciseSession(start: ZonedDateTime, end: ZonedDateTime) {
    healthConnectClient.insertRecords(
      listOf(
        ExerciseSessionRecord(
          metadata = Metadata.manualEntry(),
          startTime = start.toInstant(),
          startZoneOffset = start.offset,
          endTime = end.toInstant(),
          endZoneOffset = end.offset,
          exerciseType = ExerciseSessionRecord.EXERCISE_TYPE_RUNNING,
          title = "My Run #${Random.nextInt(0, 60)}"
        ),
        StepsRecord(
          metadata = Metadata.manualEntry(),
          startTime = start.toInstant(),
          startZoneOffset = start.offset,
          endTime = end.toInstant(),
          endZoneOffset = end.offset,
          count = (1000 + 1000 * Random.nextInt(3)).toLong()
        ),
        TotalCaloriesBurnedRecord(
          metadata = Metadata.manualEntry(),
          startTime = start.toInstant(),
          startZoneOffset = start.offset,
          endTime = end.toInstant(),
          endZoneOffset = end.offset,
          energy = Energy.calories((140 + Random.nextInt(20)) * 0.01)
        )
      ) + buildHeartRateSeries(start, end)
    )
  }

  /**
   * TODO: Build [HeartRateRecord].
   */
  private fun buildHeartRateSeries(
    sessionStartTime: ZonedDateTime,
    sessionEndTime: ZonedDateTime,
  ): HeartRateRecord {
    val samples = mutableListOf<HeartRateRecord.Sample>()
    var time = sessionStartTime
    while (time.isBefore(sessionEndTime)) {
      samples.add(
        HeartRateRecord.Sample(
          time = time.toInstant(),
          beatsPerMinute = (80 + Random.nextInt(80)).toLong()
        )
      )
      time = time.plusSeconds(30)
    }
    return HeartRateRecord(
      metadata = Metadata.manualEntry(),
      startTime = sessionStartTime.toInstant(),
      startZoneOffset = sessionStartTime.offset,
      endTime = sessionEndTime.toInstant(),
      endZoneOffset = sessionEndTime.offset,
      samples = samples
    )
  }

5. Lee datos

Ahora escribiste registros de peso y sesiones ejercicio con la app de ejemplo del codelab o la app de Toolbox. Usemos la API de Health Connect para leer esos registros. Primero, crea una ReadRecordsRequest y especifica el tipo de registro y el período durante el que se leerá. ReadRecordsRequest también puede configurar un dataOriginFilter para especificar la app de origen del registro desde el que quieres leer.

    /**
     * TODO: Reads in existing [WeightRecord]s.
     */
    suspend fun readWeightInputs(start: Instant, end: Instant): List<WeightRecord> {
        val request = ReadRecordsRequest(
            recordType = WeightRecord::class,
            timeRangeFilter = TimeRangeFilter.between(start, end)
        )
        val response = healthConnectClient.readRecords(request)
        return response.records
    }

  /**
   * TODO: Obtains a list of [ExerciseSessionRecord]s in a specified time frame.
   */
  suspend fun readExerciseSessions(start: Instant, end: Instant): List<ExerciseSessionRecord> {
    val request = ReadRecordsRequest(
      recordType = ExerciseSessionRecord::class,
      timeRangeFilter = TimeRangeFilter.between(start, end)
    )
    val response = healthConnectClient.readRecords(request)
    return response.records
  }

Ahora ejecutemos la app y verifiquemos si puedes ver una lista de registros de peso y sesiones de ejercicio.

a08af54eef6bc832.png 3b0781389f1094a1.png
6. Lee los datos en segundo plano
Declara el permiso

Para acceder a los datos de salud en segundo plano, declara el permiso READ_HEALTH_DATA_IN_BACKGROUND en tu archivo AndroidManifest.xml.

<!-- TODO: Required to specify which Health Connect permissions the app can request -->
...
<uses-permission android:name="android.permission.health.READ_HEALTH_DATA_IN_BACKGROUND" />

Revisa la disponibilidad de las funciones

Dado que es posible que los usuarios no siempre tengan la versión más reciente de Health Connect, lo mejor es verificar primero la disponibilidad de las funciones. En HealthConnectManager.kt, usamos el método getFeatureStatus() para hacerlo.

fun isFeatureAvailable(feature: Int): Boolean{
    return healthConnectClient
      .features
      .getFeatureStatus(feature) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE
  }

La funcionalidad de lectura en segundo plano en ExerciseSessionViewModel.kt se verifica con la constante FEATURE_READ_HEALTH_DATA_IN_BACKGROUND:

backgroundReadAvailable.value = healthConnectManager.isFeatureAvailable(
    HealthConnectFeatures.FEATURE_READ_HEALTH_DATA_IN_BACKGROUND
)

Solicita permisos

Después de verificar que la función de lectura en segundo plano esté disponible, puedes solicitar el permiso PERMISSION_READ_HEALTH_DATA_IN_BACKGROUND haciendo clic en Solicitar lectura en segundo plano en la pantalla Sesiones de ejercicio.

Los usuarios ven el siguiente mensaje:

edfb507d0976427a.png

Los usuarios también pueden otorgar acceso a las lecturas en segundo plano navegando a Health Connect > Permisos de la app > Codelab de Health Connect > Acceso adicional > Acceso a los datos en segundo plano en la configuración del sistema:

154a4ebf8069457a.png
Lee los datos en segundo plano

Usa WorkManager para programar tareas en segundo plano. Cuando presiones el botón Leer pasos en segundo plano, la app iniciará ReadStepWorker después de un retraso de 10 segundos. Este Worker recuperará el recuento total de pasos de Health Connect de las últimas 24 horas. Luego, aparecerá una entrada de registro similar que detallará esta información en Logcat:

There are 4000 steps in Health Connect in the last 24 hours.

Nota: Es posible que debas cerrar la app inmediatamente después de presionar el botón para asegurarte de que ReadStepWorker se ejecute en segundo plano.
7. Lee los datos históricos
Declara el permiso

Para acceder a los datos de salud de otras aplicaciones con más de 30 días de antigüedad, declara el permiso READ_HEALTH_DATA_HISTORY en el archivo AndroidManifest.xml.

<!-- TODO: Required to specify which Health Connect permissions the app can request -->
...
<uses-permission android:name="android.permission.health.READ_HEALTH_DATA_HISTORY" />

Revisa la disponibilidad de las funciones

Dado que es posible que los usuarios no siempre tengan la versión más reciente de Health Connect, lo mejor es verificar primero la disponibilidad de las funciones. En HealthConnectManager.kt, usamos el método getFeatureStatus() para hacerlo.

fun isFeatureAvailable(feature: Int): Boolean{
    return healthConnectClient
      .features
      .getFeatureStatus(feature) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE
  }

La función de lectura del historial en ExerciseSessionViewModel.kt se verifica con la constante FEATURE_READ_HEALTH_DATA_HISTORY:

historyReadAvailable.value = healthConnectManager.isFeatureAvailable(
    HealthConnectFeatures.FEATURE_READ_HEALTH_DATA_HISTORY
)

Solicita permisos

Después de verificar que la función de lectura del historial esté disponible, podrás solicitar el permiso PERMISSION_READ_HEALTH_DATA_HISTORY haciendo clic en Solicitar lectura del historial en la pantalla Sesiones de ejercicio.

Los usuarios ven el siguiente mensaje:

ff523ee39aeadd8e.png

Los usuarios también pueden otorgar acceso a las lecturas del historial si navegan a Health Connect > Permisos de la app > Codelab de Health Connect > Acceso adicional > Acceso a los datos anteriores en la configuración del sistema:

1ec187a6c63245b6.png
Lee los datos históricos

La pantalla Sesiones de ejercicio mostrará datos anteriores de otras apps cuando se haya otorgado acceso a la lectura del historial.

Nota: Si no tienes datos históricos de otras apps almacenados en tu dispositivo, usa la Caja de herramientas de Health Connect y navega a INSERT HEALTH RECORD > Activity > ExerciseSession para agregar manualmente una sesión de ejercicio de 40 días atrás.
8. Lee datos diferenciales

La API de Differential Changes de Health Connect permite realizar un seguimiento de los cambios desde un momento específico para un conjunto de tipos de datos. Por ejemplo, quieres saber si los usuarios actualizaron o borraron algún registro existente fuera de la app para poder actualizar tu base de datos de forma acorde.

La lectura de datos con Health Connect está restringida a las aplicaciones que se ejecutan en primer plano. Se implementó esta restricción para fortalecer aún más la privacidad del usuario. Notifica y garantiza a los usuarios que Health Connect no tiene acceso de lectura en segundo plano a sus datos, y que solo se puede leer y acceder a ellos en primer plano. Cuando la app está en primer plano, la API de Differential Changes permite a los desarrolladores recuperar los cambios realizados en Health Connect a través de la implementación de un token de cambios.

En HealthConnectManager.kt hay dos funciones: getChangesToken() y getChanges(). Agregaremos las APIs de Differential Changes a estas funciones para obtener los cambios en los datos.
Configuración del token inicial de cambios

Los cambios en los datos se recuperan de Health Connect solo cuando tu app los solicita con un token de cambios. El token de cambios representa el punto en el historial de confirmaciones desde el que se tomarán los datos diferenciales.

Para obtener un token de cambios, envía una ChangesTokenRequest con el conjunto de tipos de datos de cuyos cambios desees hacer un seguimiento. Conserva el token y úsalo cuando quieras recuperar cualquier actualización de Health Connect.

Nota: DeletionChanges solo devuelve id del registro borrado, sin el tipo de registro que se usa en deleteRecords, debido a cuestiones de privacidad. Para controlar esto, puedes especificar solo 1 tipo de datos para cada llamada a getChanges o puedes asegurarte de haber almacenado esta información por separado de antemano.

  /**
   * TODO: Obtains a Changes token for the specified record types.
   */
  suspend fun getChangesToken(): String {
    return healthConnectClient.getChangesToken(
      ChangesTokenRequest(
        setOf(
          ExerciseSessionRecord::class
        )
      )
    )
  }

Actualización de datos con un token de cambios

Cuando quieras obtener cambios de la última vez que tu app se sincronizó con Health Connect, usa el token de cambios que obtuviste anteriormente y envía una llamada getChanges con el token. ChangesResponse muestra una lista de los cambios observados desde Health Connect, como UpsertionChange y DeletionChange.

  /**
   * TODO: Retrieve changes from a Changes token.
   */
  suspend fun getChanges(token: String): Flow<ChangesMessage> = flow {
    var nextChangesToken = token
    do {
      val response = healthConnectClient.getChanges(nextChangesToken)
      if (response.changesTokenExpired) {
        throw IOException("Changes token has expired")
      }
      emit(ChangesMessage.ChangeList(response.changes))
      nextChangesToken = response.nextChangesToken
    } while (response.hasMore)
    emit(ChangesMessage.NoMoreChanges(nextChangesToken))
  }

Nota: Los tokens de cambios solo son válidos por 30 días. Asegúrate de que tu app haga lo siguiente:

    Actualice periódicamente los datos para cualquier cambio en un plazo de 30 días o menos para evitar los tokens inactivos.
    Maneje casos en los que el token ya no es válido.
    Tenga un mecanismo de resguardo para obtener los datos necesarios.

Importante: Es posible que la primera respuesta que se muestra no siempre proporcione todos los cambios realizados en Health Connect. Tal vez sea necesario realizar llamadas a la API adicionales y recuperar otros cambios para abordar este problema.

Ahora, ejecuta la app y ve a la pantalla Changes. Primero, habilita Track changes para obtener un token de cambios. Luego, inserta el peso o las sesiones de ejercicio desde Toolbox o desde la app del codelab. Regresa a la pantalla Changes y selecciona Get new changes. Ahora deberías ver los cambios.

f3aded8ae5487e9c.png 437d69e3e000ce81.png
9. Datos agregados

Health Connect también proporciona datos agregados a través de APIs agregadas. En los siguientes ejemplos, se muestra cómo obtener datos estadísticos y acumulativos de Health Connect.

Usa healthConnectClient.aggregate para enviar AggregateRequest. En la solicitud agregada, especifica un conjunto de métricas agregadas y el período de tiempo que deseas obtener. Por ejemplo, ExerciseSessionRecord.EXERCISE_DURATION_TOTAL y StepsRecord.COUNT_TOTAL proporcionan datos acumulativos, mientras que WeightRecord.WEIGHT_AVG, HeartRateRecord.BPM_MAX y HeartRateRecord.BPM_MIN proporcionan datos estadísticos.

    /**
     * TODO: Returns the weekly average of [WeightRecord]s.
     */
    suspend fun computeWeeklyAverage(start: Instant, end: Instant): Mass? {
        val request = AggregateRequest(
            metrics = setOf(WeightRecord.WEIGHT_AVG),
            timeRangeFilter = TimeRangeFilter.between(start, end)
        )
        val response = healthConnectClient.aggregate(request)
        return response[WeightRecord.WEIGHT_AVG]
    }

En este ejemplo, se muestra cómo obtener datos agregados asociados para una sesión de ejercicio específica. Primero, lee un registro a través de healthConnectClient.readRecord con un uid. Luego, usa startTime y endTime de la sesión de ejercicio como el período de tiempo y dataOrigin como filtros para leer las agregaciones asociadas.

  /**
   * TODO: Reads aggregated data and raw data for selected data types, for a given [ExerciseSessionRecord].
   */
  suspend fun readAssociatedSessionData(
      uid: String,
  ): ExerciseSessionData {
    val exerciseSession = healthConnectClient.readRecord(ExerciseSessionRecord::class, uid)
    // Use the start time and end time from the session, for reading raw and aggregate data.
    val timeRangeFilter = TimeRangeFilter.between(
      startTime = exerciseSession.record.startTime,
      endTime = exerciseSession.record.endTime
    )
    val aggregateDataTypes = setOf(
      ExerciseSessionRecord.EXERCISE_DURATION_TOTAL,
      StepsRecord.COUNT_TOTAL,
      TotalCaloriesBurnedRecord.ENERGY_TOTAL,
      HeartRateRecord.BPM_AVG,
      HeartRateRecord.BPM_MAX,
      HeartRateRecord.BPM_MIN,
    )
    // Limit the data read to just the application that wrote the session. This may or may not
    // be desirable depending on the use case: In some cases, it may be useful to combine with
    // data written by other apps.
    val dataOriginFilter = setOf(exerciseSession.record.metadata.dataOrigin)
    val aggregateRequest = AggregateRequest(
      metrics = aggregateDataTypes,
      timeRangeFilter = timeRangeFilter,
      dataOriginFilter = dataOriginFilter
    )
    val aggregateData = healthConnectClient.aggregate(aggregateRequest)
    val heartRateData = readData<HeartRateRecord>(timeRangeFilter, dataOriginFilter)

    return ExerciseSessionData(
      uid = uid,
      totalActiveTime = aggregateData[ExerciseSessionRecord.EXERCISE_DURATION_TOTAL],
      totalSteps = aggregateData[StepsRecord.COUNT_TOTAL],
      totalEnergyBurned = aggregateData[TotalCaloriesBurnedRecord.ENERGY_TOTAL],
      minHeartRate = aggregateData[HeartRateRecord.BPM_MIN],
      maxHeartRate = aggregateData[HeartRateRecord.BPM_MAX],
      avgHeartRate = aggregateData[HeartRateRecord.BPM_AVG],
      heartRateSeries = heartRateData,
    )
  }

Ahora ejecuta la app y comprueba si puedes ver el peso promedio en la pantalla Record weight. También puedes ver los datos detallados de una sesión de ejercicio si abres la pantalla Exercise sessions y eliges uno de los registros de la sesión.

af1fe646159d6a60.png
10. Felicitaciones

Felicitaciones, compilaste correctamente tu primera app de salud y fitness integrada en Health Connect.

La app puede declarar permisos y solicitar permisos de usuario en los tipos de datos que se usan en la app. También puede leer y escribir datos del almacenamiento de datos de Health Connect. También aprendiste a usar Health Connect Toolbox para respaldar el desarrollo de tu app a través de la creación de datos ficticios en el almacenamiento de datos de Health Connect.

Ahora conoces los pasos clave necesarios para que tu app de salud y fitness forme parte del ecosistema de Health Connect.