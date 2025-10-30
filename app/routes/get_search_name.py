from sqlalchemy import text
from flask_api import status
from resources.connections import engine, NAME_QUERY
from resources.cache import cache
from resources.api_decorator import api_endpoint


@api_endpoint()
@cache.cached()
def search_name(partial_name):
    try:
        results = []
        with engine.connect() as connection:
            # Prepare the query with the partial name
            query = text(NAME_QUERY.format(':partialName'))
            result = connection.execute(query, {'partialName': partial_name})

            # Collect results
            for row in result:
                data = {"idPatient": row[0], "name": row[1]}
                results.append(data)

        if results:
            return {
                "status": "success",
                "partial_name": partial_name,
                "results": results,
            }, status.HTTP_200_OK
        else:
            return {
                "status": "error",
                "partial_name": partial_name,
                "results": [],
                "message": "No matching records found",
            }, status.HTTP_404_NOT_FOUND
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }, status.HTTP_500_INTERNAL_SERVER_ERROR
