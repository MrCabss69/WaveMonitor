# Ondas y Aplicaciones en Detección, Seguimiento y Ciberseguridad

## Introducción

Las ondas, tanto **mecánicas** como **electromagnéticas**, son fundamentales para numerosas tecnologías utilizadas en la **detección, seguimiento y comunicación** de objetos y dispositivos electrónicos. Este documento explora las características de las ondas, sus aplicaciones en diversos campos, y su importancia en la **ciberseguridad moderna**. Además, se analizan las posibles interferencias, los ataques basados en ondas y las contramedidas tecnológicas emergentes.

---

## Clasificación de Ondas

Las ondas pueden clasificarse en **ondas mecánicas** (sonoras) y **ondas electromagnéticas**, diferenciándose principalmente por su mecanismo de propagación y su dependencia (o no) de un medio físico.

### Ondas Mecánicas (Sonoras)

- **Definición**: Perturbaciones que se propagan a través de un medio (sólido, líquido o gaseoso) mediante la vibración de partículas.
- **Rango de frecuencias**:
  - **Audible**: 20 Hz - 20 kHz.
  - **Ultrasonidos**: Por encima de 20 kHz, típicamente hasta 100 kHz.
- **Propagación**:
  - Requieren un medio físico para viajar; no se propagan en el vacío.
  - La velocidad depende del medio: sólidos > líquidos > gases.
- **Características**:
  - Alta atenuación en medios porosos o gaseosos, lo que reduce su alcance.
  - **Aplicaciones**: Detección de proximidad, sonar submarino, ecografía médica.

### Ondas Electromagnéticas

- **Definición**: Oscilaciones de campos eléctricos y magnéticos que pueden propagarse en el vacío.
- **Rango de frecuencias**: Desde **ondas de radio** (3 kHz) hasta **rayos gamma** (300 EHz).
- **Propagación**:
  - Velocidad en el vacío: ~300,000 km/s.
  - La absorción y reflexión dependen del medio: los **conductores reflejan**, mientras que los **dieléctricos** permiten una transmisión con ciertas pérdidas.
- **Características**:
  - Incluyen microondas, infrarrojos, luz visible y rayos X.
  - **Aplicaciones**: Comunicaciones, radares, cámaras térmicas.

---

## Comparativa entre Ondas Mecánicas y Electromagnéticas

| Característica               | Ondas Mecánicas               | Ondas Electromagnéticas        |
|-----------------------------|-------------------------------|-------------------------------|
| **Medio de propagación**    | Requieren un medio físico     | No requieren medio físico     |
| **Velocidad en el vacío**   | No aplicable                  | ~300,000 km/s                 |
| **Rango de frecuencias**    | 20 Hz - 100 kHz               | 3 kHz - 300 EHz               |
| **Aplicaciones**            | Sonar, ecografía              | Comunicaciones, radares       |

---

## Aplicaciones y Tecnologías Basadas en Ondas

En esta sección se detallan las propiedades y aplicaciones de diversos tipos de ondas, empleadas para la detección y seguimiento en distintos contextos.

### 1. Ultrasonidos (20 kHz - 100 kHz)
- **Naturaleza**: Ondas mecánicas de alta frecuencia.
- **Propagación**:
  - Eficientes en medios sólidos y líquidos; alta atenuación en gases.
  - No se propagan en el vacío.
- **Aplicaciones**:
  - **Sensores de proximidad**: Vehículos y robótica.
  - **Sonar submarino**: Localización de objetos bajo el agua.
  - **Ecografía médica**: Visualización de tejidos blandos.

### 2. Infrarrojos (300 GHz - 430 THz)
- **Naturaleza**: Ondas electromagnéticas situadas entre microondas y luz visible.
- **Propagación**:
  - No atraviesan materiales opacos; susceptibles a la absorción atmosférica.
- **Aplicaciones**:
  - **Cámaras térmicas**: Vigilancia y búsqueda en condiciones de baja visibilidad.
  - **Sensores PIR**: Sistemas de seguridad basados en detección de movimiento.

### 3. Microondas (300 MHz - 300 GHz)
- **Naturaleza**: Ondas electromagnéticas de alta frecuencia.
- **Propagación**:
  - Atraviesan paredes y materiales dieléctricos; absorbidas por agua y vegetación.
