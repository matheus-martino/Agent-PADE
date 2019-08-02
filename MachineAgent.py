from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from pade.behaviours.types import OneShotBehaviour, CyclicBehaviour
from pade.core.agent import Agent
from pade.misc.utility import display, start_loop
from pade.acl.filters import Filter
import sys

# Agent
class MachineAgent(Agent):
	def setup(self):
		self.add_behaviour(SendMessage(self))

class SendMessage(OneShotBehaviour):
	def action(self):
		self.wait(5)
		
		message = ACLMessage(ACLMessage.INFORM)
		message.add_receiver(AID('DF'))
		message.set_content(sys.argv[2]) # ('pintar azul:pintar preto')
		self.agent.send(message)
		display(self.agent, 'I sent INFORM to DF: %s' %sys.argv[2])
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
	agents.append(MachineAgent('Maquina1'))
	start_loop(agents)