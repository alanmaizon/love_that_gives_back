// src/components/PaymentInstructions.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

function PaymentInstructions() {
  const navigate = useNavigate();

  return (
    <div className="container mt-5">
      <h2>Manual Payment Instructions</h2>
      <p>
        Thank you for your donation. To complete your donation, please follow these manual payment instructions:
      </p>
      <ul>
        <li>Transfer the donation amount to the following bank account:</li>
        <li><strong>Bank:</strong> Example Bank</li>
        <li><strong>Account Number:</strong> 123456789</li>
        <li><strong>Routing Number:</strong> 987654321</li>
        <li><strong>Reference:</strong> Your Donation ID (provided in your confirmation email)</li>
      </ul>
      <p>
        Once your payment is received, your donation status will be updated. If you have any questions, please contact us.
      </p>
      <button className="btn btn-primary" onClick={() => navigate('/')}>
        Return Home
      </button>
    </div>
  );
}

export default PaymentInstructions;
