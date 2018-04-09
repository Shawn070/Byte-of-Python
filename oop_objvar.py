# coding=UTF-8

class Robot:
    """a robot with name"""
    # read it by Robot.__doc__

    population = 0
    # population is a Class Variable

    def __init__(self, name):
        '''initialize data'''
        self.name = name
        # show is a Object Variable

        print('(Initializing {})'.format(self.name))
        Robot.population += 1
        # Robot.population = self.__class__.population

    def die(self):
        '''destroy a robot'''
        # show it by Robot.say_hi.__doc__
        print('{} is being deatroyed!'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print('There are still {:d} robots working.'\
                    .format(Robot.population))
    
    def say_hi(self):
        print('Greetings, my master call me {}.'\
                .format(self.name))

    @classmethod
    def how_many(cls):
        print('We have {:d} robots.'.format(cls.population))
    # how_many = classmethod(how_many)

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

print('\nRobots can do some work here!\n')

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
