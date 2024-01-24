import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Contacts from './pages/Contacts/Contacts';
import AboutUs from './pages/AboutUs/AboutUs';
import Sources from './pages/Sources/Sources';
import Weather from './pages/Weather/Weather';
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
        <Route path="/tempo" element={<Weather />} />
        <Route path="/contactos" element={<Contacts />} />
        <Route path="/sobre" element={<AboutUs />} />
        <Route path="/fontes" element={<Sources />} />
        <Route path="*" element={<h1>Not Found</h1>} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
