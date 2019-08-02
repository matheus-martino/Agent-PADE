from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from pade.acl.filters import Filter
from pade.behaviours.types import CyclicBehaviour, OneShotBehaviour
from pade.core.agent import Agent, AgentFactory
from pade.misc.utility import display_message, start_loop
from pade.core.new_ams import ComportVerifyConnTimed



class Directory(Agent):
	def setup(self):
		# Adding behaviours to this agent
		self.add_behaviour(Dfacility(self))  

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

reg1 = Registro()

class Dfacility(CyclicBehaviour):
	def action(self):
		self.wait(1)
		print(reg1.posicao)
		sublist = []
		f = Filter()
		f.set_performative(ACLMessage.INFORM) 
		message = self.read()
		if f.filter(message):   
			if message.content == 'morri':
				reg1.desregistrar(message.sender.getLocalName())
				print(reg1.posicao)
								
			else:
				sublist.append(message.sender.getLocalName())
				sublist.extend(message.content.split(":"))
        
				reg1.registrar(sublist)
				print(reg1.posicao)
		
				reply = message.create_reply()
				reply.set_performative(ACLMessage.INFORM_IF)
				reply.set_content('OK')
				display_message(self.agent, '%s registrado no DF' % message.sender.getLocalName())
                # Wait a time before send the message
                #(Do you want to see the results, do not you?)
				self.wait(0.5)
                # Sending the message
				self.agent.send(reply)
				#print(resultado)


if __name__ == '__main__':
    agents = list()
    agents.append(Directory('DF'))
    start_loop(agents)
