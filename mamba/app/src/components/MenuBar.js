import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { FaBars } from "react-icons/fa";

const useStyles = makeStyles({
  menuContainer: {
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    width: '100%',
    backgroundColor: '#29b6f6ff',
  },
  menuBars: {
    fontSize: 'xx-large',
    margin: 10,
    color: "black",
  },
  menuTitle: {}
});

const MenuBar = () => {
  const classes = useStyles();
  return (
    <div className={classes.menuContainer}>
      <FaBars className={classes.menuBars} />
      <h3>Traditional Purchase Calculator</h3>
      {/*<FaBars className={classes.menuBars} onClick={showSidebar}/>*/}
    </div>
  );
}

export default MenuBar;