- **Aplicaciones**:
  - **Radares**: Detección de vehículos y drones.
  - **Seguimiento de dispositivos**: Uso en Wi-Fi y Bluetooth.

### 4. Ondas de Radio (3 kHz - 300 GHz)
- **Naturaleza**: Ondas electromagnéticas de baja frecuencia.
- **Propagación**:
  - Excelente alcance en exteriores; reflejan y difractan en entornos urbanos.
- **Aplicaciones**:
  - **GPS y UWB**: Geolocalización y rastreo preciso en interiores.

---


## Aplicaciones

Las tecnologías basadas en ondas electromagnéticas y mecánicas son ampliamente utilizadas en la ciberseguridad para la **detección, identificación y rastreo** de dispositivos, así como para la protección de infraestructuras críticas. A continuación, se describen aplicaciones específicas en la detección de intrusos, la geolocalización y la protección contra ataques basados en ondas.

**Detección y Seguimiento**

| **Tecnología**        | **Frecuencia**       | **Aplicaciones**                           | **Condiciones de Propagación**             | **Limitaciones**                   |
|-----------------------|----------------------|--------------------------------------------|--------------------------------------------|------------------------------------|
| **Ultrasonidos**      | 20 kHz - 100 kHz     | Proximidad, ecografía, sonar                | Eficientes en sólidos y líquidos           | Alta atenuación en el aire         |
| **Infrarrojos**       | 300 GHz - 430 THz    | Cámaras térmicas, sensores PIR              | Limitada en medios opacos                  | Sensible a fuentes de calor        |
| **Microondas**        | 300 MHz - 300 GHz    | Radares, Wi-Fi, Bluetooth tracking           | Atraviesan materiales dieléctricos         | Interferencias en metales          |
| **Ondas de Radio**    | 3 kHz - 300 GHz      | GPS, UWB, redes celulares                    | Largo alcance en exteriores                | Bloqueadores de señal              |
| **Ondas Milimétricas**| 30 GHz - 300 GHz     | Escaneo corporal, sensores de vehículos      | Alta resolución, alcance limitado          | Alta absorción atmosférica         |

**Interpretación**

La tabla anterior resume las características clave de diferentes tecnologías basadas en ondas, destacando sus aplicaciones principales, condiciones de propagación ideales y limitaciones inherentes. Esta comparativa facilita la selección de la tecnología adecuada según las necesidades específicas de detección y seguimiento en diversos entornos.





### 1. Detección de Intrusos con Sensores de Ultrasonidos

- **Descripción**: Los sensores ultrasónicos operan emitiendo ondas de alta frecuencia (20 kHz - 100 kHz) que rebotan en los objetos cercanos. Al medir el tiempo de retorno, es posible detectar la presencia y movimiento de intrusos en áreas restringidas.
- **Aplicaciones**:
  - **Sistemas de seguridad perimetral**: Utilizados en almacenes, centros de datos y áreas de alta seguridad para detectar movimientos no autorizados.
  - **Vigilancia en interiores**: En combinación con sistemas de alarmas, los sensores ultrasónicos pueden generar alertas en tiempo real ante cualquier intrusión.
- **Ventajas**:
  - Funcionan en condiciones de baja visibilidad y en entornos donde las cámaras pueden ser menos efectivas, como espacios oscuros o con humo.
- **Limitaciones**:
  - **Interferencias ambientales**: La presencia de superficies porosas o condiciones climáticas adversas (p.ej., corrientes de aire) puede afectar la precisión de los sensores.
- **Contramedidas**:
  - Ajustes en la sensibilidad del sensor y filtros de ruido para minimizar falsas alarmas.
  - Combinación con otros sistemas, como cámaras infrarrojas o sensores PIR, para un sistema de detección más robusto.

### 2. Sensores Infrarrojos para la Detección de Dispositivos

- **Descripción**: Los sensores infrarrojos (300 GHz - 430 THz) detectan la radiación térmica emitida por los objetos, permitiendo la identificación de dispositivos electrónicos activos basándose en su firma de calor.
- **Aplicaciones**:
  - **Monitoreo perimetral** en instalaciones críticas como centros de datos y oficinas gubernamentales.
  - **Detección de dispositivos ocultos**: Identificación de equipos electrónicos encendidos que pueden estar siendo utilizados para espionaje.
