def top_grade(grades: dict[str, str | list[int]]) -> dict[str, int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}


print(*top_grade.__annotations__.values())
