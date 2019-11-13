import React, { Component } from "react";
import reactLogo from "./logo-react.svg";
import djangoLogo from "./logo-django.svg";
import "./styles/index.css";

class App extends Component {
  render() {
    return (
      <div className="bg-black h-screen">
        <header className="flex text-white flex-wrap justify-center pt-4">
          <img src={reactLogo} className="App-logo" alt="React logo" />
          <img src={djangoLogo} className="App-logo" alt="Django logo" />
          <h1 className="w-full text-center">Welcome to the Dealdock app</h1>
        </header>
      </div>
    );
  }
}

export default App;
