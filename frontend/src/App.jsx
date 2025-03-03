// src/App.jsx
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import DonationForm from './components/DonationForm';
import DonationConfirmation from './components/DonationConfirmation';
import UserDashboard from './components/UserDashboard';
import AdminDashboard from './components/AdminDashboard';
import PaymentInstructions from './components/PaymentInstructions';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/donate" element={<DonationForm />} />
        <Route path="/confirmation" element={<DonationConfirmation />} />
        <Route path="/dashboard" element={<UserDashboard />} />
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/payment-instructions" element={<PaymentInstructions />} />
      </Routes>
    </Router>
  );
}

export default App;
