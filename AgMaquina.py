from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from pade.acl.filters import Filter
from pade.behaviours.types import CyclicBehaviour, OneShotBehaviour
from pade.core.agent import Agent
from pade.misc.utility import display, start_loop
import threading


class maquina(Agent):
	def setup(self):
		# Adding behaviours to this agent
		self.add_behaviour(maquina1(self))


class maquina1(CyclicBehaviour):
	def __init__(self, agent):
		super().__init__(agent)
        
		self.primeira=0
		self.negociando=0
        
		self.run = self.primeira 
		self.estado = self.negociando

	def action(self):  
        
		cfp = Filter()
		cfp.set_performative(ACLMessage.CFP)
		accept = Filter()
		accept.set_performative(ACLMessage.ACCEPT_PROPOSAL)        
		# Preparando mensagem para cadastro DF
        
		if self.run == self.primeira:     
		    message = ACLMessage(ACLMessage.INFORM)
		    message.add_receiver(AID('DF'))
		    message.set_content('Dispensar Chassi')
		    # Sending the message
		    self.agent.send(message)
        
		    message = self.read()
        
		    if message.content == 'OK':
		        self.run = 1
		        display(self.agent, 'Registrado')

               
		message = self.read()
        
		if self.estado == self.negociando:
        
		    if cfp.filter(message):
        
		        if message.content == 'Dispensar Chassi':
            
			        reply = message.create_reply()
			        reply.set_performative(ACLMessage.PROPOSE)
			        reply.set_content('0')
			        self.agent.send(reply)
                
		        else:
            
		    	    reply = message.create_reply()
		        	reply.set_performative(ACLMessage.REJECT)
		        	reply.set_content('Servico invalido')                
		        	self.agent.send(reply)
                
		if accept.filter(message):
            
            if message.content == 'Dispensar Chassi':
            
		        self.estado = 1            
		        agente = []
		        agente.append(message.sender.getLocalName())
		        agente.append(message.content)
            #momento de aguardar o inform do transportador
		        display(self.agent, 'Dispensando Chassi')
            #momento de usar a Thread, devido o self.read() travar o programa
		        t = threading.Thread(target=tAuxiliar, args=(lambda : killEvent, ))
		        t.start()
                
		        self.wait(10)
                
		        killEvent = True
		        t.join()
                
		        display(self.agent, 'Dispensado')     
            
		        reply = message.create_reply()
		        reply.set_performative(ACLMessage.INFORM)
		        reply.set_content('pronto')
		        self.agent.send(reply)
                
		        self.estado = self.negociando
                
	def tAuxiliar(self, kill):
        
        while True:         
            message = self.read(False)
            print('Thread executando')
            if kill():
		        break
            if message is not None:      
        
		        reply = message.create_reply()
		        reply.set_performative(ACLMessage.REJECT)
		        reply.set_content('OCUPADO')
		        self.agent.send(reply)

if __name__ == '__main__':

    agents = list()
    agents.append(maquina('maquina1'))
    #maquina.ams={'name':'10.34.15.221','port':8000}
    start_loop(agents)
