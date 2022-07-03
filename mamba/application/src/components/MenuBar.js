import React, {Component} from 'react';
import Navbar from 'react-bootstrap/Navbar';

const navbarStyle = {
    display: 'flex',
    justifyContent: 'center',
}

const titleStyle = {
    color: 'white'
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
                    <h1
                        id={"title"}
                        style={titleStyle}
                    >
                        Unice Properties
                    </h1>
                </Navbar>
            </div>
        );
    }
}


export default MenuBar;