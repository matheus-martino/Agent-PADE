from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from pade.acl.filters import Filter
from pade.behaviours.types import CyclicBehaviour, OneShotBehaviour
from pade.core.agent import Agent
from pade.misc.utility import display, start_loop
import sys

class Registro:
	def __init__(self):
		self.posicao=[]
        
	def registrar(self, rlista):
		sublista=rlista
		self.posicao.append(sublista)
        
	def procurar(self, value):
		self.busca=[]
		i=-1
		for idx, list in enumerate(self.posicao):
			if value in list:
				i=i+1
				self.busca.append(idx)
		if self.busca is not None:
			return self.busca
		return None
        
	def desregistrar(self, nomeServ):
		self.kill = None
		i=-1
		#print(nomeServ)
		for idx, list in enumerate(self.posicao):
			if nomeServ in list:
				i=i+1
				self.kill = idx
		#		print(self.kill)                
		if self.kill is not None:		
			del self.posicao[self.kill] 
            
	def atualizar(self):
		self.atualizacao=[]
		for idx, list in enumerate(self.posicao):
			self.posicao[idx][1]=(self.posicao[idx][1])-1
			

class AgPeca(Agent):
	def setup(self):
		# Adding behaviours to this agent
		reg1 = Registro()
		self.add_behaviour(Peca(self,reg1))

class Peca(CyclicBehaviour):
	def __init__(self, agent, reg1):
		super().__init__(agent)
		self.reg1=reg1
		sublist=[]
		inputList = []
		
		#sublist.append(['Dispensar Chassi',0])
		#sublist.append(['Montar roda',0])
		#sublist.append(['Batman',0])
		#sublist.append(['Pintar',1])
		#sublist.append(['Furar',1])
		#sublist.append(['Entregar',2])
		inputList = sys.argv[3].split(":") #Exemplo: 'Dispensar Chassi:0:Montar Roda:1:Furar:1:Entregar:2'
		for i in range(0, len(inputList), 2):
			chunk = inputList[i:i + 2]
			chunk[1] = int(chunk[1])
			sublist.append(chunk)
			
		tamanho_sublist=len(sublist)
		for i in range(tamanho_sublist):
			self.reg1.registrar(sublist[i]) 
		self.wait(10)            
        
	def action(self):
		sublist=[]
		nomeServ=[]
		sublist = self.reg1.procurar(0)
		print(self.reg1.posicao)
		print('FLAG 1')
		print(sublist)
		print('FLAG 2')
        
		if len(sublist)!=0:
			tamanho_sublist=len(sublist)
			for processos in range(tamanho_sublist):
				print(self.reg1.posicao[processos][0])
				nomeServ.append(self.reg1.posicao[processos][0])#só botar essa função para  serviços que foram concluidos
				#self.reg1.desregistrar(self.reg1.posicao[processos][0])#problema aqui
				print(self.reg1.posicao[processos][0])
				print('FLAG 3')
				self.wait(10)
		else:
			print('vazio')
			self.reg1.atualizar()
            
		if len(nomeServ)!=0:
			tamanho_nomeServ=len(nomeServ)
			for servicos in range(tamanho_nomeServ):
				self.reg1.desregistrar(nomeServ[servicos])
            
        

if __name__ == '__main__':

    agents = list()
    agents.append(AgPeca('Peca1'))
    #maquina.ams={'name':'10.34.15.221','port':8000}
    start_loop(agents)
