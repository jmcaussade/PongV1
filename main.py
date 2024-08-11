import pygame

from duplicate_ball_mode import duplicate_ball_mode
from increase_velocity_mode import increase_speed_mode
from obstacle_mode import obstacle_mode
from menu import menu


pygame.init()


def main():
    while True:
        game_mode, points_limit = menu()
        if not game_mode:
            break

        if game_mode == "increase_speed_pvp":
            increase_speed_mode(points_limit, player_vs_computer=False)
        elif game_mode == "increase_speed_pvc":
            increase_speed_mode(points_limit, player_vs_computer=True)
        elif game_mode == "duplicate_ball_pvp":
            duplicate_ball_mode(points_limit, player_vs_computer=False)
        elif game_mode == "duplicate_ball_pvc":
            duplicate_ball_mode(points_limit, player_vs_computer=True)
        elif game_mode == "obstacle_pvp":
            obstacle_mode(player_vs_computer=False)
        elif game_mode == "obstacle_pvc":
            obstacle_mode(points_limit, player_vs_computer=True)
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
