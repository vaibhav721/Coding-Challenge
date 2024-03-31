import React from 'react';
import { useDispatch } from 'react-redux';
import { setFilterInfo } from './features/appSlice';
import './FunnelGraph.css'; // Import CSS file for FilterDropdown styles

const FilterDropdown = ({ options, filterType }) => {
  const dispatch = useDispatch();

  const handleChange = (e) => {
    dispatch(
      setFilterInfo({
        [filterType]: e.target.value,
      })
    )
  };

  return (
    <select className="filter-dropdown" onChange={handleChange}>
      <option value="">Select {filterType}</option>
      {options.map(option => (
        <option key={option} value={option}>{option}</option>
      ))}
    </select>
  );
};

export default FilterDropdown;