- **Ventajas**:
  - Eficaces en condiciones de baja luz y en entornos donde la visibilidad es limitada (por ejemplo, humo o niebla).
- **Limitaciones**:
  - **Interferencias térmicas**: Fuentes de calor ambiental pueden generar falsos positivos.
- **Contramedidas**:
  - Uso de algoritmos de reconocimiento térmico y análisis de patrones para filtrar fuentes de calor no relacionadas con amenazas.

---

### 3. Rastreo y Geolocalización con Ondas de Radio

Las ondas de radio (3 kHz - 300 GHz) son esenciales para sistemas de comunicación y rastreo en tiempo real. Estas ondas permiten tanto la **detección pasiva** de dispositivos como la **geolocalización activa** mediante triangulación de señales.

#### 3.1. Triangulación y Geolocalización GSM

- **Descripción**: La triangulación GSM utiliza la intensidad de las señales recibidas desde múltiples torres de telefonía para localizar un dispositivo. Esta técnica es utilizada por agencias de seguridad para rastrear a sospechosos y para aplicaciones de geofencing.
- **Aplicaciones en ciberseguridad**:
  - **Monitoreo de dispositivos móviles**: Rastrear la ubicación de teléfonos vinculados a actividades sospechosas.
  - **Investigaciones forenses**: Determinar la trayectoria histórica de un dispositivo para establecer un perfil de comportamiento.
  - **Geofencing**: Definir perímetros virtuales que activan alertas si un dispositivo entra o sale de un área designada.
- **Técnicas de ataque**:
  - **IMSI Catchers (Stingrays)**: Dispositivos que se hacen pasar por torres legítimas para interceptar comunicaciones y rastrear dispositivos móviles.
  - **GSM Spoofing**: Emulación de torres para redirigir y capturar comunicaciones.
- **Contramedidas**:
  - **Cifrado avanzado**: Implementación de **A5/3** en lugar de los obsoletos **A5/1** y **A5/2**.
  - **Monitoreo con SDR (Software Defined Radio)**: Detección de IMSI Catchers mediante el análisis de patrones anómalos en las comunicaciones.
  - **Desconexión automática**: Configuración para evitar la conexión automática a torres desconocidas.

#### 3.2. Bluetooth Tracking

- **Descripción**: El protocolo Bluetooth permite la comunicación de corto alcance entre dispositivos, con un rango de hasta 100 metros (Bluetooth 5.0). Su uso en ciberseguridad permite la **detección de dispositivos no autorizados** en entornos corporativos.
- **Aplicaciones**:
  - **Control de acceso**: Monitoreo de la presencia de dispositivos en áreas restringidas, como oficinas y laboratorios.
  - **Análisis de comportamiento**: Seguimiento de patrones de movimiento de personas mediante el rastreo de sus dispositivos.
- **Técnicas de ataque**:
  - **Bluejacking y Bluesnarfing**:
    - **Bluejacking**: Envío de mensajes no solicitados a dispositivos cercanos.
    - **Bluesnarfing**: Acceso no autorizado a datos en un dispositivo mediante vulnerabilidades del protocolo.
  - **Bluetooth Beacon Tracking**: Uso de beacons para rastrear la ubicación de dispositivos sin el conocimiento del usuario.
- **Contramedidas**:
  - **Cifrado fuerte**: Implementación de autenticación avanzada para prevenir ataques de suplantación.
  - **Monitoreo activo**: Uso de **Bluetooth Sniffers** para detectar dispositivos sospechosos en la red.

---

### 4. Wi-Fi Sniffing y Detección de Intrusiones

La captura y análisis del tráfico Wi-Fi se ha convertido en una técnica común tanto en ciberseguridad defensiva como ofensiva. 

- **Descripción**: El **sniffing** de Wi-Fi implica la captura de paquetes de red para extraer información sensible. Esto es especialmente peligroso en redes que no están debidamente aseguradas.
- **Aplicaciones en ciberseguridad**:
  - **Monitoreo de redes**: Detección de dispositivos no autorizados en redes empresariales.
  - **Análisis forense**: Identificación de actividad sospechosa mediante el análisis del tráfico capturado.
