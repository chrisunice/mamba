import React, {Component} from 'react';

const containerStyle = {
    display: 'flex',
    justifyContent: 'center',
    padding: '10px'
}

const formStyle = {
    width: '75%'
}

const labelStyle = {
    textAlign: 'left'
}

class Form extends Component {
    render() {
        return (
            <div id={"form-container"} style={containerStyle}>
                <form style={formStyle}>
                    <fieldset>
                        <legend style={{textAlign: 'left'}}>Property Address</legend>
                        <div style={{display: 'flex', justifyContent: 'space-evenly', textAlign: 'left', border: '1px solid black'}}>
                            <div style={{width: '70%'}}>
                                <label
                                className={"col-form-label col-form-label-lg"}
                                htmlFor="propertyAddress"
                                style={labelStyle}
                                >
                                    Street Address
                                </label>
                                <input type="text" className="form-control" id={"propertyAddress"}/>
                            </div>
                            <div>
                                <label
                                    className={"col-form-label col-form-label-lg"}
                                    htmlFor="propertyAddress"
                                    style={labelStyle}
                                >
                                    Unit Number
                                </label>
                                <input type="text" className="form-control" id={"propertyAddress"}/>
                            </div>

                        </div>
                    </fieldset>
                </form>
            </div>
        );
    }
}

export default Form;