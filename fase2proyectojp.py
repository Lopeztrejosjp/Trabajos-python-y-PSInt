from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# ==============================================================================
# 1. Configuración Inicial y Preparación
# ==============================================================================

# 1.1. Configuraciones Anti-Bot (Básicamente hace que todo parezca "humano")
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False) 
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--log-level=3")

# Parametros clave
search_query = "PS5 precio" #Palabra clave a buscar
NUM_LINKS_TO_VISIT = 3 # Número de tiendas a visitar
driver = None # Variable global del driver

# LISTA DE DOMINIOS/PALABRAS CLAVE A EXCLUIR (Porque estas tiendas usualmente tienen captchas o bloqueos)
EXCLUDED_KEYWORDS = ["walmart", "credix", "mediamarkt", "carrefour"]

# Elementos comunes donde suele aparecer el precio en tiendas online
# (Se prueban en orden hasta encontrar uno que funcione)
PRICE_SELECTORS = [
    (By.CSS_SELECTOR, "[itemprop='price']"),
    (By.CSS_SELECTOR, "meta[property='product:price:amount']"),
    (By.CSS_SELECTOR, "[data-testid*='price']"), # Para componentes Reactivos
    (By.XPATH, "//span[contains(text(), '$') or contains(text(), '€') or contains(text(), '₡')]"),
    (By.CSS_SELECTOR, "div.price"),
    (By.CSS_SELECTOR, "span.amount"),
    (By.CSS_SELECTOR, "p.price"),
    (By.XPATH, "//*[contains(@class, 'price') or contains(@class, 'amount')]")
]
PRICE_WAIT_TIME = 6 
USER_VISIT_TIME = 8 #Esta es la pausa que el robot hace en cada tienda para que el usuario pueda inspeccionar

try:
    # 1.3. Abrir el Navegador usando webdriver-manager
    service = ChromeService(ChromeDriverManager().install()) #Asegura que el robot siempre use la versión de Chrome Driver compatible, previniendo el error más común de configuración inicial.
    driver = webdriver.Chrome(service=service, options=chrome_options) 
    print(f"✅ WebDriver iniciado para buscar: '{search_query}'")
    
    wait = WebDriverWait(driver, 15)  #Esto es para esperas explíctas, osea esperar a que ciertos elementos estén presentes
    driver.implicitly_wait(5) 

    # ==========================================================================
    # 2. Automatización de la Búsqueda
    # ==========================================================================

    driver.get("https://www.google.com") #Aca le decimos a selenium que abra google.com
    # Manejo de Cookies
    try:
        accept_button = wait.until(EC.element_to_be_clickable((By.ID, "L2AGLb"))) #Aca basicamente esperamos a que el boton de aceptar cookies sea clickeable
        accept_button.click()
    except:
        pass 
    time.sleep(1) 

    # Realizar la búsqueda
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    search_box.send_keys(search_query) 
    search_box.send_keys(Keys.RETURN) 
    print(f"➡️ Búsqueda ejecutada.")

    # ==========================================================================
    # 3. PAUSA OBLIGATORIA PARA RESOLVER EL CAPTCHA (Intervención Manual)
    # ==========================================================================
    
    time.sleep(5) 
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3")))
        print("✅ Resultados cargados. No se detectó bloqueo inicial.")
    except Exception:
        print("\n==================== 🛑 VERIFICACIÓN MANUAL REQUERIDA 🛑 ====================")
        print("   -> Por favor, revise la ventana de Chrome y resuelva el reCAPTCHA si aparece.")
        input("   -> PRESIONA ENTER en esta terminal DESPUÉS de que la página esté lista. ")
        print("✅ Reanudando la ejecución para recolectar URLs...")

    # ==========================================================================
    # 4. Extracción y Navegación a Tiendas (Lógica Clave)
    # ==========================================================================

    urls_to_visit = []
    
    # 4.1. Recolectar las URLs con el selector más robusto (a[.//h3])
    try:
        product_links = driver.find_elements(By.XPATH, "//a[.//h3]")
        
        for i, link_element in enumerate(product_links):
            if len(urls_to_visit) >= NUM_LINKS_TO_VISIT:
                break
            
            url = link_element.get_attribute("href")
            title_text = link_element.text.split('\n')[0].strip().lower()
            
            is_excluded = False
            for keyword in EXCLUDED_KEYWORDS:
                # Comprobar si la palabra clave está en la URL o en el texto del enlace
                if keyword in url.lower() or keyword in title_text:
                    is_excluded = True
                    break
            
            # FILTRO FINAL: Solo guardar si no está en la lista de exclusión
            if url and "google.com" not in url and "/search" not in url and not is_excluded:
                
                urls_to_visit.append(url)
                print(f"[{len(urls_to_visit)}] URL ENCONTRADA: {title_text[:40]}...")

    except Exception as e:
        print(f"❌ Fallo al intentar recolectar enlaces: {e.__class__.__name__}")

    # 4.2. BUCLE CLAVE: Navegación Múltiple con Extracción de Precio
    if urls_to_visit:
        print(f"✅ Se recolectaron {len(urls_to_visit)} URLs de tiendas.")
        print("\n================== NAVEGANDO A TIENDAS ==================")
        
        for i, url in enumerate(urls_to_visit):
            print(f"\n🖱️ VISITANDO TIENDA {i + 1}/{len(urls_to_visit)}...")
            
            try:
                driver.get(url)
                print(f"⭐ Título de la Tienda: {driver.title}")
                
                # BÚSQUEDA DEL PRECIO
                price = "Precio no encontrado (Verifique manualmente)"
                
                # Iterar sobre los selectores genéricos hasta encontrar el precio
                for selector_type, selector_value in PRICE_SELECTORS:
                    try:
                        # ESPERA AUMENTADA PARA CARGA DE JAVASCRIPT
                        price_element = WebDriverWait(driver, PRICE_WAIT_TIME).until(
                            EC.presence_of_element_located((selector_type, selector_value))
                        )
                        price_text = price_element.text.strip().split('\n')[0]
                        
                        # Filtro de cordura: debe contener dígitos para ser un precio
                        if len(price_text) > 2 and any(c.isdigit() for c in price_text):
                            price = price_text
                            break 
                    except:
                        continue 

                # RESULTADO FINAL MOSTRADO EN LA TERMINAL
                print(f"💰 **PRECIO ESTIMADO:** {price}")
                
                # PAUSA PARA INSPECCIÓN MANUAL
                time.sleep(USER_VISIT_TIME) 

            except Exception as e_nav:
                print(f"❌ Error al visitar {url}: {e_nav.__class__.__name__}")
                
        print("\nEl robot ha completado la visita a todas las tiendas.")
    else:
        print("\n⛔ No se encontraron URLs válidas para visitar. Fin de la navegación.")
    
except Exception as e:
    # Captura cualquier error grave de inicialización
    print(f"\n❌ Ocurrió un error grave durante la ejecución: {e}")

finally:
    # 5. MANTENER ABIERTO
    if driver:
        print("\n🛑 SCRIPT FINALIZADO. EL NAVEGADOR PERMANECERÁ ABIERTO.")
        print("   Presione Ctrl+C en la terminal para detener el script y cerrar la ventana.")
        while True:
            time.sleep(1)