import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

class App extends Component {
  state = {
    recommendations: []
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/recommendations/api/v1/count/')
      .then(res => {
        const recommendations = res.data;
        this.setState({recommendations});
      })
  }

  handleSubmit = event => {
    event.preventDefault();
    const no_recommendations = {
      number: this.state.number
    }
    console.log('Number of recommendations');
    console.log(no_recommendations.number);
    console.log('http://127.0.0.1:8000/recommendations/api/v1/count/' + no_recommendations.number);
    axios.get('http://127.0.0.1:8000/recommendations/api/v1/count/' + no_recommendations.number + '/')
      .then(res => {
        const recommendations = res.data;
        this.setState({recommendations});
    })
  }

  handleChange = event =>{
    this.setState({ number: event.target.value});
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label> Number Of recommendations?:
            <input type="text" name="number" onChange={this.handleChange}/>
          </label>
          <button type="submit">Add</button>
        </form>

        <ul>
          { this.state.recommendations.map(recommendation => <li>{recommendation.title}</li>)}
        </ul>
      </div>
    )
  }
}
export default App;
