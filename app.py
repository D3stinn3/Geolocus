import folium

# Create a map of the world
base_map = folium.Map()
base_map_type = print(type(base_map))

# Save a map in html
creator_map = base_map.save('basemap.html')




