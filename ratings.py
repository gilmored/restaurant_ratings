import csv 

class RestaurantRating:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __repr__(self):
        return f"<RestaurantRating name={repr(self.name)} rating={repr(self.rating)}>"

    def __lt__(self, other):
        return self.rating < other.rating

    def update_rating(self, rating):
        self.rating = rating

class RestaurantRatings:
    def __init__(self, restaurants=None):
        self.ratings = restaurants or []

    def __repr__(self):
        return f"<RestaurantRatings ratings={repr(self.restaurants)}>"

    def add_rating(self, name, rating):
        """Create and add a new restaurant rating"""
        # TODO: Create a new RestaurantRating instance
        r = RestaurantRating(name, rating)
        # TODO: Add it to the list of ratings
        self.ratings.append(r)

    def remove_rating_by_index(self, index):
        """Remove a rating by its index"""
        #TODO: Remove the item from self.ratings at the given index
        self.ratings.pop(index)

    def remove_rating_by_name(self, name):
        """Remove a rating by its name"""
        # Loop through each item and index in self.ratings
        for i, rating in enumerate(self.ratings):
            # Find the item with the given name
            if rating.name == name:
                # Call self.remove_rating_by_index with the index
                self.remove_rating_by_index(i)
    def get_rating_by_name(self, name):
        """Get a rating by its name"""
        # TODO: Find the item with the given name and return it
        for rating in self.ratings:
            if rating.name == name:
                return rating

    def to_file(self, filename):
        """Write ratings to filename."""

        # Open filename in write mode
        with open(filename, "w") as f:
            # Create a CSV writer
            writer = csv.writer(f)

            # Loop over ratings and write data to CSV
            for r in self.ratings:
                writer.writerow([r.name, r.rating])

    @classmethod
    def from_file(cls, filename):
        """Read ratings from filename."""

        # TODO: Create a new RestaurantRatings instance
        ratings = cls()
        # TODO: Open filename in read mode
        with open(filename, "r") as f:
        # TODO: Create a CSV reader
            reader = csv.reader(f)
        # TODO: Loop over each row in the CSV file
            for row in reader: 
        # TODO: Add it to the list of ratings
                ratings.add_rating(name, int(rating))
        # TODO: Return the RestaurantRatings instance
        return r
