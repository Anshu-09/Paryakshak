//add logs
struct Incident {
    string description;
    uint256 timestamp;
}

mapping(address => Incident[]) public incidents;

event IncidentLogged(address indexed tourist, string description, uint256 timestamp);

function logIncident(string memory _description) public {
    require(tourists[msg.sender].registered, "Not registered");
    incidents[msg.sender].push(Incident(_description, block.timestamp));
    emit IncidentLogged(msg.sender, _description, block.timestamp);
}
