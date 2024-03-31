import React, { useState, useEffect } from 'react';
import { DyFunnel } from 'dynamochart';
import axios from 'axios';
import { useSelector } from 'react-redux';
import { selectFilter } from './features/appSlice';
import './FunnelGraph.css';

const FunnelGraph = () => {
  const [loading, setLoading] = useState(true);
  const filter = useSelector(selectFilter);
  const [data, setData] = useState([]);

  const fetchData = async () => {
    try {
      if (filter) {
        const response = await axios.get('http://127.0.0.1:8000/query', {
          params: {
            username:'vaibhav',
            password:'vaibhav721',
            State: filter.State,
            Gender: filter.Gender,
            County: filter.County,
          }
        });
        const d = response.data;
        console.log("vaibhav is lazy");
        console.log(d.Under5yrsPopulation);
        setData([
          { name: '<5', values: { '<5': d.Under5yrsPopulation } },
          { name: '5-17', values: { '5-17': d.t5to17yrs } },
          { name: '18-24', values: { '18-24': d.t18to24yrs } },
          { name: '25-34', values: { '25-34': d.t25to34years } },
          { name: '35-44', values: { '35-44': d.t35to44yrs } },
          { name: '45-64', values: { '45-64': d.t45to64yrs } },
          { name: '65-84', values: { '65-84': d.t65to84yrs } },
          { name: '85-99', values: { '85-99': d.t85to99yrs } },
          { name: '>100', values: { '>100': d.t100yrs_and_over } },
        ]);
        console.log(response);
        console.log(data);
        if (loading)
          setLoading(false);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
      alert("No Data Found for this "+filter.State +", "+filter.County+" and "+filter.Gender);
      setLoading(false);
    }
  };

  const handleGoButtonClick = () => {
    fetchData();
    setLoading(true);
  };

  if (loading) {
    return (
      <div className="button-container">
      <button onClick={handleGoButtonClick}>Go</button>
      <br />
      <h2>Please select all filters</h2>
    </div>
    );
  }

  const colors = [
    {
      '<5': '#ccebff',
      '5-17': '#99d6ff',
      '18-24': '#66c2ff',
      '25-34': '#33adff',
      '35-44': '#0099ff',
      '45-64': '#007acc',
      '65-84': '#005c99',
      '85-99': '#003d66',
      '>100': '#001f33'
    }
  ];

  return (
    <div className="funnel-container">
       <div className="button-container">
      <button onClick={handleGoButtonClick}>Reset</button>
      </div>
      <div className="chart-wrapper">
        <div className="chart-heading">Population Funnel Chart</div>
        <div className="chart-content">
          <DyFunnel
            data={data}
            colors={colors}
            showLegend={false}
            funnelValues={false}
            chartWidth={800}
            chartHeight={420}
            chartDecimals={0}
            chartTemplate="t1"
          />
        </div>
      </div>
    </div>
  );
};

export default FunnelGraph;
