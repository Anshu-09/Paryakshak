//contract define
pragma solidity ^0.8.0;

contract TouristSafety {

    struct Tourist {
        string name;
        string passport;
        string nationality;
        string itinerary;
        bool registered;
    }

    mapping(address => Tourist) public tourists;
    event TouristRegistered(address indexed tourist, string name);
}
