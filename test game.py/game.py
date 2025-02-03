import pygame
import socket
import pickle
 
# Initialize pygame
pygame.init()
 
# Set up the display
window_size = (1500, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Simple Pygame Game Client")
 
# Networking setup
server_ip = '172.16.120.5'
server_port = 5555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
 
# Main game loop
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                client_socket.close()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                coordinates = event.pos
                client_socket.sendall(pickle.dumps(coordinates))
 
        screen.fill((255, 255, 255))
        pygame.display.flip()
        pygame.time.Clock().tick(60)
 
if __name__ == "__main__":
    game_loop()