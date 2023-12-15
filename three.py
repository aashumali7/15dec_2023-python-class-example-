class A:
    #property
    bloodGroup = ''

    # Constructor
    def __init__(self, x):
        self.bloodGroup = x

    # Method
    def displayBloodGroup(self):
        print(f'Blood group is {self.bloodGroup}')

# Create classobject
co = A('Ab+')
# Call the method from class A
co.displayBloodGroup()
