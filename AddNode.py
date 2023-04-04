import pygame, sys, random
import pygame.locals as pl
import pygame.event as pe
import AddEdge
from DFS import *
from Node import *
from Graph import *
import Handle_Button


# collide fund for checking if two nodes collide
def collide(pos, node):
    if node.isOver(pos):
        return True
    return False

# create_node func for creatind a new node
def create_node(node, pos, i):
    node.pos = pos
    node.text = "%d" % (i)
    node.data = i
    node.display = True

# add_node func for drawing the nodes on the window
def add_node(window, buttons, colors, graph, nodes, edges, i):

    node = None

    while True:

        window.fill(colors['paper'])
        pygame.draw.rect(window, colors['emerald'], (250, 50, 400, 300), 2)
        Handle_Button.draw_btns(buttons, colors['emerald'])
        node = Node(window, colors['green'])
        pos = pygame.mouse.get_pos()

        # event handling
        for event in pe.get():

            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pl.KEYDOWN:
                if event.key == pl.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pl.MOUSEBUTTONDOWN:
                if 250 < pos[0] <= 650 and 50 <= pos[1] <= 350:
                    if len(nodes) != 0:
                        if not any([collide(pos, x) for x in nodes]):
                            create_node(node, pos, i)
                            nodes.append(node)
                            i += 1
                    else:
                        create_node(node, pos, i)
                        nodes.append(node)
                        i += 1
                Handle_Button.button_handler(window, buttons, colors, graph, nodes, edges, i, pos)

            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.isOver(pos):
                        button.color = colors['silver']
                    else:
                        button.color = colors['blacksteel']

        graph.nodes = nodes
        graph.edges = edges

        # showing the graph
        graph.graph_show()

        pygame.display.update()
