//registeration function
function registerTourist(
    string memory _name,
    string memory _passport,
    string memory _nationality,
    string memory _itinerary
) public {
    require(!tourists[msg.sender].registered, "Already registered");
    tourists[msg.sender] = Tourist(_name, _passport, _nationality, _itinerary, true);
    emit TouristRegistered(msg.sender, _name);
}
