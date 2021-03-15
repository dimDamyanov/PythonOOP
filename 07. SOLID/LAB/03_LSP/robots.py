from abc import ABC, abstractmethod


class Robot(ABC):
    @abstractmethod
    def sensors_count(self):
        pass


class Android(Robot):
    def senzors_count(self):
        return 4


class Chappie(Robot):
    def senzors_count(self):
        return 6


def count_robot_senzors(robots: list):
    for robot in robots:
        print(robot.sensors_count())


robots = [Android(), Chappie()]
count_robot_senzors(robots)
