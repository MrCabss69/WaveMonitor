# Introducción a la seguridad en dispositivos IoT
- **Definición de IoT (Internet of Things)**:
  - Dispositivos conectados que recopilan, procesan y transmiten datos a través de redes.
  - Ejemplos: cámaras de seguridad, sensores industriales, wearables, dispositivos domésticos inteligentes, vehículos autónomos, etc.
- **Arquitectura típica de un sistema IoT**:
  - **Capa de dispositivos (sensing layer)**: Sensores y actuadores.
  - **Capa de red (network layer)**: Protocolos de comunicación como MQTT, CoAP, HTTP, Bluetooth, Wi-Fi, Zigbee.
  - **Capa de procesamiento (edge computing y cloud layer)**: Servidores y sistemas de análisis en la nube.
  - **Capa de aplicación (application layer)**: Aplicaciones y plataformas que interactúan con los usuarios.
- **Superficie de ataque en IoT**:
  - Dispositivos de bajo costo y baja potencia con limitaciones de seguridad.
  - Vulnerabilidades en firmware, hardware, y protocolos de comunicación.
  - Integración en entornos críticos como infraestructuras industriales y de salud.

---

## Vectores de ataque en IoT
#### A nivel físico (hardware y señales)
- **Extracción de datos del hardware (Side-Channel Attacks)**:
  - **Análisis de potencia (Power Analysis)**: Detección de patrones de consumo eléctrico para inferir datos sensibles.
  - **Análisis de emisiones electromagnéticas (Electromagnetic Analysis)**: Captura de emisiones para descifrar claves o datos.
  - **Ataques de manipulación física**: Desmontaje de dispositivos para extraer información de memoria EEPROM, Flash o chips.
  - **Cold Boot Attack**: Extracción de claves y datos desde la memoria volátil cuando el dispositivo se reinicia.
  
- **Interferencia y manipulación de señales**:
  - **Jamming**: Interferencia en las comunicaciones inalámbricas (Wi-Fi, Zigbee, Bluetooth).
  - **Signal Injection**: Inyección de señales para desestabilizar sensores y actuadores.
  - **Replay Attacks**: Captura y reutilización de señales inalámbricas para reproducir comandos.

#### A nivel de red (protocolos y comunicación)
- **Intercepción de tráfico (eavesdropping)**:
  - Captura de paquetes en redes Wi-Fi, Zigbee, y Bluetooth con herramientas como Wireshark y radios SDR.
  - **ARP Spoofing y ataques MITM (Man-in-the-Middle)** para interceptar y manipular tráfico IoT.

- **Ataques DoS (Denegación de Servicio)**:
  - **Inundación de paquetes (Packet Flooding)** para agotar los recursos del dispositivo.
  - **DDoS (Distributed Denial of Service)**: Uso de botnets de dispositivos IoT para sobrecargar servidores.

- **Secuestro de comunicaciones (session hijacking)**:
  - Explotación de sesiones no cifradas o con cifrado débil para tomar el control de dispositivos.

---

### Vulnerabilidades en dispositivos IoT
#### Hardware
- **Firmware desactualizado o sin parches**:
  - Uso de firmware con vulnerabilidades conocidas debido a la falta de actualizaciones automáticas.
- **Backdoors preinstalados**:
  - Puertas traseras introducidas por fabricantes para diagnóstico que pueden ser explotadas por atacantes.
- **Exposición de interfaces de depuración**:
  - **JTAG y UART**: Acceso directo a la memoria y control del dispositivo.

#### Red y protocolos de comunicación
- **Protocolos inseguros**:
  - Uso de protocolos como MQTT y HTTP sin cifrado (sin TLS/SSL).
  - Falta de autenticación en protocolos como CoAP, modbus, o Zigbee.
- **Explotación de contraseñas débiles o por defecto**:
  - Uso de credenciales predeterminadas, facilitando ataques de fuerza bruta.
- **Vulnerabilidades en la autenticación**:
  - **Broken Authentication**: Implementaciones débiles que permiten eludir la autenticación.
  - **Replay Attacks**: Falta de tokens de sesión seguros permite reutilización de credenciales.

#### Aplicaciones y servicios
- **Inyección de comandos**:
  - **Command Injection**: Inyecciones de comandos a través de interfaces web o APIs expuestas.
  - **Inyección SQL y NoSQL**: Explotación de entradas no validadas en bases de datos.
