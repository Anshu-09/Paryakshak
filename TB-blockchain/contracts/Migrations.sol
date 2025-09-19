//verf for dashboard
function verifyTourist(address _tourist) public view returns (string memory, string memory, string memory, string memory) {
    Tourist memory t = tourists[_tourist];
    require(t.registered, "Tourist not found");
    return (t.name, t.passport, t.nationality, t.itinerary);
}
