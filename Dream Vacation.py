# Dream Vacation

destination = "Where would your dream vacation be?"
destination += "\nType 'quit' to exit. "


prompt = ""
while prompt != 'quit':
    prompt = str(input(destination))
    print(f"\nWow! {prompt} sounds like it would be amazing!\n")