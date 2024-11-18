### 1. Introducción a la seguridad en Wi-Fi
- **Visión general de los estándares Wi-Fi**: IEEE 802.11a/b/g/n/ac/ax.
- **Arquitectura de la red Wi-Fi**: Capas de protocolo, desde la capa física hasta las aplicaciones.
- **Tipos de autenticación y cifrado**: WEP, WPA, WPA2, WPA3.
- **Superficie de ataque de redes Wi-Fi**: Resumen de las áreas vulnerables en la pila de protocolos y en la capa física.

---

### 2. Vectores de ataque en Wi-Fi
#### 2.1 A nivel físico (señales/ondas)
- **Intercepción de señales (eavesdropping)**:
  - Captura de tráfico utilizando radios SDR (Software Defined Radio) y herramientas como Wireshark.
  - Análisis del espectro de frecuencia y canales Wi-Fi (2.4 GHz y 5 GHz).
- **Interferencia de señales (jamming)**:
  - Ataques de denegación de servicio (DoS) mediante saturación de canales.
  - Técnicas de flooding para interrumpir la comunicación entre dispositivos.
- **Inyección de señales**:
  - Spoofing para falsificar puntos de acceso (APs).
  - Manipulación de tramas para desestabilizar la red.

#### 2.2 A nivel de protocolo
- **Ataques a la capa MAC**:
  - Deauth Attack: Envío de tramas de desautenticación.
  - Ataques de suplantación de dirección MAC.
- **Ataques a la autenticación y asociación**:
  - Rogue Access Point (Rogue AP) y Evil Twin.
  - Explotación de la falta de cifrado en redes abiertas.
- **Ataques a la capa de red**:
  - ARP Spoofing y ataques de envenenamiento de caché DNS.
  - Intercepción de paquetes (MITM) y sniffing de tráfico.

---

### 3. Vulnerabilidades en Wi-Fi
#### 3.1 Cifrado y autenticación
- **Debilidades en WEP**:
  - Criptoanálisis y ataques de reensamblaje de paquetes.
  - Ataques por diccionario para recuperar la clave WEP.
- **Fallas en WPA/WPA2**:
  - Ataques al protocolo de autenticación de 4 vías (4-Way Handshake).
  - Explotación de PSK (Pre-Shared Keys) débiles.
  - Vulnerabilidad KRACK (Key Reinstallation Attack) en WPA2.
- **Debilidades en WPA3**:
  - Ataques de fuerza bruta en redes con Dragonfly handshake.
  - Fallos en la implementación de SAE (Simultaneous Authentication of Equals).

#### 3.2 Autorización y control de acceso
- **Redes abiertas sin cifrado**:
  - Captura de credenciales mediante ataques de sniffing.
- **Ataques a WPS (Wi-Fi Protected Setup)**:
  - Fuerza bruta del PIN WPS para obtener la clave de la red.
  - Vulnerabilidades en el protocolo WPS-PBC (Push Button Configuration).

#### 3.3 Privacidad y rastreo
- **Fingerprinting y rastreo de dispositivos**:
  - Identificación de dispositivos mediante direcciones MAC.
  - Explotación de solicitudes de probe para rastrear la ubicación.
- **Ataques de geolocalización**:
  - Uso de triangulación y señales de Wi-Fi para rastrear la posición de un dispositivo.

---

### 4. Técnicas y ataques conocidos
#### 4.1 Ataques a nivel físico
- **Wi-Fi Jamming**: Saturación de canales para interrumpir la conectividad.
- **Deauth Attack**: Desconexión forzada de dispositivos mediante tramas de desautenticación.
- **Packet Injection**: Inyección de paquetes para manipular el tráfico.
  
#### 4.2 Ataques a nivel de protocolo
- **Evil Twin Attack**: Creación de un punto de acceso malicioso que imita una red legítima.
- **KRACK (Key Reinstallation Attack)**: Explotación del protocolo WPA2 para reiniciar la clave de cifrado.
- **PMKID Attack**: Recuperación de la clave WPA2/WPA3 utilizando PMKID en lugar del 4-Way Handshake.
- **ARP Spoofing**: Redirección de tráfico mediante la falsificación de respuestas ARP.
- **DNS Spoofing**: Manipulación de las respuestas DNS para redirigir a sitios falsos.

---

### 5. Metodología de explotación
#### 5.1 Reconocimiento
- **Identificación de redes Wi-Fi y dispositivos**:
  - Uso de herramientas como `airodump-ng`, `kismet` y `Wireshark`.
  - Análisis de tráfico con radios SDR para capturar paquetes y señales.
- **Escaneo de vulnerabilidades**:
  - Utilización de herramientas como `aircrack-ng`, `reaver`, y `wifite`.
  - Identificación de puntos de acceso vulnerables y redes con cifrado débil.

#### 5.2 Explotación
- **Técnicas de MITM (Man-In-The-Middle)**:
  - Uso de Bettercap y Ettercap para interceptar tráfico.
  - Ataques de sniffing y exfiltración de datos sensibles.
- **Ataques de fuerza bruta y cracking de claves**:
  - Ataques de diccionario para WPA/WPA2 con `hashcat` y `john the ripper`.
  - Cracking de claves WEP y WPA con `aircrack-ng`.
- **Ataques DoS y jamming**:
  - Implementación de ataques de jamming con `mdk3` y `aireplay-ng`.

#### 5.3 Post-explotación
- **Exfiltración de datos y acceso remoto**:
  - Robo de credenciales mediante sniffing de tráfico HTTPS.
  - Manipulación de configuraciones de routers comprometidos.
- **Persistencia y control de la red**:
  - Creación de backdoors en dispositivos IoT conectados.
- **Rastreo y geolocalización**:
  - Uso de direcciones MAC y análisis de señales para rastrear usuarios.

---

### 6. Contramedidas y defensa
#### 6.1 A nivel de red
- **Fortalecimiento de la autenticación**: Uso de WPA3 y eliminación de WEP.
- **Implementación de VLANs y segmentación de la red** para aislar dispositivos críticos.
- **Monitoreo y detección de intrusos (IDS)**:
  - Uso de sistemas como Snort, Suricata y Zeek.
  - Detección de anomalías en el tráfico de red y dispositivos conectados.

#### 6.2 A nivel de dispositivo
- **Configuración segura de routers y APs**:
  - Desactivar WPS y habilitar WPA3.
  - Uso de listas de control de acceso (ACLs).
- **Actualización de firmware**:
  - Aplicación de parches para vulnerabilidades conocidas como KRACK.
- **Privacidad del usuario**:
  - Utilización de direcciones MAC aleatorias para evitar el rastreo.
  - Deshabilitar el auto-conexión a redes públicas.

---

### 7. Herramientas y recursos recomendados
- **Hardware**: SDR (HackRF, BladeRF, USRP), tarjetas Wi-Fi compatibles con `aircrack-ng`.
- **Software y herramientas**: Kali Linux, Wireshark, Aircrack-ng, Bettercap, Reaver.
- **Entornos de laboratorio**: VirtualBox, Docker, Raspberry Pi.

---

### 8. Conclusión
- Resumen de los principales vectores de ataque y técnicas de defensa.
- Importancia de la actualización y configuración segura para mitigar riesgos.
- Recomendaciones para futuras investigaciones en seguridad de redes Wi-Fi.
