from subject import Subject


class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, observer):
        '''If need to register observer, just add it to observers list
        '''
        self.observers.append(observer)

    def remove_observer(self, observer):
        '''The same, if observer wants to unregister, we will remove
        him from observer list.'''
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        '''We sent statement to every observers. Since all observers
         implement update() method, we know how to notify them.'''
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changes(self):
        '''We need to notify observers when we get measurements from
        Weather-O-Rama company.'''
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        '''We will use this method to test billboard.'''
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changes()

    # Other methods in WeatherData