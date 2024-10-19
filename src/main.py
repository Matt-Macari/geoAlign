import orb as orb

def main():
    base = 'data/airPort.jpg'
    query = 'data/airportCrop.png'

    orb.orb_detect(base, query)


if __name__ == "__main__":
    main()
