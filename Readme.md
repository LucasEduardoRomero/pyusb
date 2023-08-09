# Como rodar local

1. clonar repo
2. instalar pipenv
3. na pasta do projet rode pipenv install
4. pipenv shell para gerar virtualenv 
5. pegar libusb-1.0.dll e colocar no path das var de ambient do windows
6. rodar control.py para testar


### Notas dia 08/08/2023

Conseguimos fazer a leitura do dispositivo via código e printar na tela. Inicialmente ao rodar 'python teste.py' vai dar permission error.
Por isso é necessário 
1. pipenv shell - gerar o virtualenv
2. which python - pega o caminho do python deste env - vamos chamar de <CAMINHO_PYTHON>
3. sudo <CAMINHO_PYTHON> <CAMINHO_PROJETO>/linux_teste/read_barcode_scanner/read_barcode_scanner.py

