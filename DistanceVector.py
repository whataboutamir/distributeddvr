# This defines a DistanceVector (specialization of the Node class)
# that can run the Bellman-Ford algorithm. 
        											
from Node import *
from helpers import *

class DistanceVector(Node):
    
    def __init__(self, name, topolink, outgoing_links, incoming_links):
        ''' Constructor. This is run once when the DistanceVector object is
        created at the beginning of the simulation. Initializing data structure(s)
        specific to a DV node is done here.'''

        super(DistanceVector, self).__init__(name, topolink, outgoing_links, incoming_links)        
        self.vector = {}
        self.vector[self.name] = 0

    def send_initial_messages(self):
        ''' This is run once at the beginning of the simulation, after all
        DistanceVector objects are created and their links to each other are
        established, but before any of the rest of the simulation begins. 
        Nodes send out their initial DV advertisements here.'''

        msg = (self.name, self.vector)
        for neighbour in self.incoming_links:
            self.send_msg(msg, neighbour.name)

    def process_BF(self):
        ''' This is run continuously (repeatedly) during the simulation. DV
        messages from other nodes are received here, processed, and any new DV
        messages that need to be sent to other nodes as a result are sent. '''

        # 1. Process queued messages
        
        vector_updated = False        

        for msg in self.messages:            
            origin, vector = msg
            for node in vector:
                if node != self.name:
                    new_cost = int(self.get_outgoing_neighbor_weight(origin)) + vector[node]
                    if node not in self.vector:
                        if vector[node] <= -99:
                            self.vector[node] = -99
                        else:
                            self.vector[node] = new_cost
                        vector_updated = True
                    else:
                        if vector[node] <= -99 and self.vector[node] != -99:
                            self.vector[node] = -99
                            vector_updated = True
                        elif vector[node] > -99 and self.vector[node] > new_cost:
                            self.vector[node] = new_cost
                            vector_updated = True 

        # Empty queue
        self.messages = []

        # 2. Send neighbors updated distances               
        
        if vector_updated:
            msg = (self.name, self.vector)
            for neighbour in self.incoming_links:
                self.send_msg(msg, neighbour.name) 
        

    def log_distances(self):
        ''' This function is called immedately after process_BF each round.  It 
        prints distances to the console and the log file in the following format (no whitespace either end):
        
        A:A0,B1,C2
        
        Where:
        A is the node currently doing the logging (self),
        B and C are neighbors, with vector weights 1 and 2 respectively
        NOTE: A0 shows that the distance to self is 0 '''
        
        entry = ",".join("{}{}".format(node, cost) for node, cost in self.vector.items())
        add_entry(self.name, entry)