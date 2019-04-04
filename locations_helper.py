import pymysql
from trilateration import calculate_intersection

server = "majorproj.cgogalrvwv6s.ap-south-1.rds.amazonaws.com"
user = "admin"
password = "password"
db = "majordb"

query = "SELECT wd.id, wd.ssid, wd.distance, nl.latitude, nl.longitude FROM wifidata AS wd INNER JOIN node_location " \
        "AS nl ON wd.fk_location_id = nl.pk_location_id WHERE wd.rssi != 0 AND wd.id < 4"


def get_location_data():
    conn = pymysql.connect(host=server, user=user, password=password, database=db)

    response = dict()
    nodes = []
    position = dict()

    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall();

            for row in results:
                nodeData = dict()
                nodeData["id"] = row[0]
                nodeData["ssid"] = row[1]
                nodeData["distance"] = row[2]
                nodeData["latitude"] = row[3]
                nodeData["longitude"] = row[4]

                nodes.append(nodeData)

            lat, lng = calculate_intersection(nodes[0]["latitude"], nodes[0]["longitude"], nodes[0]["distance"],
                                              nodes[1]["latitude"], nodes[1]["longitude"], nodes[1]["distance"],
                                              nodes[2]["latitude"], nodes[2]["longitude"], nodes[2]["distance"])

            position = {"latitude": lat, "longitude": lng}

    finally:
        conn.close()

    response["ap_nodes"] = nodes
    response["position"] = position

    return response