- **Técnicas de ataque**:
  - **Packet Sniffing**: Uso de herramientas como **Wireshark** para capturar y analizar datos en redes sin cifrado robusto.
  - **Evil Twin Attack**: Creación de puntos de acceso falsos que imitan redes legítimas, permitiendo la interceptación de datos.
  - **Deauthentication Attacks**: Forzar la desconexión de dispositivos para redirigirlos a un punto de acceso controlado por el atacante.
- **Contramedidas**:
  - **Uso de WPA3**: Implementación de cifrado avanzado para proteger redes Wi-Fi.
  - **VPN**: Protección adicional del tráfico de red, especialmente en entornos públicos.
  - **Sistemas IDS**: Implementación de **Intrusion Detection Systems** (IDS) para identificar comportamientos anómalos en la red.

---

## Interferencias y Contraataques en Ciberseguridad

Las tecnologías basadas en ondas pueden ser **vulnerables a interferencias** intencionadas por parte de atacantes. A continuación, se describen las técnicas de **jamming**, **spoofing** y las estrategias defensivas para mitigarlas.

### 1. Jamming (Inhibición de Señales)

- **Descripción**: El jamming implica la emisión de ruido en la misma frecuencia que el dispositivo objetivo para bloquear su comunicación.
- **Aplicaciones en ataques**:
  - **Inhibidores de GSM**: Bloqueo de comunicaciones móviles en áreas sensibles.
  - **Desactivación de dispositivos IoT**: Mediante el uso de bloqueadores de Wi-Fi y Bluetooth.
- **Contramedidas**:
  - **Espectro ensanchado (Spread Spectrum)**: Técnicas como **Frequency Hopping** y **Chirp Modulation** para dificultar el jamming.
  - **Ultra-Wideband (UWB)**: Uso de bandas anchas que reducen la susceptibilidad a interferencias.

### 2. Spoofing y Replay Attacks

- **Descripción**: El spoofing se refiere a la emisión de señales falsas para engañar a un receptor, mientras que los **replay attacks** implican la repetición de señales capturadas previamente.
- **Ejemplos**:
  - **GPS Spoofing**: Desviación de la ubicación percibida por un receptor GPS.
  - **Bluetooth Replay Attacks**: Captura y reproducción de señales para obtener acceso no autorizado.
- **Contramedidas**:
  - **Autenticación multifactor**: Utilización de características físicas, como la huella RF, para la autenticación de dispositivos.
  - **Verificación criptográfica** de señales para prevenir la repetición de mensajes.

---

## Vectores de Ataque Basados en Ondas

Los ataques que explotan las ondas electromagnéticas son cada vez más sofisticados y representan un riesgo significativo para la ciberseguridad. Se dividen en tres categorías principales: **interferencia activa**, **repetición de señales** y **manipulación de señales**. A continuación, se detallan las técnicas más avanzadas y los ataques recientes que han cobrado relevancia.

---

### 2. Ataques Activos de Interferencia

Los ataques de interferencia activa buscan **perturbar, deshabilitar o desviar las comunicaciones inalámbricas**, con un enfoque en sistemas críticos, como redes industriales, infraestructuras de telecomunicaciones y dispositivos IoT.

#### 2.1. Jamming Avanzado

El jamming se utiliza para interrumpir la comunicación inalámbrica mediante la emisión de **señales de interferencia en las frecuencias objetivo**. 

- **Técnicas avanzadas de jamming**:
  - **Reactive Jamming**: Detecta actividad en una frecuencia específica antes de emitir interferencia. Este método ahorra energía y reduce la posibilidad de ser detectado, ya que solo actúa cuando se detecta actividad.
  - **Follow-on Jamming**: Se enfoca en un objetivo que utiliza **Frequency Hopping Spread Spectrum (FHSS)**. El atacante rastrea la frecuencia en la que opera el sistema y emite interferencia a medida que esta cambia.
  - **Swept Jamming**: Emite interferencia de forma continua y en ciclos a través de un **rango de frecuencias**, afectando múltiples canales simultáneamente.
  - **Deceptive Jamming**: El atacante emite señales que imitan las transmisiones originales para engañar a los dispositivos y causar confusión en la red.
  - **Inteligencia Artificial en Jamming**:
    - **Machine Learning (ML)** para optimizar ataques de jamming: Los modelos de ML pueden identificar los **canales más activos** y ajustar dinámicamente las frecuencias y potencias para maximizar el impacto y minimizar la detección.

