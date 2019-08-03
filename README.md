# Agent-PADE
_A multi-agent solution developed in PADE with emphasis on use in Industrial Automation._

Deve ser executado com o "fork" do PADE disponivel em https://github.com/matheus-martino/pade

__GetIP.py__\
Fornece uma definição que retorna o endereço IP na rede local.
```bash
from GetIP import get_ip

IP = get_ip()
```
\
__run_machine.bat__\
Fornece automatização na inicializaçao de um agente máquina no Windows (não é compatível com Linux).
```bash
run_machine.bat nome_da_maquina "Serviços_da_máquina"
```
\
__run_part.bat__\
Fornece automatização na inicializaçao de um agente peça no Windows (não é compatível com Linux).
```bash
run_part.bat nome_da_peça "Serviços_requeridos"
```
