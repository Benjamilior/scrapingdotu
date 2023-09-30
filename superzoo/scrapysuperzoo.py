#Codigo para sacar el precio de producto donde la pagina no tiene boton 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#Ejecutador del Codigo

# PATH = "C:\\Program Files (x86)\\chromedriver.exe"
PATH = "/usr/local/bin/chromedriver"
# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ver el Navegador
chrome_options.add_argument("--window-size=1920x1080")

start_time = time.time()  # Tiempo de inicio de la ejecución

driver = webdriver.Chrome(options=chrome_options)


direccionestipo2 = ["/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[1]/input",
               "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[2]/input",
               "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[3]/input"]
direccionestipo3 = ["/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[1]/input",
               "/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/ul/li[2]/input"]



#URLs

tipo1 = [
    "https://www.superzoo.cl/gato/alimentos/alimento-seco/acana-cat-first-feast-1.8-kg-alimento-para-gato/9509.html",
    "https://www.superzoo.cl/gato/alimentos/alimento-seco/fit-formula-gato-adulto-alimento-para-gato/652_m.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-seco/fit-formula-senior-20-kg-alimento-para-perro/1396.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-seco/fit-formula-adulto-alimento-para-perro/563_m.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-seco/fit-formula-cachorro-alimento-para-perro/575_m.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-seco/fit-formula-adulto-razas-pequenas-alimento-para-perro/651_m.html",
    "https://www.superzoo.cl/perro/farmacia/farmacia-pipetas/desparasitante-bravecto-para-perros-20-kg-a-40-kg/1138.html",
    "https://www.superzoo.cl/perro/farmacia/farmacia-pipetas/desparasitante-bravecto-para-perros-10-kg-a-20-kg/1137.html",
    "https://www.superzoo.cl/perro/farmacia/farmacia-pipetas/desparasitante-bravecto-para-perros-45-kg-a-10-kg/1136.html",
    "https://www.superzoo.cl/gato/farmacia/farmacia-farmacos/desparasitante-bravecto-para-gatos-2.8---6.25kg/7503.html",
    "https://www.superzoo.cl/promociones/delivery-express/desparasitante-bravecto-para-perros-2-kg-a-45-kg/1135.html",
    "https://www.superzoo.cl/gato/farmacia/farmacia-farmacos/desparasitante-bravecto-para-gatos-1.2---2.8kg/7502.html",
    "https://www.superzoo.cl/gato/farmacia/farmacia-farmacos/feliway-repuesto-para-difusor-48-ml/3941.html",
    "https://www.superzoo.cl/gato/farmacia/farmacia-repelentes/feliway-en-spray-60-ml/1243.html",
    "https://www.superzoo.cl/gato/accesorios/otros-accesorios/feliway-friends-repuesto-para-difusor-48ml/3943.html",
    "https://www.superzoo.cl/gato/accesorios/otros-accesorios/feliway-difusor-y-repuesto-48ml/3939.html",
    "https://www.superzoo.cl/gato/farmacia/farmacia-farmacos/feliway-friends-difusor-y-repuesto-48ml/3942.html",
    "https://www.superzoo.cl/gato/alimentos/alimento-seco/royal-canin-mother-and-baby-cat-alimento-para-gato/43_m.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-medicados/royal-canin-alimento-seco-perro-adulto-hypoallergenic/56_m.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-seco/royal-canin-adulto-mini-adult-alimento-para-perro/9_m.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-seco/bil-jac-small-breed-adulto-alimento-para-perros-2.7-kg/1189.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-seco/bil-jac-puppy-select-alimento-para-perros/565_m.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-seco/oven-baked-tradition-adult-all-breeds-chicken-alimento-para-perro/2145_m.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-seco/oven-baked-tradition-adult-all-breeds-fish-alimento-para-perro/2146_m.html",
    "https://www.superzoo.cl/perro/alimentos/alimentos-seco/oven-baked-tradition-senior-and-weight-mgt.-all-breeds-chicken-11.34-kg-alimento-para-perro/4175.html",
    "https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/silimarina/2354_m.html",
    "https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/oxtrin-30-comprimidos/1174.html",
    "https://www.superzoo.cl/gato/farmacia/farmacia-arena-para-gato/arena-para-gatos-sanitaria-traper/2861_m.html",
    "https://www.superzoo.cl/gato/farmacia/farmacia-farmacos/calmer-30-ml-spray/7473.html",
    "https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/arti-tabs-complex-60-tabletas/10342.html",
    "https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/condrovet-30-comprimidos/6535.html",
    "https://www.superzoo.cl/perro/alimentos/snack-y-premios/wanpy-soft-lamb-jerky-slices/6094_m.html",
    "https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/sucravet-100-ml/2078.html",
    "https://www.superzoo.cl/perro/accesorios/accesorios-entrenamiento/adaptil-difusor-electrico-repuesto-48-ml/4204.html"
]

