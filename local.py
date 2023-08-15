import folium

# Create a specific folium map
def main():
    cordinates_ = [1.2504, 36.9487]
    zoom = 9
    base_map = folium.Map(cordinates_, zoom_start=zoom)
    base_map.save('localmap.html')
    return "Map created successfully"

if __name__ == "__main__":
    main()