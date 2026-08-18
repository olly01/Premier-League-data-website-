import React, {useState} from 'react';

const SearchTeamForm = ({fetchFixtures}) => {
    const[teamName, setTeamName] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        if(teamName){
            fetchFixtures(teamName);
            setTeamName('');
        }
    }
    return(
        <form onSubmit={handleSubmit}>
            <input 
            type="text"
            value={teamName}
            onChange={(e) => setTeamName(e.target.value)}
            placeholder="Enter team name."
            />
            <button type="submit">Search team</button>
        </form>
    )

}
export default SearchTeamForm;