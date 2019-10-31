# Agent-PADE
_A multi-agent solution developed in PADE with emphasis in Industrial Automation._

Deve ser executado com o "fork" do PADE disponivel em https://github.com/matheus-martino/pade \
Neste fork foi adicionado a possibilidade de o operador repassar até 2 comandos via linha de comando para o agente.

__GetIP.py__\
Fornece uma definição que retorna o endereço IP na rede local.
```bash
from GetIP import get_ip

IP = get_ip()
```
\
__run_machine.bat__\
Fornece automatização na inicializaçao de um agente máquina no Windows (não é compatível com Linux). \
Formato:
```bash
run_machine.bat nome_da_maquina "Serviços_da_máquina"
```
Exemplo:
```bash
run_machine.bat Maquina1 "Serviço1:Serviço2:Serviço3"
```
__run_part.bat__\
Fornece automatização na inicializaçao de um agente peça no Windows (não é compatível com Linux). \
Formato:
```bash
run_part.bat nome_da_peça "Serviço1:Prioridade1:Serviço2:Prioridade2:Serviço3:Prioridade3"
```
Exemplo:
```bash
run_part.bat Peça1 "Serviço1:1:Serviço2:2:Serviço3:3"
```
