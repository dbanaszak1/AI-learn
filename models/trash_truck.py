import pygame
import os
from coordinates import Coordinates, check_collision, Directions, SQUARE_SIZE, WIDTH, HEIGHT
import asyncio
from utils.utils import move_direction, check_flip, calc_rotation, a_star_search
from gui.grid_one import get_road_type
from joblib import load
import pandas as pd


current_directory = os.getcwd()
PATH_TO_TRASH_TRUCK_IMAGE = os.path.join(current_directory, "assets", "images", "trash-truck.png")
COLLECTION_ORDER = ("BIO", "Plastic", "Paper", "Glass", "Mixed")

model = load('decison_tree/decision_tree_model.joblib')
label_encoders = load('decison_tree/label_encoders.joblib')


class TrashTruck:
    def __init__(self, size, coordinates: Coordinates, weather, temp, season):
        self.original_image = pygame.image.load(PATH_TO_TRASH_TRUCK_IMAGE)
        self.image = pygame.transform.scale(self.original_image, size)
        self.coordinates = coordinates
        self.size = size
        self.rotation = calc_rotation(self.coordinates.direction)
        self.flip = check_flip(self.coordinates.direction)
        self.trash_type = "BIO"
        self.capacity = 0
        self.maxCapacity = 400
        self.weather = weather
        self.temp = temp
        self.season = season

    async def move(self, key_pressed, houses):
        directions = {
            # Key_Pressed : ( Coordinates, Rotation, Flip)
            pygame.K_LEFT: (self.coordinates.rotate_left()),
            pygame.K_RIGHT: (self.coordinates.rotate_right()),
            pygame.K_UP: (self.coordinates.move_forward()),
        }

        for key, (coordinates) in directions.items():
            if key_pressed[key]:
                if not check_collision(truck_coordinates=coordinates, houses=houses):
                    self.coordinates = coordinates
                    self.rotation = calc_rotation(self.coordinates.direction)
                    self.flip = check_flip(self.coordinates.direction)
                    await asyncio.sleep(0.15)
                    break

    async def follow_path(self, houses, drawWindow):
        count = 1
        for house in houses:
            print("destination: house", count)
            path = a_star_search(self.coordinates, house.coordinates)
            if path:
                for next_move in path:
                    self.coordinates = move_direction(self.coordinates, next_move)
                    self.rotation = calc_rotation(self.coordinates.direction)
                    self.flip = check_flip(self.coordinates.direction)
                    await asyncio.sleep(0.075)
                    drawWindow()
            count += 1
            await self.collect_trash_at_house(house)
            await asyncio.sleep(0.15)

    def check_capacity(self, trash_capacity):
        if self.capacity + trash_capacity <= self.maxCapacity :
            return 1
        else:
            return 0

    async def makedecision(self, last_pickup, space_in_truck, can_pickup_available, can_cap):
        data = {
            'weather': self.weather,
            'season': self.season,
            'last_pickup': last_pickup,
            'space_in_truck': space_in_truck,
            'trash_type': self.trash_type,
            'temp': self.temp,
            'can_pickup_avilable': can_pickup_available,
            'can_actual_capacity': can_cap
        }
        encoded_data = {}
        for column, value in data.items():
            if column in label_encoders:
                encoded_value = label_encoders[column].transform([value])[0]
            else:
                encoded_value = value
            encoded_data[column] = encoded_value

        # encoded_data to DataFrame convert
        encoded_data_df = pd.DataFrame([encoded_data])
        prediction = model.predict(encoded_data_df)
        if(prediction[0] == 1):
            print("TAKE")
        else:
            print("GO NEXT")
        return prediction[0]

    async def collect_trash_at_house(self, house):
        for trash_can, coords in house.trash_cans.items():
            if trash_can.expected_trash == self.trash_type:
                check_capacity = self.check_capacity(trash_can.capacity)
                weather = self.weather
                season = self.season
                temp = self.temp
                trash = self.trash_type
                if await self.makedecision(trash_can.lastPickup, check_capacity, 1, trash_can.capacity) == 1:
                    self.capacity = self.capacity + trash_can.capacity
                    trash_can.pickup()
                    self.collect_trash(trash_can)
                    break

    def collect_trash(self, trash_can):
        self.capacity += trash_can.capacity
        trash_can.capacity = 0
        trash_can.lastPickup = 0

    def draw(self, window):
        if not self.flip:
            rotated_image = pygame.transform.rotate(self.original_image, self.rotation)
            scaled_image = pygame.transform.scale(rotated_image, self.size)
        else:
            flipped_image = pygame.transform.flip(self.original_image, True, False)
            scaled_image = pygame.transform.scale(flipped_image, self.size)

        window.blit(scaled_image, (self.coordinates.x, self.coordinates.y))
