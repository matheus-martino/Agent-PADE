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
		return -1
        
	def desregistrar(self, nomeAgente):
		self.kill = None
		i=-1
		print(nomeAgente)
		for idx, list in enumerate(self.posicao):
			if nomeAgente in list:
				i=i+1
				self.kill = idx
				print(self.kill)                
		if self.kill is not None:		
			del self.posicao[self.kill]        
      

class AgPeca(Agent):
	def setup(self):
		# Adding behaviours to this agent
		reg1 = Registro()
		self.add_behaviour(Peca(self,reg1))

class Peca(CyclicBehaviour):
	def __init__(self, agent, reg1):
		super().__init__(agent)
		self.reg1=reg1
        
        i=1
        
            
        
	def action(self):
        
        
        

if __name__ == '__main__':

    agents = list()
    agents.append(AgPeca('Peca1'))
    #maquina.ams={'name':'10.34.15.221','port':8000}
    start_loop(agents)