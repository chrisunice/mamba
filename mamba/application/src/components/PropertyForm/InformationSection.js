import React, {Component} from 'react';

const sectionStyle = {
    display: 'flex',
    flexDirection: 'column',
    border: '0.5px solid black',
    borderRadius: '10px',
    padding: '25px'
}

const rowStyle = {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'space-between',
    textAlign: 'left',
    margin: '10px 0px 10px 0px'
}

const labelStyle = {
    color: 'black',
    textAlign: 'left',
    fontSize: '1.5rem',
    marginBottom: '10px'
}

class InformationSection extends Component {
    render() {
        return (
            <div style={sectionStyle}>

                <div className="row-1" style={rowStyle}>
                    <div style={{width: '70%'}}>
                        <label htmlFor="streetAddress" style={labelStyle}>Street Address</label>
                        <input type="text" className="form-control" id={"streetAddress"}/>
                    </div>
                    <div>
                        <label htmlFor="unitNumber" style={labelStyle}>Unit Number</label>
                        <input type="number" className="form-control" id={"unitNumber"}/>
                    </div>
                </div>

                <div className="row-2" style={rowStyle}>
                    <div style={{width: '50%'}}>
                        <label htmlFor="city" style={labelStyle}>City</label>
                        <input type="text" className="form-control" id={"city"}/>
                    </div>
                    <div>
                        <label htmlFor="state" style={labelStyle}>State</label>
                        <input type="text" className="form-control" id={"state"}/>
                    </div>
                    <div>
                        <label htmlFor="zipcode" style={labelStyle}>Zipcode</label>
                        <input type="number" className="form-control" id={"zipcode"}/>
                    </div>
                </div>
            </div>
        );
    }
}

export default InformationSection;