import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  filter: null

};
export const appSlice = createSlice({
  name: 'app',
  initialState,
  reducers: {
    setFilterInfo: (state, action) => {
        state.filter = { ...state.filter, ...action.payload };
    }
  },
});

export const { setFilterInfo } = appSlice.actions;

export const selectFilter = (state) => state.app.filter;

export default appSlice.reducer;