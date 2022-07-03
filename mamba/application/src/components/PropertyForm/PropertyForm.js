import React, {Component} from 'react';
import Accordion from "react-bootstrap/Accordion";
import InformationSection from "./InformationSection";
import FinancialSection from "./FinancialSection";

const containerStyle = {
    display: 'flex',
    justifyContent: 'center',
    padding: '10px'
}


class PropertyForm extends Component {
    render() {
        return (
            <div id={"form-container"} style={containerStyle}>
                <form>
                    <fieldset>
                        <fieldset>
                            <Accordion>
                                <Accordion.Item>
                                    <Accordion.Header>
                                        <legend>Property Information</legend>
                                    </Accordion.Header>
                                    <Accordion.Body>
                                        <InformationSection/>
                                    </Accordion.Body>
                                </Accordion.Item>
                            </Accordion>
                            <FinancialSection/>
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