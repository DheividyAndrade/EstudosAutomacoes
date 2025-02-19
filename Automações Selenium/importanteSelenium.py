driver = iniciar_driver()
driver.get("https://cursoautomacao.netlify.com/")  # navegar até um site
driver.maximize_window()  # maximizar a janela
driver.refresh()  # recarrega página atual
driver.get(driver.current_url)  # recarrega página atual
driver.back()  # volta à página anterior
driver.forward()  # navega 1 vez para frente
print(driver.title)  # Obtem título da página
print(driver.current_url)  # Obtem URL(endereço) da página atual
print(driver.page_source)  # Obtem o código fonte da página atual
# obtem o texto dentro de um elemento
print(driver.find_element(By.XPATH, '//a[@class="navbar-brand"]').text)
print(driver.find_element(    By.XPATH, '//a[@class="navbar-brand"]').get_attribute("style"))

driver.close() # Fecha janela atual
input('')
