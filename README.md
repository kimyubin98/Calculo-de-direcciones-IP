Calculadora de direcciones IP
# Cálculo de direcciones IP

Una pequeña utilidad en Python para calcular información de subredes y planificar VLSM (Variable Length Subnet Mask).

**Descripción**: Esta herramienta proporciona dos funcionalidades principales: calculadora de subredes (subnet calculator) y planificador VLSM. Está pensada para uso educativo y práctico en redes pequeñas.

**Archivos clave**:
- **Código:** [calculo_ip.py](calculo_ip.py)
- **Licencia:** [LICENSE](LICENSE)

**Características**:
- Calcula dirección de red, máscara, máscara wildcard, dirección broadcast, primeros/últimos hosts y número de hosts.
- Genera un plan VLSM según requisitos de hosts (ordena subredes por tamaño y asigna bloques apropiados).
- Interfaz interactiva de consola, sin dependencias externas (usa la librería estándar `ipaddress`).

**Requisitos**:
- Python 3.8+ (la librería `ipaddress` está incluida en la stdlib desde Python 3.3).

**Instalación**

Clona el repositorio o descarga los archivos y ejecuta el script con Python:

```bash
git clone <tu-repositorio>
cd "Calculo de direcciones IP"
python calculo_ip.py
```

**Uso (interactivo)**

Al ejecutar `python calculo_ip.py` verás un menú con opciones:

1) Subnet Calculator — pedirá una red como `192.168.1.0/24` y mostrará información sobre esa subred.

2) VLSM Planner — pedirá una red base (ej. `192.168.0.0/24`) y una lista de requisitos de hosts separados por comas (ej.: `100,50,10`). El programa ordenará los requisitos y asignará subredes adecuadas, mostrando máscara, prefijo, broadcast y rango usable.

3) Salir — termina la ejecución.

Ejemplo rápido:

```text
> Selecciona opción: 1
> Ingresa red (ejemplo 192.168.1.0/24): 192.168.1.0/24
	(muestra Network, Subnet Mask, Broadcast, First/Last Host, Total/Usable Hosts)
```

Y para VLSM:

```text
> Selecciona opción: 2
> Red base (ejemplo 192.168.0.0/24): 192.168.0.0/24
> Ingresa hosts separados por coma (Ej: 100,50,10): 100,50,10
	(muestra subredes asignadas y resumen)
```

**Notas y limitaciones**
- El script es interactivo y no está diseñado para uso en producción ni para manejar entradas malformadas complejas; valida manualmente las redes y los requisitos.
- Para redes con prefijos /31 o /32 el cálculo de hosts útiles se adapta, pero tenga en cuenta las restricciones de esas máscaras.

**Contribuir**
- Fork y pull requests son bienvenidos. Para cambios propuestos, añade tests o ejemplos si aplican.

**Licencia**
- Revisa el archivo [LICENSE](LICENSE) para detalles sobre la licencia del proyecto.

---

Si quieres, puedo añadir ejemplos de salida reales, pruebas unitarias básicas o un archivo `requirements.txt` (aunque no hay dependencias externas). ¿Quieres que agregue alguno de esos ahora?

**Construir ejecutable (PyInstaller)**

El repositorio incluye un archivo de especificación para PyInstaller: `calculo_ip.spec`. Este archivo ya está configurado para generar un ejecutable llamado `calculo_ip` (opción `name='calculo_ip'`), con `upx` habilitado y `console=True`.

Pasos rápidos para generar el ejecutable en tu máquina:

```bash
# Instalar PyInstaller (recomendado en un virtualenv)
pip install pyinstaller

# Desde la carpeta del proyecto, usar el .spec incluido
pyinstaller calculo_ip.spec

# El ejecutable resultante estará en la carpeta `dist/calculo_ip/`
```

Notas:
- Si no quieres usar el `.spec`, también puedes ejecutar `pyinstaller --onefile calculo_ip.py` para generar un único binario.
- `upx=True` en el `.spec` permitirá comprimir el ejecutable si tienes `upx` instalado en tu sistema; si causa problemas, edita `calculo_ip.spec` y pon `upx=False` o instala `upx`.
- En Windows, ejecuta los comandos desde PowerShell o cmd con permisos adecuados.

Si quieres, puedo generar el ejecutable aquí y añadir el binario al repositorio (no recomendado) o preparar un release ZIP listo para subir a GitHub. ¿Qué prefieres?
