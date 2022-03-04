# Teste Promaxima

## free_proxy

- necessário Firefox instalado
- Após rodando a máquina virtual, insta-le requirements.txt (pip install -r requirements.txt)
- Em ./free_proxy_list/data/views.py, alterar o caminho para o geckodriver.exe (./free_proxy_list/geckodriver.exe) de acordo com seu computador. 
  - Para achar o caminho, no caso do Windows, clique com o **botão direito** em geckodriver.exe -> **propriedades** -> aba **Geral** -> Local
- Feito isso basta rodar o servidor django do free_proxy
- Eventualmente, quando clicar no botão Colect Proxys, será necessário passar por uma verificação contra robôs
  - O programa usa um time de 20 segundos para passar essa verificação, essa parte necessita de interação humana para passar a verificação
- para adicionar, deletar ou editar -> usar os botões Add, Delete e Edit, respectivamente.

Comentários:
  Neste programa usamos o selenium integrado com BeautifulSoup para fazer a raspagem por conta da verificação contra robôs.


## gasolina

- Após rodando a máquina virtual, insta-le requirements.txt (pip install -r requirements.txt) ... O arquivo requirements.txt é o mesmo para free_proxy e para gasolina
- rodar o servidor django gasolina
- clicar no botão para coletar os dados
- para adicionar, deletar ou editar -> usar os botões Add, Delete e Edit, respectivamente.
