
// React Code:
```
import React from 'react';
import './HolidayOffer.css';

function HolidayOffer() {
  return (
    <div className="holiday-offer">
      <div className="banner">
        <h1>Holiday Offer</h1>
        <p>Now up to 50% OFF! & ovy @ Xu</p>
      </div>
      <div className="fashion-38-home">
        <h2>Fashion 38 Home</h2>
        <p>About Services</p>
        <ul>
          <li>Element 1</li>
          <li>Element 2</li>
          <li>Element 3</li>
          <li>Extra Pages ~ Contact Q</li>
        </ul>
      </div>
      <div className="extraordinary-with-website">
        <h3>Embrace the Extraordinary with Website</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vitae ultricies leo integer malesuada tempor orci dapibus ultries diam in arcu cursus euismod purus viverra accumsan.</p>
        <button className="btn">Learn More</button>
      </div>
      <div className="top-brands">
        <h3>Top Brands</h3>
        <ul>
          <li>Brand 1</li>
          <li>Brand 2</li>
          <li>Brand 3</li>
          <li>High Quality Free Delivery</li>
        </ul>
      </div>
      <div className="brands-collection">
        <h3>Brands Collection Luxury Redefined Every Order</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vitae ultricies leo integer malesuada tempor orci dapibus ultries diam in arcu cursus euismod purus viverra accumsan.</p>
      </div>
    </div>
  );
}

export default HolidayOffer;
```
// CSS Code:
```
.holiday-offer {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
}

.banner {
  background-color: #f1c40f;
  padding: 20px;
}

.banner h1 {
  font-size: 36px;
  margin: 0;
}

.banner p {
  font-size: 18px;
  color: #777;
  margin-bottom: 20px;
}

.fashion-38-home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.fashion-38-home h2 {
  font-size: 24px;
  margin-bottom: 15px;
}

.fashion-38-home ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.fashion-38-home li {
  font-size: 18px;
  color: #777;
  margin-bottom: 15px;
}

.extraordinary-with-website {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.extraordinary-with-website h3 {
  font-size: 24px;
  margin-bottom: 15px;
}

.extraordinary-with-website p {
  font-size: 18px;
  color: #777;
  margin-bottom: 20px;
}

.extraordinary-with-website button {
  background-color: #f1c40f;
  border: none;
  padding: 10px 20px;
  font-size: 18px;
  color: #fff;
  cursor: pointer;
}

.top-brands {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.top-brands h3 {
  font-size: 24px;
  margin-bottom: 15px;
}

.top-brands ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.top-brands li {
  font-size: 18px;
  color: #777;
  margin-bottom: 15px;
}

.brands-collection {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.brands-collection h3 {
  font-size: 24px;
  margin-bottom: 15px;
}

.brands-collection p {
  font-size: 18px;
  color: #777;
  margin-bottom: 20px;
}
```