- **Nuevas variantes**:
  - **Smart Jamming**: Utiliza **redes neuronales** para predecir patrones de comunicación y realizar ataques más eficientes, interrumpiendo solo en momentos críticos.
  - **Adaptive Jamming**: Ajusta la interferencia en función del **ancho de banda detectado** y la densidad del tráfico en tiempo real, optimizando el uso de recursos.

- **Contramedidas**:
  - **Spread Spectrum Techniques**: FHSS y **Direct Sequence Spread Spectrum (DSSS)** dispersan las señales en un amplio espectro, lo que dificulta su bloqueo.
  - **MIMO (Multiple Input, Multiple Output)**: Aumenta la robustez mediante el uso de múltiples antenas para minimizar la interferencia.
  - **Redes Mesh Autorreparables**: En sistemas IoT, las topologías mesh permiten el **rerouting automático** para evitar los nodos afectados.

---

### 2.2. Replay Attacks

Los ataques de repetición consisten en **capturar señales válidas y retransmitirlas** para engañar al sistema objetivo y realizar acciones no autorizadas.

- **Técnicas utilizadas**:
  - **Keyfob Cloning**: Captura y reproducción de las señales emitidas por controles remotos de automóviles, lo que permite desbloquear vehículos.
  - **Garage Door Opener Attacks**: Interceptación de las señales utilizadas para abrir puertas de garaje. Utiliza técnicas como **brute force** sobre los códigos emitidos.
  - **NFC y RFID Replay**: Almacenar y reproducir señales de tarjetas de pago o llaves electrónicas, permitiendo el acceso no autorizado a edificios o sistemas de pago.
  - **Signal Amplification Relay Attack (SARA)**: Utilizado para sistemas de **entrada sin llave** en vehículos. Amplifica la señal legítima del dispositivo para desbloquear el coche sin necesidad del control original cerca.

- **Contramedidas**:
  - **Challenge-Response Authentication**: Implementar un intercambio de desafíos y respuestas que incluya **nonces (números aleatorios)** para evitar la reutilización de señales.
  - **Cifrado Asimétrico**: Protección adicional mediante la autenticación mutua basada en cifrado.
  - **Temporal Tokens**: Uso de marcas temporales para invalidar las señales capturadas, haciendo que expiren rápidamente.

---

### 3. Manipulación de Señales

La manipulación activa de señales tiene como objetivo **alterar la información transmitida**, comprometiendo la integridad y la fiabilidad de los sistemas que dependen de estas señales.

#### 3.1. Signal Spoofing Avanzado

El spoofing consiste en la suplantación de **señales legítimas** para engañar al receptor. Esto es especialmente peligroso en aplicaciones que dependen de la precisión de la señal, como la navegación y los sistemas de control industrial.

- **Técnicas avanzadas**:
  - **GPS/GNSS Spoofing**:
    - **Meaconing**: Captura y retransmisión de señales GPS auténticas para desviar la ubicación percibida por el receptor.
    - **Trajectory Spoofing**: Manipulación de la trayectoria para confundir a sistemas autónomos, como drones o vehículos autónomos.
    - **GPS Time Spoofing**: Alteración de señales de tiempo para interrumpir sistemas financieros y de telecomunicaciones que dependen de una sincronización precisa.
  - **Bluetooth Spoofing**:
    - **MAC Address Spoofing**: Falsificación de la dirección MAC para suplantar dispositivos y obtener acceso a redes o interceptar comunicaciones.
    - **Bluetooth Beacon Spoofing**: Utilizado para redirigir a usuarios a páginas maliciosas o rastrear su ubicación en interiores.

