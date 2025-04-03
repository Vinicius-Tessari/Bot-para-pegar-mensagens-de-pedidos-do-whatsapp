📱 Extrator de Pedidos de Grupos do WhatsApp
Extrai e organiza informações de pedidos de grupos do WhatsApp para uma planilha Excel automaticamente!

🌟 Funcionalidades
Login automático no WhatsApp Web

Extrai detalhes de pedidos das mensagens do grupo

Organiza os dados em um arquivo Excel estruturado

Lida com múltiplos produtos por pedido

Rola toda a história de mensagens

Mantém sua sessão e configurações do Chrome

🛠️ Pré-requisitos
Antes de começar, você precisa ter:

Python 3.6 ou superior instalado

Google Chrome instalado

Conta no WhatsApp Web (com acesso ao grupo alvo)

📥 Instalação
Clone este repositório ou baixe o script

Instale os pacotes necessários:

bash
Copy
pip install selenium webdriver-manager openpyxl pyautogui
⚙️ Configuração
Abra o script em um editor de texto

Localize esta linha:

python
Copy
group_name = ""
Substitua "" pelo nome exato do seu grupo no WhatsApp (deve ser entre aspas duplas)

🚀 Como Usar
Execute o script:

bash
Copy
python whatsapp_pedidos.py
Escaneie o QR code quando solicitado (você tem 60 segundos)

Aguarde enquanto o script:

Faz login no WhatsApp Web

Navega até seu grupo

Rola todas as mensagens

Extrai e processa os pedidos

Encontre seu arquivo pedidos.xlsx gerado na mesma pasta do script

📊 Estrutura do Arquivo Excel
O arquivo Excel gerado conterá estas colunas:

Nome da Coluna	Descrição
Nome Completo	Nome completo do cliente
CPF	Número do CPF do cliente
Celular	Telefone do cliente
E-mail	E-mail do cliente
Rua	Nome da rua
Número	Número da residência
Complemento	Complemento do endereço
Bairro	Bairro
Cidade	Cidade
Estado	Estado
Ponto de referência	Ponto de referência
CEP	CEP
Quantidade	Quantidade do produto
Produto	Nome do produto
Preço	Preço do produto
Tipo do frete	Tipo de frete
Valor do frete	Custo do frete
Total	Total do pedido
⏳ Tempo de Processamento
O tempo de execução depende de:

Tamanho do histórico de mensagens do grupo

Velocidade da conexão de internet

Desempenho do computador

Tempos típicos de processamento:

Grupos pequenos (50 mensagens): 1-2 minutos

Grupos médios (500 mensagens): 5-7 minutos

Grupos grandes (5000+ mensagens): 15-20 minutos

🔄 Atualizando Arquivos Existentes
O script irá automaticamente:

Deletar qualquer arquivo pedidos.xlsx existente

Criar um novo arquivo com os dados atuais

❌ Solução de Problemas
Problema: Tempo esgotado do QR code
Solução: Execute o script novamente e escaneie rapidamente

Problema: Grupo não encontrado
Solução: Verifique se o nome do grupo está exatamente como aparece no WhatsApp

Problema: Problemas com perfil do Chrome
Solução: Certifique-se que o Chrome não está rodando quando iniciar o script

Problema: Mensagens faltando
Solução: Aumente as tentativas de rolagem no código (mude tentativas < 10 para um número maior)

🤝 Contribuindo
Contribuições são bem-vindas! Por favor abra uma issue ou pull request para:

Correções de bugs

Novas funcionalidades

Melhorias na documentação

📜 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

💡 Dica: Para melhores resultados, execute este script quando tiver uma boa conexão de internet e puder deixar seu computador ininterrupto durante o processamento.
