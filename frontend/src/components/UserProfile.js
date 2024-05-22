import React, { useState, useEffect } from 'react';
import userService from '../services/user.service';
import '../styles/profile.css';

const UserProfile = () => {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      const data = await userService.getProfile();
      setProfile(data);
    };
    fetchProfile();
  }, []);

  return (
    <div className="user-profile">
      {profile ? (
        <>
          <h2>{profile.name}</h2>
          <p>Email: {profile.email}</p>
          <p>Joined: {new Date(profile.joined).toLocaleDateString()}</p>
        </>
      ) : (
        <p>Loading profile...</p>
      )}
    </div>
  );
};

export default UserProfile;
