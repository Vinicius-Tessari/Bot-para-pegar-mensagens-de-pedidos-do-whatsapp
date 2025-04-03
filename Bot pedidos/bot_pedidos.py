from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
import time
import os
import re
import pyautogui

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--start-maximized")

user_data_dir = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--profile-directory=Default")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://web.whatsapp.com")
print("Escaneie o QR Code do WhatsApp Web...")

try:
    search_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    print("Login bem-sucedido!")
except:
    print("Erro ao fazer login. Verifique o QR Code e tente novamente.")
    driver.quit()
    exit()

group_name = "nome do grupo"
search_box.send_keys(group_name)
time.sleep(2)
try:
    group = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//span[@title="{group_name}"]'))
    )
    group.click()
    time.sleep(5)
except:
    print(f"Grupo '{group_name}' não encontrado.")
    driver.quit()
    exit()

def rolar_com_mouse():
    scroll_pause_time = 2
    tentativas = 0

    while tentativas < 5:
        pyautogui.moveTo(500, 500)
        pyautogui.scroll(1000)
        time.sleep(scroll_pause_time)
        tentativas += 1

    print("Rolagem concluída.")

def carregar_todas_as_mensagens():
    mensagens_coletadas = set()
    tentativas = 0

    while tentativas < 10:
        rolar_com_mouse()

        mensagens = driver.find_elements(By.XPATH, '//div[@data-pre-plain-text]')
        print(f"Encontradas {len(mensagens)} mensagens visíveis.")

        for mensagem in mensagens:
            mensagens_coletadas.add(mensagem)

        if len(mensagens_coletadas) > len(mensagens):
            break

        tentativas += 1

    print(f"{len(mensagens_coletadas)} mensagens coletadas.")
    return list(mensagens_coletadas)

messages = carregar_todas_as_mensagens()

pedidos = []
for message in messages:
    try:
        content = message.text
        print(f"Conteúdo da mensagem: {content}")
        
        if "Nome Completo:" in content and "Total:" in content:
            pedido = {
                "Nome Completo": "", "CPF": "", "Celular": "", "E-mail": "", "Rua": "",
                "Número": "", "Complemento": "", "Bairro": "", "Cidade": "", "Estado": "",
                "Ponto de referência": "", "CEP": "", "Produto": "", "Quantidade": "",
                "Preço": "", "Tipo do frete": "", "Valor do frete": "", "Total": ""
            }
            
            produtos = []
            
            for linha in content.split("\n"):
                linha = linha.strip()
                if ":" in linha:
                    campo, valor = linha.split(":", 1)
                    campo = campo.strip()
                    valor = valor.strip()

                    if campo in pedido:
                        pedido[campo] = valor
                    
                    elif re.match(r'^\d+x\s.+(?::\s*R\$[\d,]+)?$', linha):
                        match = re.match(r'^\d+x\s(.+)(?::\s*(R\$[\d,]+))?$', linha)
                        if match:
                            quantidade_produto = linha.split('x')[0].strip()
                            nome_produto = match.group(1).strip()
                            preco_produto = match.group(2).strip() if match.group(2) else ""
                        else:
                            quantidade_produto = ""
                            nome_produto = linha.split('x')[-1].split(':')[0].strip() if ':' in linha else linha.split('x')[-1].strip()
                            preco_produto = linha.split(':')[-1].strip() if ':' in linha else ""
                            
                        produtos.append({
                            "Quantidade": quantidade_produto,
                            "Produto": nome_produto,
                            "Preço": preco_produto
                        })
            
            for produto in produtos:
                novo_pedido = pedido.copy()
                novo_pedido["Quantidade"] = produto["Quantidade"]
                novo_pedido["Produto"] = produto["Produto"]
                novo_pedido["Preço"] = produto["Preço"]
                pedidos.append(novo_pedido)

    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        continue

if pedidos:
    wb = Workbook()
    ws = wb.active
    ws.title = "Pedidos"
    
    cabecalhos = [
        "Nome Completo", "CPF", "Celular", "E-mail", "Rua", "Número", 
        "Complemento", "Bairro", "Cidade", "Estado", "Ponto de referência", 
        "CEP", "Quantidade", "Produto", "Preço", "Tipo do frete", "Valor do frete", "Total"
    ]
    
    ws.append(cabecalhos)
    
    for pedido in pedidos:
        linha = [
            pedido["Nome Completo"], pedido["CPF"], pedido["Celular"], pedido["E-mail"],
            pedido["Rua"], pedido["Número"], pedido["Complemento"], pedido["Bairro"],
            pedido["Cidade"], pedido["Estado"], pedido["Ponto de referência"], pedido["CEP"],
            pedido["Quantidade"], pedido["Produto"], pedido["Preço"], pedido["Tipo do frete"], 
            pedido["Valor do frete"], pedido["Total"]
        ]
        ws.append(linha)
    
    arquivo_excel = "pedidos.xlsx"
    if os.path.exists(arquivo_excel):
        os.remove(arquivo_excel)
    wb.save(arquivo_excel)
    print(f"{len(pedidos)} pedidos salvos em '{arquivo_excel}'!")
else:
    print("Nenhum pedido válido encontrado.")

driver.quit()