- **Deserialización insegura**:
  - Explotación de procesos de deserialización que permiten la ejecución remota de código.
  
---

### Técnicas y ataques conocidos en IoT

#### Ataques a nivel físico
- **Side-Channel Attacks**:
  - Análisis de criptochips mediante análisis de potencia.
  - Ataques de temporización para extraer claves de cifrado.
- **Cold Boot Attack**:
  - Uso en dispositivos IoT para extraer claves en sistemas críticos.
- **Fault Injection**:
  - Inducción de fallos en microcontroladores para obtener acceso no autorizado.

#### Ataques a nivel de red y protocolo
- **Mirai Botnet**:
  - Uso de dispositivos IoT comprometidos para lanzar ataques DDoS masivos.
- **BrickerBot**:
  - Malware que "ladrilliza" dispositivos IoT explotando contraseñas débiles y vulnerabilidades de red.
- **IoTroop/Reaper**:
  - Botnet avanzada que explota vulnerabilidades en cámaras y routers IoT.
- **BLESA (Bluetooth Low Energy Spoofing Attack)**:
  - Manipulación de la re-autenticación de dispositivos BLE para interceptar y manipular comunicaciones.

#### Explotaciones en entornos industriales (IIoT)
- **TRITON (Trisis)**:
  - Ataque dirigido a sistemas de seguridad en plantas industriales.
- **Stuxnet**:
  - Ataque a sistemas SCADA mediante explotación de vulnerabilidades en controladores PLC.

---

### Metodología de ataque a dispositivos IoT
#### Reconocimiento y escaneo
- **Enumeración de dispositivos**:
  - Uso de herramientas como `nmap`, `shodan` y `zoomeye` para descubrir dispositivos expuestos.
- **Escaneo de puertos y servicios**:
  - Identificación de servicios expuestos mediante `masscan` y `amap`.
- **Recolección de información**:
  - Captura de tráfico con `Wireshark`, radios SDR y herramientas como `bettercap`.

#### Explotación de vulnerabilidades
- **Ataques MITM**:
  - Uso de `bettercap` para interceptar y manipular tráfico en redes IoT.
- **Ataques a APIs expuestas**:
  - Pruebas de inyección con `sqlmap`, `burpsuite` y `zap`.
- **Explotación de firmware**:
  - Análisis estático y dinámico con `binwalk`, `firmadyne` y `ghidra`.
- **Buffer Overflow y explotación en sistemas embebidos**:
  - Técnicas de explotación usando `pwntools` y `radare2`.

#### Post-explotación
- **Persistencia en dispositivos**:
  - Instalación de rootkits para mantener acceso continuo.
- **Exfiltración de datos**:
  - Uso de `netcat` y `scp` para transferir datos desde dispositivos comprometidos.
- **Control remoto y monitorización**:
  - Control de dispositivos IoT comprometidos mediante `Metasploit`.

---

### Contramedidas y defensa en entornos IoT
#### A nivel de dispositivo
- **Hardening de firmware**:
  - Actualizaciones regulares y uso de firmware firmado.
- **Desactivación de interfaces no utilizadas**: UART, JTAG y Telnet.
- **Implementación de autenticación multifactor (MFA)**.

#### A nivel de red
- **Segmentación de la red**:
  - Uso de VLANs y firewalls para aislar dispositivos IoT.
- **Monitoreo y detección de intrusos**:
  - Implementación de IDS/IPS para detectar actividades anómalas.
  
#### A nivel de protocolo
- **Uso de cifrado TLS/SSL en todas las comunicaciones**.
- **Autenticación basada en certificados y tokens**.
- **Implementación de prácticas de desarrollo seguro (SDLC)**.

---

### Herramientas y recursos recomendados
- **Hardware**: Radios SDR (HackRF, BladeRF), adaptadores Wi-Fi y Zigbee.
- **Software y herramientas**: Wireshark, Metasploit, Burp Suite, Bettercap, Ghidra.
- **Entornos de laboratorio**: Kali Linux, Docker para entornos aislados, y plataformas como IoT-LAB y ThingSpeak para pruebas.

---

### Conclusión
- **Resumen de los vectores de ataque y técnicas de defensa más importantes**.
- **Recomendaciones para mejorar la seguridad en entornos IoT críticos**.
        - IoT/docs/Weaponizing.md/:
            - content: ## **Capítulo: Weaponización de Dispositivos y Conexiones IoT**

