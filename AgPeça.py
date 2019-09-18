from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from pade.acl.filters import Filter
from pade.behaviours.types import CyclicBehaviour, OneShotBehaviour
from pade.core.agent import Agent
from pade.misc.utility import display, start_loop

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
			if '1' in list:
				self.posicao[idx][1]='0'
			else:
				pass
			

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
         
		sublist.extend(['Dispensar Chassi','0'])
		self.reg1.registrar(sublist)
		del sublist[1]
		del sublist[0]
		sublist.extend(['Pintar','1'])
		self.reg1.registrar(sublist)             
        
	def action(self):
		sublist=[]
		sublist = self.reg1.procurar('0')
		print(self.reg1.posicao)
		print(sublist)
		if len(sublist)!=0:
			for processos in sublist:
				print(self.reg1.posicao[processos][0])
				self.reg1.desregistrar(self.reg1.posicao[processos][0])
				self.reg1.atualizar()                
			self.wait(10)
		else:
			print('vazio')
			self.wait(10)
		self.reg1.atualizar()
        

if __name__ == '__main__':

    agents = list()
    agents.append(AgPeca('Peca1'))
    #maquina.ams={'name':'10.34.15.221','port':8000}
    start_loop(agents)