tipo2 = ["https://www.superzoo.cl/gato/farmacia/farmacia-farmacos/revolution-plus-gato/4579_m.html",
"https://www.superzoo.cl/gato/farmacia/farmacia-farmacos/revolution-plus-gato/4579_m.html",
"https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/simparica-80-mg-antiparasitario-oral-antiparasitarios/2171_m.html",
"https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/simparica-80-mg-antiparasitario-oral-antiparasitarios/2171_m.html",
"https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/simparica-40-mg-antiparasitario-oral-antiparasitarios/2170_m.html",
"https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/simparica-40-mg-antiparasitario-oral-antiparasitarios/2170_m.html",
"https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/simparica-20-mg-antiparasitario-oral-antiparasitarios/2169_m.html",
"https://www.superzoo.cl/perro/farmacia/farmacia-farmacos/simparica-20-mg-antiparasitario-oral-antiparasitarios/2169_m.html"]
tipo3 = []

#Diccionario para guardar los datos
results = []

#Tipo 1

for url in tipo1:

    driver.get(url)
    try:
        nombresku = driver.find_element("xpath", '/html/body/div[1]/div[2]/div/div[3]/div[2]/div[3]/div/h1') #CAMBIAR
        precio = driver.find_element(By.CLASS_NAME, "sales")#CAMBIAR
        
        print(nombresku.text + " " + precio.text)
        data = {
                "Nombre SKU": nombresku.text,
                "Precio": precio.text
            }

            # Add the dictionary to the results list
        results.append(data)

    except Exception as e:
        print(f"No hay Stock de {url}: {str(e)}")
        


# #Tipo 2
# for i in direccionestipo2:
#     for a in tipo2:
#         driver.get(a)  # Cambia la URL para cada botón

#         # Apretar el botón correspondiente
#         boton = driver.find_element(By.XPATH, i)  # Puedes usar "url" para ubicar el botón si es único en cada página
#         boton.click()
#         time.sleep(1)

#         # Seleccionar todos los Xpath Extradiables
#         nombresku = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/h1/span')
#         price = driver.find_element_by_class_name('product-price')
#         tipoalimento = driver.find_element(By.XPATH, i)

#         resultado_dict = {
#             'nombre': nombresku.text,
#             'tipo_alimento': tipoalimento.text,
#             'precio': price.text
#         }
#         results.append(resultado_dict)

#Tipo 3
# for i in direccionestipo3:
#     for a in tipo3:
#         driver.get(a)  # Cambia la URL para cada botón

#         # Apretar el botón correspondiente
#         boton = driver.find_element(By.XPATH, i)  # Puedes usar "url" para ubicar el botón si es único en cada página
#         boton.click()
#         time.sleep(1)

#         # Seleccionar todos los Xpath Extradiables
#         nombresku = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/h1/span')
#         price = driver.find_element_by_class_name('product-price')
#         tipoalimento = driver.find_element(By.XPATH, i)

#         resultado_dict = {
#             'nombre': nombresku.text,
#             'tipo_alimento': tipoalimento.text,
#             'precio': price.text
#         }
#         results.append(resultado_dict)
        
#Tipo 4

#Tipo 5

#Tipo 6


driver.quit()

print(results)
end_time = time.time()  # Tiempo de finalización de la ejecución

execution_time = end_time - start_time

print("Tiempo de ejecución: %.2f segundos" % execution_time)

      
