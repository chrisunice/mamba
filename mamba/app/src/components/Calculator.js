import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles({
    root: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: "space-evenly",
        border: '1px solid black',
        width: '50%',
        height: '100%',
        margin: 10
    },
    leftContainer: {
        display: "flex",
        flexDirection: "column",
        textAlign: "left"
    }
});

const Calculator = () => {
    const classes = useStyles()
    return (
        <div className={classes.root}>
            <div className={classes.leftContainer}>
                <label>Address</label>
                <label>City</label>
                <label>State</label>
                <label>Zipcode</label>
                <label>Fair Market Value</label>
                <label>Fair Market Rent</label>
                <label>Profit</label>
                <label htmlFor="">Loan Term</label>
                <label htmlFor="">Interest Rate</label>
                <label htmlFor="">Down Payment</label>
            </div>
            <div>
                <input type="text"/>
            </div>

        </div>
    );
};

export default Calculator;