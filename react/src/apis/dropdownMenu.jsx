import React, {useState, useEffect} from 'react';
import api from "../api.js";



const DropdownMenu = ({fetchFixtures}) => {

    const[teams, setTeams] = useState([]);

    const[selectedTeam, setSelected] = useState('')


    const fetchTeams= async() => {

        try{
            const response = await api.get('/allteams');
            setTeams(response.data);

        }
        catch(error){
            console.error("Error fetching teams", error)
        }
    }
    useEffect(() =>{
        fetchTeams();
    },[])

    return(
        <>
        <label htmlFor ="team">Choose a team</label>
        <select name = "team" id = "team" onSelect-{(e) => {setSelected(e.target.value); fetchFixtures(e.target.value)}}onChange={(e) => {setSelected(e.target.value); fetchFixtures(e.target.value)}} value = {selectedTeam} > 
        {teams.map((team) =>
            <option key = {team} value = {team}>{team}</option>
        )}
        </select>       
        </>
    )
}
export default DropdownMenu;