### 1. **Introducción a la weaponización de IoT**
- **Concepto de weaponización**:
  - Transformar dispositivos IoT legítimos en herramientas para llevar a cabo ataques cibernéticos.
  - Dispositivos comprometidos se utilizan para denegación de servicio, espionaje, exfiltración de datos y control remoto.
- **Contexto**:
  - La creciente adopción de IoT en entornos industriales, domésticos y de infraestructuras críticas aumenta la superficie de ataque.
  - Muchos dispositivos IoT tienen vulnerabilidades debido a la falta de actualizaciones y medidas de seguridad, convirtiéndose en objetivos fáciles para los atacantes.

---

### 2. **Técnicas de weaponización de dispositivos IoT**
#### 2.1 **Explotación de dispositivos vulnerables**
- **Backdoors preinstalados**:
  - Algunos dispositivos IoT vienen con puertas traseras dejadas por los fabricantes para mantenimiento, las cuales pueden ser explotadas por atacantes.
- **Firmware desactualizado**:
  - Uso de vulnerabilidades conocidas en versiones antiguas de firmware para obtener acceso no autorizado.
- **Manipulación de interfaces de administración**:
  - Explotación de paneles de administración web y APIs para tomar control del dispositivo.

#### 2.2 **Instalación de malware y rootkits**
- **Inyección de código malicioso**:
  - Uso de exploits como buffer overflow y command injection para inyectar malware.
  - Despliegue de rootkits en dispositivos comprometidos para mantener el control persistente.
- **Uso de troyanos específicos para IoT**:
  - **Mirai Botnet**: Uso de contraseñas por defecto para comprometer dispositivos y utilizarlos en ataques DDoS.
  - **Gafgyt y Qbot**: Malware orientado a enrutadores y cámaras IP que explota vulnerabilidades en servicios como Telnet.

#### 2.3 **Persistencia y control remoto**
- **Instalación de puertas traseras**:
  - Creación de túneles seguros (SSH reverse shell) para acceder a dispositivos IoT desde redes externas.
  - Uso de conexiones VPN para ocultar la comunicación con dispositivos comprometidos.
- **Técnicas de ofuscación**:
  - Uso de cifrado y ofuscación para ocultar el malware en el firmware del dispositivo.
  - Empaquetado de malware para que parezca tráfico legítimo.

---

### 3. **Vectores de ataque utilizados en la weaponización de IoT**
#### 3.1 **Redes de botnets IoT**
- **Concepto de botnet**:
  - Red de dispositivos IoT comprometidos que los atacantes pueden controlar de forma remota.
  - Utilizadas para ataques de DDoS, minería de criptomonedas y ataques de fuerza bruta.
- **Ejemplos de botnets conocidas**:
  - **Mirai**: Comprometió millones de dispositivos usando credenciales por defecto.
  - **Mozi**: Botnet peer-to-peer que persiste incluso después de reinicios.
  - **Dark Nexus**: Botnet avanzada que utiliza técnicas de evasión para evitar la detección.

#### 3.2 **Explotación de conexiones inalámbricas y protocolos**
- **Bluetooth Low Energy (BLE)**:
  - **BLESA (BLE Spoofing Attack)**: Manipulación de sesiones autenticadas para interceptar tráfico.
  - Ataques de eavesdropping y jamming en dispositivos IoT conectados por BLE.
- **Wi-Fi y Zigbee**:
  - Ataques de deautenticación para desconectar dispositivos y forzar la reconexión a redes controladas por el atacante.
  - **Explotación de Zigbee**: Uso de herramientas como Zigbee2MQTT para interceptar y manipular comandos de dispositivos domésticos.

---

### 4. **Enfoques y técnicas de weaponización**
#### 4.1 **Uso de dispositivos IoT como trampolines (pivoting)**
- **Infiltración en redes internas**:
  - Compromiso de dispositivos IoT conectados a redes corporativas para obtener acceso a servidores y sistemas sensibles.
- **Movimientos laterales (Lateral Movement)**:
  - Uso de dispositivos IoT comprometidos como puntos de entrada para explorar redes internas y propagar malware.
  
