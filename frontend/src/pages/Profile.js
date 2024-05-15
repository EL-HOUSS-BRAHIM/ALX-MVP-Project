import React, { useEffect, useState } from 'react';
import { getUserProfile, updateUserProfile } from '../services/user.service';

const Profile = () => {
  const [userProfile, setUserProfile] = useState({});
  const [editMode, setEditMode] = useState(false);

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        const profile = await getUserProfile();
        setUserProfile(profile);
      } catch (error) {
        console.error('Failed to fetch user profile:', error);
      }
    };

    fetchUserProfile();
  }, []);

  const handleUpdateProfile = async (updatedProfile) => {
    try {
      await updateUserProfile(updatedProfile);
      setUserProfile(updatedProfile);
      setEditMode(false);
    } catch (error) {
      console.error('Failed to update user profile:', error);
    }
  };

  return (
    <div>
      <h1>User Profile</h1>
      {/* Render user profile details */}
      {/* Add edit functionality if editMode is true */}
      {editMode ? (
        // Render form to update user profile
        <form onSubmit={handleUpdateProfile}>
          {/* Form fields */}
          <button type="submit">Save Changes</button>
        </form>
      ) : (
        <button onClick={() => setEditMode(true)}>Edit Profile</button>
      )}
    </div>
  );
};

export default Profile;