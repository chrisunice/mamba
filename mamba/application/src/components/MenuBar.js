import React, {Component} from 'react';
import Navbar from 'react-bootstrap/Navbar';

const navbarStyle = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '0px'
}

const titleStyle = {
    color: 'white',
    margin: '0px'
}

class MenuBar extends Component {
    render() {
        return (
            <div>
                <Navbar
                    id={"navbar"}
                    className="navbar navbar-expand-lg navbar-dark bg-primary"
                    style={navbarStyle}
                >
                    <img src={require("../logo.png")} alt="image" height={'75px'}/>
                    <h1 id={"title"} style={titleStyle}>Unice Properties</h1>
                </Navbar>
            </div>
        );
    }
}


export default MenuBar;