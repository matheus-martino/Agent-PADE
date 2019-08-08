from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from pade.acl.filters import Filter
from pade.behaviours.types import CyclicBehaviour, OneShotBehaviour
from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop
from GetIP import get_ip

class Directory(Agent):
	def setup(self):
		# Adding behaviours to this agent
		reg1 = Registro()
		self.add_behaviour(Dfacility(self, reg1)) 

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

class Dfacility(CyclicBehaviour):
	def __init__(self, agent, reg1):
		super().__init__(agent)
		self.reg1=reg1
        
	def action(self):
		print(self.reg1.posicao)
		sublist = []
		f = Filter()
		f.set_performative(ACLMessage.INFORM)
		m = Filter()
		m.set_performative(ACLMessage.REQUEST)
		message = self.read()
        
		if f.filter(message):   
			if message.content == 'morri':
				self.reg1.desregistrar(message.sender.getLocalName())
				print(self.reg1.posicao)
								
			else:
				sublist.append(message.sender.getLocalName())
				sublist.extend(message.content.split(":"))
        
				self.reg1.registrar(sublist)
				print(self.reg1.posicao)
		
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
                
		if m.filter(message):       
			sublist = self.reg1.procurar(message.content)
			outralista=[]
            
			for maquinas in sublist:
				outralista.append(self.reg1.posicao[maquinas][0] + ':')

			s = ''.join(outralista)
			
			print(s)
            
			reply = message.create_reply()
			reply.set_performative(ACLMessage.INFORM_IF)
			reply.set_content(s)
            
if __name__ == '__main__':
    agents = list()
	
	# Encontra o IP automaticamente
    localIP = get_ip()
    agents.append(Directory('DF@' + localIP + ':2000'))
	
    start_loop(agents)
