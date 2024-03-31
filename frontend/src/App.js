import React, { useState, useEffect } from 'react';
import FilterDropdown from './FilterDropdown';
import FunnelGraph from './FunnelGraph.js';
import states from './states.json';
import { selectFilter } from './features/appSlice';
import { useSelector } from 'react-redux';
import axios from 'axios';
import './App.css';

const genders = ['Male', 'Female'];
function App() {
  const [counties,setCounties] = useState([]);
  const filter = useSelector(selectFilter);
  useEffect(() => {
    const fetchData = async () => {
      try {
        //basic authentication implemented for each request from REACT to Django
        if(filter && filter.State)
        {
        const response = await axios.get('http://127.0.0.1:8000/countyList', {
          params: {
            username: 'vaibhav',
            password: 'vaibhav721',
            State: filter.State,
          }
        });;
        var d = response.data;
        setCounties(d);
      }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
  
    fetchData();
  }, [filter]);
  return (
    <div className="app-container">
      <h1 className="app-title">Population Analysis</h1>
      <div className="filters-container">
        <FilterDropdown options={genders} filterType="Gender" className="dropdown" />
        <FilterDropdown options={states.sort()} filterType="State" className="dropdown" />
        <FilterDropdown options={counties} filterType="County" className="dropdown" />
      </div>
      <div className="graph-container">
        <FunnelGraph />
      </div>
    </div>
  );
}

export default App;
