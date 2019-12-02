import pygame


def scale(new_surface, old_surface, old_size, new_size):
    """ Scale a surface onto another without distortion with letterboxing"""
    x_scale = new_size[0] / old_size[0]
    y_scale = new_size[1] / old_size[1]

    # scale_factor = min(x_scale, y_scale)

    if x_scale < y_scale:
        scale_factor = x_scale
        x_offset = 0
        y_offset = 0
    else:
        scale_factor = y_scale
        x_offset = 0
        y_offset = 0

    new_surface.fill((0, 0, 0))
    new_surface.blit(pygame.transform.scale(
        old_surface,
        (int(scale_factor * old_size[0]), int(scale_factor * old_size[1]))),
        (x_offset, y_offset))
