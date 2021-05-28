class dog:

    animal = 'dog'

    def __init__(self,breed,color):
        self.breed = breed
        self.color = color


    def display(self):
        return self.breed,self.color
        


puf = dog('puf','brown')
hutch = dog('hutch','white')

print(puf.display())
print(hutch.display())
#print('all of these animals have a type',dog.animal)
