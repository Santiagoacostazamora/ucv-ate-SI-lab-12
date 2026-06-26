# ucv-ate-SI-lab-12

## Laboratorio UCV - Perceptron Simple

Este proyecto implementa desde cero un perceptron simple en Python para resolver un problema de aprobacion preliminar de creditos bancarios.

## Objetivo

Implementar desde cero un perceptron simple para resolver un problema de aprobacion de creditos y comprender el aprendizaje de una neurona artificial.

## Caso de negocio

Un banco desea automatizar la aprobacion preliminar de creditos utilizando dos variables principales:

- Ingreso mensual.
- Historial crediticio.

El modelo debe predecir si un cliente debe ser aprobado o rechazado preliminarmente.

## Tecnologias utilizadas

- Python 3.12
- Git
- GitHub
- GitHub Actions
- pytest
- VS Code

## Estructura del proyecto

```text
ucv-ate-SI-lab-12/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── __init__.py
│   ├── dataset.py
│   └── perceptron.py
├── tests/
│   └── test_perceptron.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## Dataset

El archivo `src/dataset.py` contiene los datos de entrenamiento:

```python
training_data = [
    ([8, 1], 1),
    ([7, 1], 1),
    ([6, 1], 1),
    ([3, 0], 0),
    ([2, 0], 0),
    ([1, 0], 0),
]
```

Donde:

- El primer valor representa el ingreso mensual.
- El segundo valor representa el historial crediticio.
- La salida `1` significa credito aprobado.
- La salida `0` significa credito rechazado.

## Instalacion

Clonar el repositorio:

```bash
git clone https://github.com/TU-USUARIO/ucv-ate-SI-lab-12.git
cd ucv-ate-SI-lab-12
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

Activar el entorno virtual en Linux o macOS:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecucion del programa

```bash
python main.py
```

Salida esperada aproximada:

```text
Laboratorio UCV - Perceptron Simple
Pesos aprendidos: [...]
Bias aprendido: ...
----------------------------------------
Datos del cliente: [9, 1]
Prediccion: 1
Resultado: Credito aprobado
----------------------------------------
Datos del cliente: [2, 0]
Prediccion: 0
Resultado: Credito rechazado
```

## Ejecucion de pruebas

```bash
pytest
```

Resultado esperado:

```text
6 passed
```

## GitHub Actions

El proyecto incluye un workflow de integracion continua en:

```text
.github/workflows/ci.yml
```

Este workflow ejecuta las pruebas automaticamente cuando se realiza un `push` o un `pull_request`.

## Preguntas de analisis

### 1. ¿Que representan los pesos?

Los pesos representan la importancia de cada entrada dentro del modelo. En este caso, indican cuanto influyen el ingreso mensual y el historial crediticio en la decision final del perceptron.

Si un peso aumenta, significa que esa variable tiene mayor influencia en la prediccion. Durante el entrenamiento, el perceptron ajusta estos pesos para reducir los errores.

### 2. ¿Que funcion cumple el bias?

El bias permite desplazar la frontera de decision del perceptron. Gracias al bias, el modelo no depende unicamente de las entradas y puede ajustar mejor el punto desde el cual decide aprobar o rechazar un credito.

En terminos simples, el bias funciona como un valor adicional que ayuda al perceptron a tomar mejores decisiones.

### 3. ¿Como aprende el perceptron?

El perceptron aprende mediante un proceso de entrenamiento. Primero realiza una prediccion, luego compara esa prediccion con el resultado esperado. Si existe un error, ajusta sus pesos y el bias usando la tasa de aprendizaje.

La regla general es:

```text
nuevo peso = peso actual + tasa de aprendizaje * error * entrada
nuevo bias = bias actual + tasa de aprendizaje * error
```

Este proceso se repite durante varias epocas hasta que el modelo aprende a clasificar correctamente los datos de entrenamiento.

### 4. ¿Por que el perceptron no puede resolver XOR?

El perceptron simple no puede resolver XOR porque XOR no es un problema linealmente separable. Esto significa que no existe una sola linea recta capaz de separar correctamente las salidas 0 y 1.

Un perceptron simple solo puede resolver problemas donde las clases pueden separarse mediante una frontera lineal.

### 5. ¿Que ventajas tiene un perceptron multicapa?

Un perceptron multicapa tiene una o mas capas ocultas. Estas capas permiten aprender relaciones no lineales y resolver problemas mas complejos que un perceptron simple no puede resolver.

Entre sus ventajas estan:

- Puede resolver problemas no lineales.
- Puede aprender patrones mas complejos.
- Puede trabajar con mayor cantidad de variables.
- Es la base de las redes neuronales modernas.

## Reto MIT: problema XOR

El problema XOR se representa con la siguiente tabla:

| Entrada A | Entrada B | Salida XOR |
|----------:|----------:|-----------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

En XOR, la salida es 1 cuando las entradas son diferentes y es 0 cuando las entradas son iguales.

Un perceptron simple no puede resolver este problema porque no puede trazar una sola linea recta que separe los puntos con salida 1 de los puntos con salida 0.

Para resolver XOR se puede utilizar un perceptron multicapa. Este modelo usa una capa oculta que permite transformar el espacio de entrada y crear fronteras de decision no lineales. De esta manera, el modelo puede combinar varias neuronas para clasificar correctamente los cuatro casos de XOR.

## Comandos para subir a GitHub

```bash
git init
git add .
git commit -m "Laboratorio 12 - Perceptron Simple"
git branch -M main
git remote add origin https://github.com/Santiagoacostazamora/ucv-ate-SI-lab-12.git
git push -u origin main
```

Reemplaza `TU-USUARIO` por tu usuario real de GitHub.

## Autor

- Estudiante: Oscar Santiago Acosta Zamora 
- Curso: Sistemas Inteligentes
- Universidad: UCV
- Laboratorio: 12
