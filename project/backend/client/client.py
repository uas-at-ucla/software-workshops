import requests

correct_coords = [
    (147.0, 6.0),
    (-46.0, 9.0),
    (-33.0, 55.0),
    (40.0, -13.0),
    (57.0, -32.0),
    (-42.0, 30.0),
    (24.0, -20.0),
    (-1.0, 19.0)
]

def assert_coords_within_range(your_coords, correct_coords):
    tolerance = 10
    tests_passed = 0
    for i, (your_x, your_y) in enumerate(your_coords):
        correct_x, correct_y = correct_coords[i]

        if abs(your_x - correct_x) <= tolerance and abs(your_y - correct_y) <= tolerance:
            print(f"Image {i+1}: Coordinates are within the acceptable range.")
            tests_passed += 1

        if abs(your_x - correct_x) > tolerance:
            print(f"X coordinate for image {i+1} out of range: got {your_x}, expected {correct_x}")
        if abs(your_y - correct_y) > tolerance:
            print(f"Y coordinate for image {i+1} out of range: got {your_y}, expected {correct_y}")

    print(f"Tests passed: {tests_passed}/8")

def main():

    your_coords = []
    for i in range(1, 9):
        image_name = f"i{i}.jpg"

        # send a post request holding the image name to the server at /odlc endpoint
        response = requests.post('http://localhost:5000/odlc', json={'img_name': image_name})
        reponse_json = response.json()

        # get the coordinates from the response and save it in x_dist and y_dist
        x_dist = reponse_json['x_dist']
        y_dist = reponse_json['y_dist']

        # add the coordinates to the your_coords array
        your_coords.append((x_dist, y_dist))

    assert_coords_within_range(your_coords, correct_coords)


if __name__ == "__main__":
    main()