- **Ataques basados en SDR (Software Defined Radio)**:
  - **Emulación de Estaciones Base (Fake BTS)**: Crear torres celulares falsas para interceptar comunicaciones móviles. Utilizado por dispositivos como **IMSI Catchers (Stingrays)**.
  - **IoT Signal Spoofing**: Suplantación de señales para engañar a dispositivos IoT, como sistemas de seguridad y sensores industriales.
  - **ADS-B Spoofing**: Ataques contra sistemas de aviación, alterando la información de la ubicación de aeronaves.

- **Contramedidas**:
  - **Autenticación Física Basada en RF Fingerprinting**: Utilizar características únicas de la señal, como la distorsión introducida por el hardware, para verificar la autenticidad.
  - **Análisis de Espectro en Tiempo Real**: Uso de sistemas basados en **ML** y **SDR** para detectar patrones inusuales en las transmisiones.
  - **Señales Resilientes al Spoofing (Anti-Spoofing Signals)**: Implementación de **códigos cifrados y autenticación multilayer** para garantizar la integridad de la señal.

#### 3.2. Protocol-Specific Exploits

Algunos ataques se centran en explotar vulnerabilidades específicas en los protocolos de comunicación.

- **Bluetooth Attacks**:
  - **KNOB Attack (Key Negotiation of Bluetooth)**: Reducir la entropía durante la negociación de la clave, lo que permite ataques de fuerza bruta.
  - **BlueBorne**: Permite la ejecución de código remoto al explotar vulnerabilidades en el protocolo Bluetooth.
  - **BIAS (Bluetooth Impersonation Attacks)**: Suplantación de dispositivos emparejados mediante la reutilización de claves.
- **Wi-Fi Attacks**:
  - **Kr00k**: Fuerza la desconexión y captura de datos sin cifrar al reiniciar la clave de cifrado.
  - **FragAttacks**: Manipulación de fragmentos de paquetes para comprometer la seguridad de redes Wi-Fi.
  - **Evil Twin**: Creación de puntos de acceso falsos que imitan redes legítimas, permitiendo la interceptación de tráfico y el robo de credenciales.

- **Contramedidas**:
  - **Wi-Fi Protected Access 3 (WPA3)**: Mejora la seguridad de las redes inalámbricas al introducir **Simultaneous Authentication of Equals (SAE)**.
  - **Bluetooth Security Updates**: Implementación de parches y mejoras en el protocolo para prevenir ataques conocidos.
  - **IDS/IPS Basados en ML**: Uso de **sistemas de detección de intrusiones** que emplean algoritmos de aprendizaje automático para identificar patrones de ataque en tiempo real.
  

## Mitigación y Contramedidas Avanzadas

A medida que las técnicas de ataque basadas en ondas se vuelven más sofisticadas, las contramedidas también deben evolucionar. Esta sección explora estrategias defensivas que aprovechan el procesamiento de señales, la inteligencia artificial y tecnologías avanzadas para mitigar ataques.

### 1. Procesamiento Defensivo de Señales

#### 1.1. Signal Hardening

- **Técnicas de espectro ensanchado**:
  - **Frequency Hopping** y **Chirp Modulation** para dificultar la detección y bloqueo.
  - **Orthogonal Frequency Division Multiplexing (OFDM)**: Minimización de interferencias entre señales cercanas.
- **Aplicaciones**:
  - **Redes Wi-Fi y Bluetooth seguras**.
  - **Sistemas críticos militares y gubernamentales**.

#### 1.2. Adaptive Countermeasures

- **Dynamic Frequency Allocation**: Ajuste de frecuencias en respuesta a ataques de jamming.
- **Beamforming**: Concentración de señales hacia el receptor para reducir la interceptación.
- **Null Steering**: Creación de "zonas nulas" en el patrón de radiación para bloquear interferencias.

---

### 2. Machine Learning en la Detección de Amenazas

El uso de **machine learning** mejora la detección y respuesta a ataques en tiempo real.

#### 2.1. Análisis Predictivo de Espectro

- **Detección de patrones anómalos** mediante **CNN y modelos de detección de anomalías**.
- **Redes Generativas Adversariales (GANs)** para simular ataques y entrenar modelos de defensa.

#### 2.2. Aprendizaje por Refuerzo

- **Deep Reinforcement Learning** para ajustar la respuesta defensiva en entornos cambiantes.
- **Series temporales** para prever ataques basados en patrones históricos.
        - fundamentos/docs/Nuevos Ataques.md/:
            - content: # Ataques Recientes


