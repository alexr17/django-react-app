import React, { Component } from 'react';
import reactLogo from './logo-react.svg';
import djangoLogo from './logo-django.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={reactLogo} className="App-logo" alt="React logo" />
          <img src={djangoLogo} className="App-logo" alt="Django logo" />
          <h1 className="App-title">Welcome to django-react-app!</h1>
        </header>
      </div>
    );
  }
}

export default App;