#### 4.2 **Ataques de denegación de servicio distribuidos (DDoS)**
- **Explotación de dispositivos IoT con bajo nivel de seguridad**:
  - Generación de tráfico masivo utilizando dispositivos comprometidos para saturar servidores y servicios.
- **Técnicas avanzadas**:
  - Uso de ataques DDoS reflejados mediante amplificación (e.g., DNS, NTP).
  - **HTTP Flooding**: Inundación de solicitudes HTTP utilizando dispositivos IoT para sobrecargar sitios web.

#### 4.3 **IoT como herramientas de espionaje y exfiltración**
- **Espionaje a través de cámaras y micrófonos**:
  - Compromiso de cámaras IP y altavoces inteligentes para obtener información sensible.
- **Captura de datos ambientales**:
  - Uso de sensores IoT (temperatura, movimiento, luz) para inferir actividades dentro de un entorno.
  
---

### 5. **Ataques conocidos basados en la weaponización de IoT**
#### 5.1 **Mirai Botnet**
- **Descripción**:
  - Botnet que aprovechó la falta de autenticación y contraseñas por defecto en millones de dispositivos IoT.
  - Causó un DDoS masivo que afectó a servicios como Dyn, interrumpiendo el acceso a sitios como Twitter y Reddit.
- **Técnicas utilizadas**:
  - Fuerza bruta de credenciales.
  - Detección de dispositivos vulnerables mediante escaneo masivo.

#### 5.2 **BrickerBot**
- **Descripción**:
  - Malware diseñado para "ladrillizar" dispositivos IoT, dejándolos inservibles.
  - Utiliza técnicas de manipulación de firmware y eliminación de particiones.
- **Objetivo**:
  - Destruir dispositivos comprometidos para impedir que sean utilizados en ataques futuros.

#### 5.3 **TRITON (TRISIS)**
- **Descripción**:
  - Ataque dirigido a sistemas de control industrial (ICS) mediante la weaponización de dispositivos IoT conectados.
  - Comprometió sistemas de seguridad para provocar fallos catastróficos en plantas industriales.
  
---

### 6. **Metodología para la weaponización y explotación de dispositivos IoT**
#### 6.1 **Reconocimiento y análisis**
- **Escaneo de dispositivos expuestos**:
  - Uso de plataformas como `Shodan` y `Censys` para identificar dispositivos vulnerables.
- **Fingerprinting de dispositivos**:
  - Identificación de dispositivos IoT y sus versiones de firmware utilizando `nmap` y `fingerprintdb`.

#### 6.2 **Explotación**
- **Uso de herramientas automatizadas**:
  - **Metasploit** y **bettercap** para comprometer dispositivos y obtener shells remotos.
- **Despliegue de payloads**:
  - Uso de `Mirai Source Code` para crear botnets personalizadas.
  - Inyección de malware mediante APIs y exploits conocidos.

#### 6.3 **Post-explotación y persistencia**
- **Mantenimiento de acceso**:
  - Instalación de rootkits y backdoors para garantizar el acceso remoto continuo.
- **Exfiltración de datos**:
  - Uso de `scp` y `rsync` para transferir datos sensibles.
- **Monitoreo de dispositivos comprometidos**:
  - Configuración de herramientas de control como **C2 (Command and Control)** para gestionar botnets.

---

### 7. **Contramedidas para mitigar la weaponización de IoT**
#### 7.1 **Fortalecimiento de dispositivos**
- **Implementación de autenticación fuerte**: Uso de MFA y certificados digitales.
- **Actualización periódica de firmware**: Implementación de parches y sistemas de actualización automática.
- **Desactivación de servicios no utilizados**: Cerrar puertos y deshabilitar interfaces como Telnet y SSH.

#### 7.2 **Defensa en red**
- **Segmentación de redes**: Uso de VLANs y firewalls para aislar dispositivos IoT.
- **Monitoreo en tiempo real**: Implementación de sistemas de detección de intrusos (IDS/IPS) específicos para IoT.
- **Uso de honeypots**: Atraer a los atacantes hacia entornos controlados para analizar sus tácticas.

---

### 8. **Conclusión**
- **Resumen de la weaponización y su impacto en la seguridad global**.
- **La importancia de la adopción de buenas prácticas y estándares de seguridad en IoT**.
- **Recomendaciones para fortalecer la ciberseguridad en entornos IoT a medida que estos dispositivos continúan expandiéndose**.
