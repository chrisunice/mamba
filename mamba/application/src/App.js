import './App.css';
import Button from 'react-bootstrap/Button';
import Navbar from "react-bootstrap/Navbar";

function App() {
  return (
    <div className="App">

        <div>
            <Navbar className={"navbar navbar-expand-lg navbar-dark bg-primary"} style={{display: 'flex', justifyContent: 'center'}}>
                <h1 style={{color: 'white'}}>This is my title</h1>
            </Navbar>
        </div>
        <div>
            <Button className={"btn btn-info"}>Primary</Button>
        </div>

    </div>
  );
}

export default App;
