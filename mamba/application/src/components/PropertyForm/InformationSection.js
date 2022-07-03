import React, {Component} from 'react';

const sectionStyle = {
    display: 'flex',
    flexDirection: 'column',
    border: '0.5px solid black',
    borderRadius: '10px',
    padding: '25px'
}

class InformationSection extends Component {
    render() {
        return (
            <div id="information-section" style={sectionStyle}>
                <div id="row-1" className="form-row">
                    <div style={{width: '70%'}}>
                        <label htmlFor="streetAddress">Street Address</label>
                        <input type="text" className="form-control" id={"streetAddress"}/>
                    </div>
                    <div style={{width:'20%'}}>
                        <label htmlFor="unitNumber">Unit Number</label>
                        <input type="number" className="form-control" id={"unitNumber"}/>
                    </div>
                </div>

                <div id="row-2" className="form-row">
                    <div style={{width: '50%'}}>
                        <label htmlFor="city">City</label>
                        <input type="text" className="form-control" id={"city"}/>
                    </div>
                    <div style={{width: '20%'}}>
                        <label htmlFor="state">State</label>
                        <input type="text" className="form-control" id={"state"}/>
                    </div>
                    <div style={{width: '20%'}}>
                        <label htmlFor="zipcode">Zipcode</label>
                        <input type="number" className="form-control" id={"zipcode"}/>
                    </div>
                </div>

                <div id="row-3" className="form-row" style={{justifyContent: 'center'}}>
                    <label htmlFor="listPrice">Listing Price</label>
                    <span className="input-group-text">$</span>
                    <input type="number" className="form-control" id={"listPrice"} style={{width: '50%'}}/>
                </div>

            </div>
        );
    }
}

export default InformationSection;