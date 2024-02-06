import React from 'react';
import { HashRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Contacts from './pages/Contacts/Contacts';
import AboutUs from './pages/AboutUs/AboutUs';
import Sources from './pages/Sources/Sources';
import Weather from './pages/Weather/Weather';
import Category from './pages/Categorys/Category';
import NavBar from './components/NavBar/NavBar';
import Footer from './components/Footer/Footer';
import './App.css';
import './vendor.css';

function App() {
  return (
    <HashRouter>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/categoria/:id" element={<Category />} />
        <Route path="/source/:id" element={<Category source={true} />} />
        <Route path="/ultimas" element={<Category CategoryName="Últimas" latest={true} />} />
        <Route path="/pesquisa/:id" element={<Category CategoryName="Pesquisa" search={true} />} />
        <Route path="/tempo" element={<Weather />} />
        <Route path="/contactos" element={<Contacts />} />
        <Route path="/sobre" element={<AboutUs />} />
        <Route path="/fontes" element={<Sources />} />
        <Route path="*" element={<h1>Not Found</h1>} />
      </Routes>
      <Footer />
    </HashRouter>
  );
}

export default App;
