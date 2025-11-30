from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def parse_images(category):
    """Парсит изображения по категории"""
    driver = webdriver.Firefox()
    images_data = []
    
    try:
        driver.get(f"https://yandex.ru/images/search?text={category}")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img.ImagesContentImage-Image"))
        )
        
        time.sleep(2)
        
        images = driver.find_elements(By.CSS_SELECTOR, "img.ImagesContentImage-Image")[:6]
        
        for i, img in enumerate(images):
            src = img.get_attribute("src")
            if src and src.startswith("//"):
                src = "https:" + src
            if src:
                images_data.append({
                    'url': src,
                    'filename': f'image_{i+1}.jpg'
                })
                
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()
        
    return images_data