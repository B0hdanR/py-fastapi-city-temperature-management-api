import httpx


async def get_lat_and_lon(city_name: str) -> tuple[float, float]:
    url = "https://nominatim.openstreetmap.org/search"

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            params={"q": city_name, "format": "json"},
            headers={"User-Agent": "fastapi-weather-app"},
        )

    data = response.json()

    if not data:
        raise ValueError(f"City {city_name} not found")

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])

    return lat, lon
