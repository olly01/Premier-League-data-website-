import React, {useState, useEffect} from 'react';
import api from "../api.js";
import SearchTeamForm from './searchTeamForm.jsx';
import DropdownMenu from './dropdownMenu.jsx';
const FixtureList = () => {
    const[fixtures, setFixtures] = useState([]);

    const fetchFixtures = async(teamName) => { 
        try{
            const response = await api.get(`/team/${encodeURIComponent(teamName)}`);
            setFixtures(response.data);
        }
        catch(error){
            console.error("Error fetching fixtures", error)
        }
    }

    
    return (
        <div>
            <h2>
                Fixture List
            </h2>
            <DropdownMenu fetchFixtures={fetchFixtures} />
            <table>
                <thead>
                <tr><th>Team</th><th>Opponent</th></tr>
                </thead>
                <tbody>
                {fixtures.map((fixture, index) =>
                    <tr key ={index}> 
                    <td>{fixture.Team}</td>
                    <td>{fixture.Opponent}</td>
                    <td>{fixture.Venue}</td>
                    <td>{fixture.Date}</td>
                    </tr>
                )}
                </tbody>
            </table>
            
        </div>
    )
}
export default FixtureList;