### 1. **GhostTelephonist Attack**

- **Descripción**: Este ataque se centra en la **suplantación de estaciones base GSM/UMTS (2G/3G)**. Aprovecha las debilidades en la autenticación unidireccional de los dispositivos móviles para secuestrar llamadas y mensajes SMS sin que el usuario sea consciente.
- **Funcionamiento**:
  - El atacante despliega una **falsa estación base (Fake BTS)** que se hace pasar por una torre celular legítima.
  - El teléfono móvil de la víctima se conecta automáticamente a la estación más cercana con la mejor señal, permitiendo al atacante interceptar llamadas y mensajes en tiempo real.
  - Utilizando técnicas de **Man-in-the-Middle (MITM)**, el atacante puede redirigir las llamadas o inyectar mensajes falsos.
- **Potencial del ataque**:
  - **Dificultad para mitigar**: Las redes 2G/3G aún son ampliamente utilizadas, especialmente en zonas rurales y en sistemas IoT. Estas redes no implementan autenticación mutua, lo que las hace vulnerables.
  - **Detección compleja**: Los dispositivos móviles no suelen notificar al usuario cuando cambian de torre, lo que permite al atacante permanecer invisible.
- **Contramedidas**: Aunque los sistemas modernos utilizan 4G/5G, que requieren autenticación mutua, la migración completa de todos los dispositivos llevará tiempo. El uso de **SDR (Software Defined Radio)** para detectar estaciones base falsas es una solución emergente, pero aún no se ha implementado de manera amplia.

---

### 2. **Jamming Selectivo de Sistemas GPS: TimeJacker**

- **Descripción**: Este ataque explota la dependencia de los sistemas críticos (como infraestructuras de telecomunicaciones y financieras) en las señales de **GPS para la sincronización precisa del tiempo**.
- **Funcionamiento**:
  - Un atacante emite señales de interferencia **selectiva** dirigidas únicamente a los canales GPS que transmiten la información de tiempo.
  - Utilizando técnicas de **jamming direccional**, el ataque interfiere solo en los datos de temporización sin afectar la posición, lo que dificulta su detección.
  - Esto provoca desincronización en los sistemas que dependen del GPS, lo que puede resultar en **fallos en transacciones financieras, interrupciones en telecomunicaciones y redes eléctricas**.
- **Potencial del ataque**:
  - **Difícil de detectar**: Dado que no afecta la señal de posicionamiento, los sistemas no detectan una pérdida de señal obvia, sino solo un **desajuste temporal**.
  - **Alto impacto**: La dependencia global de los sistemas críticos en la sincronización por GPS significa que un ataque de este tipo puede tener consecuencias económicas y de infraestructura devastadoras.
- **Contramedidas**: El uso de **sistemas redundantes de temporización** basados en relojes atómicos o satélites alternativos puede mitigar parcialmente el problema, pero la implementación generalizada de estas soluciones llevará años.

---

### 3. **Wi-Fi Frag Attacks (Fragmentation and Aggregation Attacks)**

- **Descripción**: Los **Frag Attacks** son un conjunto de vulnerabilidades que afectan la fragmentación y la reensamblación de paquetes en redes Wi-Fi. Descubiertos en 2021, estos ataques permiten la **inyección de paquetes maliciosos** y la exfiltración de datos en redes Wi-Fi protegidas por WPA2 y WPA3.
- **Funcionamiento**:
  - El atacante aprovecha fallos en la forma en que los dispositivos manejan los **fragmentos de paquetes y las tramas agregadas**.
  - Mediante la inyección de paquetes cuidadosamente manipulados, un atacante puede engañar al dispositivo para que **reemplace fragmentos válidos** con datos maliciosos.
  - Incluso las redes Wi-Fi con WPA3 pueden ser vulnerables si los dispositivos no aplican correctamente los parches de seguridad.
- **Potencial del ataque**:
  - **Amplia superficie de ataque**: Casi todos los dispositivos que utilizan Wi-Fi, incluidos routers, teléfonos inteligentes, y dispositivos IoT, son vulnerables.
  - **Difícil de mitigar**: Aunque se han lanzado parches, la adopción en todos los dispositivos es lenta, especialmente en entornos industriales y dispositivos embebidos.
