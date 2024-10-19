import orb as orb

def main():
    train = 'data/airPort.jpg'
    query = 'data/airportCrop.png'

    orb.orb_detect(train, query)


if __name__ == "__main__":
    main()
