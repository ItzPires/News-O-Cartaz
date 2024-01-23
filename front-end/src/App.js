import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import NavBar from './components/NavBar/NavBar';
import Footer from './components/Footer/Footer';
import './App.css';
import './vendor.css';

function App() {
  return (
    <BrowserRouter>
    <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="*" element={<h1>Not Found</h1>} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
