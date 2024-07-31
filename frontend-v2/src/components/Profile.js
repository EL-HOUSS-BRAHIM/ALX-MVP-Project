// src/components/Profile.js

import React from 'react';
import AuthService from '../services/AuthService';
import { useNavigate } from 'react-router-dom';

function Profile() {
    const navigate = useNavigate();
    const currentUser = AuthService.getCurrentUser();

    const handleLogout = () => {
        AuthService.logout();
        navigate('/login');
    };

    return (
        <div className="auth-wrapper">
            <div className="auth-inner">
                <h3>Profile</h3>
                {currentUser ? (
                    <div>
                        <p><strong>Name:</strong> {currentUser.name}</p>
                        <p><strong>Email:</strong> {currentUser.email}</p>
                        <button onClick={handleLogout} className="btn btn-primary btn-block">
                            Logout
                        </button>
                    </div>
                ) : (
                    <div>
                        <p>Please log in to view your profile.</p>
                    </div>
                )}
            </div>
        </div>
    );
}

export default Profile;