- **Contramedidas**: Se requieren **parches de firmware** específicos para cada dispositivo afectado, pero muchos routers y dispositivos IoT antiguos no recibirán actualizaciones, lo que deja una gran cantidad de dispositivos expuestos.

---

### 4. **BLURtooth Attack**

- **Descripción**: Esta vulnerabilidad afecta a dispositivos **Bluetooth 4.2 y 5.0** que soportan la tecnología **Dual Mode**. Permite a un atacante realizar **ataques de escalamiento de privilegios y suplantación** de dispositivos emparejados.
- **Funcionamiento**:
  - El ataque explota el proceso de **Cross-Transport Key Derivation (CTKD)**, que gestiona las claves de emparejamiento entre Bluetooth Low Energy (BLE) y Classic Bluetooth.
  - Un atacante puede aprovechar esta debilidad para **anular la autenticación previa** entre dos dispositivos emparejados y, de esta forma, interceptar comunicaciones o realizar **ataques de Man-in-the-Middle**.
- **Potencial del ataque**:
  - **Dispositivos vulnerables**: La mayoría de los dispositivos modernos que soportan Bluetooth Dual Mode son vulnerables, incluyendo teléfonos inteligentes, portátiles y sistemas de infotainment en vehículos.
  - **Alto impacto**: Permite acceder a datos sensibles y control de dispositivos cercanos, especialmente en entornos corporativos y domésticos.
- **Contramedidas**: El estándar **Bluetooth 5.1** incluye mejoras que mitigan esta vulnerabilidad, pero el despliegue completo de dispositivos actualizados llevará tiempo.

---

### 5. **Laser Injection Attack**

- **Descripción**: Esta técnica utiliza **pulsos de láser** para inyectar comandos en dispositivos electrónicos, como **asistentes de voz** y sistemas de control basados en micrófonos.
- **Funcionamiento**:
  - El atacante apunta un **láser modulado** hacia el micrófono del dispositivo desde una distancia considerable (hasta 100 metros).
  - Los pulsos de láser imitan las vibraciones que un sonido real produciría en el micrófono, engañando al dispositivo para que **ejecute comandos de voz** no autorizados.
  - Esto permite al atacante controlar dispositivos inteligentes, desbloquear puertas, realizar compras, e incluso manipular sistemas de seguridad.
- **Potencial del ataque**:
  - **Difícil de detectar**: Dado que el láser es invisible y no emite sonido, los usuarios y los dispositivos no tienen forma de detectar el ataque.
  - **Superficie de ataque amplia**: Afecta a cualquier dispositivo con un asistente de voz o un sistema basado en micrófonos (Alexa, Google Home, cámaras de seguridad, etc.).
- **Contramedidas**: Proteger físicamente los micrófonos o rediseñar el hardware para **detectar las anomalías en las vibraciones** podría mitigar estos ataques, pero su implementación es costosa y no será adoptada a corto plazo.

---

### 6. **Adversarial Machine Learning (AML) en Sistemas de Reconocimiento de Voz e Imágenes**

- **Descripción**: Los ataques de **adversarial machine learning** se enfocan en **manipular modelos de IA** para que tomen decisiones incorrectas mediante la introducción de perturbaciones invisibles a los ojos humanos.
- **Funcionamiento**:
  - Un atacante entrena un modelo para generar **ruido adversarial** que, cuando se superpone a una imagen o una grabación de audio, causa que los modelos de IA cometan errores significativos.
  - Estos ataques pueden engañar a sistemas de reconocimiento facial, de voz o de objetos para que **autoricen accesos no permitidos** o clasifiquen incorrectamente objetos y personas.
- **Potencial del ataque**:
  - **Difícil de mitigar**: Los modelos de IA actuales son vulnerables a perturbaciones mínimas que no pueden ser percibidas por humanos.
  - **Superficie de ataque en expansión**: A medida que más sistemas críticos adoptan IA, la exposición a este tipo de ataques aumentará.
- **Contramedidas**: Requiere la **reentrenamiento de modelos** utilizando técnicas de robustez adversarial, lo que es costoso y difícil de aplicar a modelos ya desplegados.
