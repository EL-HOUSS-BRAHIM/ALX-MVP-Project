const accessKey = 'upXjo3d9E_TFYbGxPDea8yJPNeRO1l72nVxDwUQy2Bs'; // Replace with your Unsplash API access key
    const heroImageElement = document.querySelector('.hero-image');
    const aboutImageElement = document.querySelector('.about-image');
    const userAvatarElement = document.querySelectorAll('.user-info img')[0];
    const userBvatarElement = document.querySelectorAll('.user-info img')[1];

    let heroImageInterval, aboutImageInterval, userAvatarInterval, userBvatarInterval;

    // Function to fetch and update the hero image
    function updateHeroImage() {
      fetch(`https://api.unsplash.com/photos/random?query=finance&orientation=landscape&client_id=${accessKey}`)
        .then(response => response.json())
        .then(data => {
          heroImageElement.src = data.urls.regular;
        })
        .catch(error => console.error('Error fetching hero image:', error));
    }

    // Function to fetch and update the about image
    function updateAboutImage() {
      fetch(`https://api.unsplash.com/photos/random?query=business&orientation=landscape&client_id=${accessKey}`)
        .then(response => response.json())
        .then(data => {
          aboutImageElement.src = data.urls.regular;
        })
        .catch(error => console.error('Error fetching about image:', error));
    }

    // Function to fetch and update the user avatars
    function updateUserAvatars() {
      fetch(`https://api.unsplash.com/photos/random?query=portrait&client_id=${accessKey}`)
        .then(response => response.json())
        .then(data => {
          userAvatarElement.src = data.urls.thumb;
        })
        .catch(error => console.error('Error fetching user avatar:', error));

      fetch(`https://api.unsplash.com/photos/random?query=portrait&client_id=${accessKey}`)
        .then(response => response.json())
        .then(data => {
          userBvatarElement.src = data.urls.thumb;
        })
        .catch(error => console.error('Error fetching user avatar:', error));
    }

    // Initial image fetch
    updateHeroImage();
    updateAboutImage();
    updateUserAvatars();

    // Refresh images every 10 seconds (10000 milliseconds)
    heroImageInterval = setInterval(updateHeroImage, 900000);
    aboutImageInterval = setInterval(updateAboutImage, 900000);
    userAvatarInterval = setInterval(updateUserAvatars, 900000);

    // Stop refreshing images when you find the desired image
    heroImageElement.addEventListener('click', () => {
      clearInterval(heroImageInterval);
    });

    aboutImageElement.addEventListener('click', () => {
      clearInterval(aboutImageInterval);
    });

    userAvatarElement.addEventListener('click', () => {
      clearInterval(userAvatarInterval);
    });

    userBvatarElement.addEventListener('click', () => {
      clearInterval(userAvatarInterval);
    });