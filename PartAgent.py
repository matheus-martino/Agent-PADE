from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from pade.behaviours.types import OneShotBehaviour, CyclicBehaviour
from pade.core.agent import Agent
from pade.misc.utility import display, start_loop
from pade.acl.filters import Filter
from GetIP import get_ip
import sys

# Agent
class PartAgent(Agent):
	def setup(self):
		self.add_behaviour(SendMessage(self))

class SendMessage(OneShotBehaviour):
	def action(self):
		self.wait(5)
		
		message = ACLMessage(ACLMessage.REQUEST)
		message.add_receiver(AID('DF'))
		message.set_content(sys.argv[3])
		self.agent.send(message)
		display(self.agent, 'I sent REQUEST to DF: %s' %sys.argv[3])
        
		f = Filter()
		f.set_performative(ACLMessage.INFORM_IF) 
		message = self.read()
		if f.filter(message) and message.content == "OK":
			display(self.agent, 'Registro %s' %message.content)
			self.wait(5)
		else:
			display(self.agent, 'Erro de Registro: %s' %message.content)
			
	def done(self):
		message = ACLMessage(ACLMessage.INFORM)
		message.add_receiver(AID('DF'))
		message.set_content('morri')
		self.agent.send(message)
		display(self.agent, 'I sent morri to DF.')
		self.wait(5)
		return True

if __name__ == '__main__':
	agents = list()
	
	# Encontra o IP automaticamente
	localIP = get_ip()
	agents.append(PartAgent(sys.argv[2] + '@' + localIP + ':4000'))
	
	start_loop(agents)
