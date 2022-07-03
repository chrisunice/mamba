import React, {Component} from 'react';
import InformationSection from "./InformationSection";

const containerStyle = {
    display: 'flex',
    justifyContent: 'center',
    padding: '10px'
}

const formStyle = {
    width: '75%'
}

const legendStyle = {
    color: 'black',
    textAlign: 'left',
    fontSize: '2rem'
}


class PropertyForm extends Component {
    render() {
        return (
            <div id={"form-container"} style={containerStyle}>
                <form style={formStyle}>
                    <fieldset>
                        <fieldset>
                            <legend style={legendStyle}>Property Information</legend>
                            <InformationSection/>
                        </fieldset>
                        <div>
                            <button className="btn btn-outline-primary">Submit</button>
                            <button className="btn btn-outline-secondary">Reset</button>
                        </div>
                    </fieldset>
                </form>
            </div>
        );
    }
}

export default PropertyForm;