import React, {Component} from 'react';
import './PropertyForm.css';


class FinancialSection extends Component {
    render() {
        return (
            <div id="financial-section">

                <div id="row-1" className="form-row" style={{justifyContent: 'center'}}>
                    <label htmlFor="fairMarketValue">Fair Market Value</label>
                    <span className="input-group-text">$</span>
                    <input type="number" className="form-control" id={"fairMarketValue"} style={{width: '50%'}}/>
                </div>

                <div id="row-2" className="form-row" style={{justifyContent: 'center'}}>
                    <label htmlFor="fairMarketRent">Fair Market Rent</label>
                    <span className="input-group-text">$</span>
                    <input type="number" className="form-control" id={"fairMarketRent"} style={{width: '50%'}}/>
                </div>

            </div>
        );
    }
}

export default FinancialSection;