# -*- coding: utf-8 -*-
"""taller 3 count_word

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dsacKQCMP5q24xzx_i_j8BLqc7puqg38
"""

from collections import Counter

# frecuencia de palabras
def calcular_frecuencias(texto):
    palabras = texto.split()
    contador = Counter(palabras)
    return contador

# obtener el ranking de las palabras
def obtener_ranking(texto):
    frecuencias = calcular_frecuencias(texto)
    ranking = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    return ranking

texto_ejemplo = """
desarrollo desarrollo codigo principios datos desarrollo
codigo principios desarrollo desarrollo datos datos
"""
#palabras mas repetidas
ranking = obtener_ranking(texto_ejemplo)

#imprimir
for palabra, frecuencia in ranking:
    print(f"{palabra}: {frecuencia}")

# Base de datos
database = {
    "desarrollo": [1, 5],
    "rama": [8, 32, 11],
    "programacion": [1, 15, 5, 8]

}

#buscar los documentos con la palabra
def buscar_documentos(palabra, database):
    if palabra in database:
        return database[palabra]
    else:
        return []

#palabra que se quiere buscar
palabra_busqueda = "programacion"

#recibir la lista con la palabra
documentos_encontrados = buscar_documentos(palabra_busqueda, database)

#imprimir los documentos que se hallaron
print(f"Documentos que contienen la palabra '{palabra_busqueda}': {documentos_encontrados}")

mis_documentos = [
    "1. La programación en Python es clave para el trabajo con datos",
    "2. Los programadores en Java tienen un alto interés en pasar a Python",
    "3. La optimización de algoritmos es fundamental en el desarrollo de software",
    "4. Las bases de datos relacionales son esenciales para muchas aplicaciones",
    "5. El paradigma de programación funcional gana popularidad",
    "6. La seguridad informática es un tema crucial en el desarrollo de aplicaciones web",
    "7. Los lenguajes de programación modernos ofrecen abstracciones poderosas",
    "8. La inteligencia artificial está transformando diversas industrias",
    "9. El aprendizaje automático es una rama clave de la ciencia de datos",
    "10. Las interfaces de usuario intuitivas mejoran la experiencia del usuario",
    "11. La calidad del código es esencial para mantener un proyecto exitoso",
    "11. La agilidad en el desarrollo de software permite adaptarse a cambios rápidamente",
    "12. Las pruebas automatizadas son cruciales para garantizar la estabilidad del software",
    "13. La modularización del código facilita la colaboración en equipos de programadores",
    "14. El control de versiones es necesario para rastrear cambios en el código",
    "15. La documentación clara es fundamental para que otros entiendan el código",
    "16. La programación orientada a objetos promueve la reutilización de código",
    "17. La resolución de problemas es una habilidad esencial en la programación",
    "18. La optimización prematura puede llevar a código complicado y difícil de mantener",
    "19. El diseño de interfaces de usuario atractivas mejora la usabilidad de las aplicaciones",
    "20. El código limpio es esencial para facilitar el mantenimiento",
    "21. Los patrones de diseño son soluciones probadas para problemas comunes",
    "22. Las pruebas unitarias garantizan el correcto funcionamiento de las partes del código",
    "23. El desarrollo ágil prioriza la entrega continua de valor al cliente",
    "24. Los comentarios en el código deben ser claros y útiles",
    "25. La recursividad es una técnica poderosa en la programación",
    "26. Las bibliotecas de código abierto aceleran el desarrollo de software",
    "27. La virtualización permite una mejor utilización de los recursos de hardware",
    "28. La seguridad en la programación web es fundamental para prevenir ataques",
    "29. Los principios SOLID son fundamentales para el diseño de software robusto",
    "30. La arquitectura de microservicios permite escalar componentes individualmente",
    "31. La refactorización mejora la calidad del código sin cambiar su comportamiento",
    "32. Los sistemas distribuidos presentan desafíos en la sincronización de datos",
    "33. El enfoque DevOps une el desarrollo y las operaciones para una entrega eficiente",
    "34. Las bases de datos NoSQL son útiles para manejar datos no estructurados",
    "35. La agilidad en el desarrollo permite adaptarse a cambios del mercado",
    "36. Las buenas prácticas en el control de versiones facilitan la colaboración",
    "37. La programación concurrente mejora la eficiencia en sistemas multiusuario",
    "38. Los marcos de trabajo MVC separan la lógica de la interfaz de usuario",
    "39. La interacción entre aplicaciones se logra a través de APIs",
    "40. El machine learning permite a las máquinas aprender de los datos",
    "41. La analítica de datos ayuda a tomar decisiones basadas en información",
    "42. El diseño responsivo garantiza una experiencia consistente en diferentes dispositivos",
    "43. Las pruebas de carga verifican el rendimiento de las aplicaciones",
    "44. El enfoque centrado en el usuario mejora la usabilidad de las aplicaciones",
    "45. La programación reactiva es útil para manejar flujos de datos asincrónicos",
    "46. Los contenedores facilitan la implementación y el despliegue de aplicaciones",
    "47. La gestión de dependencias es esencial para administrar las bibliotecas externas",
    "48. La integración continua automatiza la verificación de cambios en el código",
    "49. El aprendizaje profundo es una rama avanzada del machine learning",
    "50. La depuración es una habilidad crucial para encontrar y corregir errores",
    "51. La criptografía protege la información sensible en aplicaciones",
    "52. El desarrollo full-stack abarca tanto el frontend como el backend",
    "53. Las pruebas de seguridad ayudan a identificar vulnerabilidades en el software",
    "54. La agilidad cultural es clave para adoptar prácticas ágiles de manera efectiva",
    "55. La infraestructura como código permite automatizar la gestión de servidores",
    "56. Los patrones arquitectónicos guían la estructura general de una aplicación",
    "57. El análisis predictivo utiliza datos históricos para predecir tendencias",
    "58. Las interfaces API REST son ampliamente utilizadas para comunicarse con aplicaciones",
    "59. El rendimiento de las aplicaciones es esencial para brindar una buena experiencia",
    "60. La virtualización de servidores reduce costos y facilita la administración",
    "61. La ingeniería de software implica la aplicación de métodos sistemáticos",
    "62. El código autodocumentado es claro y fácil de entender para otros programadores",
    "63. La integración de sistemas conecta diferentes aplicaciones para trabajar juntas",
    "64. Las metodologías ágiles promueven la adaptación y la colaboración continua",
    "65. El monitoreo de aplicaciones permite identificar y resolver problemas en tiempo real",
    "66. El análisis de datos masivos (big data) abre oportunidades para obtener insights",
    "67. El diseño de interfaces de usuario es crucial para la experiencia del usuario",
    "68. La seguridad en el desarrollo es un proceso constante de mitigación de riesgos"
]

#Buscar la palabra
def buscar_documentos(palabra, documentos):
    resultados = []
    for i, doc in enumerate(documentos, start=1):
        if palabra in doc.lower():
            resultados.append(i)
    return resultados

#palabra que quiero buscar
palabra_buscar = "diseño"

#encontrar los documentos
documentos_coincidentes = buscar_documentos(palabra_buscar, mis_documentos)

#Imprimir los documentos que coinciden
print(f"Documentos que contienen la palabra '{palabra_buscar}': {documentos_coincidentes}")