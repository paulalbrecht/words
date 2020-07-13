import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

class App extends Component {
  
 state = {
    recommendations: []
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:8000/recommendations/api/v1/count/3/`)
      .then(res => {
        const recommendations = res.data.results;
        this.setState({ recommendations });
      })
  }

  render() {
    return (
      <div className="App">
        <p className="App-intro">
            <h2>Grab list of books from the API and display it</h2>

      <ul>
        { this.state.recommendations.map(recommendation => <li>{recommendations.title}</li>)}
      </ul>
        </p>
      </div>
    );
  }
}

export default App;
