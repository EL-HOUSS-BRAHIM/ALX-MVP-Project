import { Helmet } from "react-helmet";
import "../styles/contact.css";

const Contact = () => {
  return (
    <div className="contact-container">
      <Helmet>
        <title>Budget Management App - Contact</title>
        <meta
          name="description"
          content="Get in touch with us for support or inquiries."
        />
      </Helmet>
      <h1>Contact Us</h1>
      <form>
        <label>
          Name:
          <input type="text" placeholder="Your name" />
        </label>
        <label>
          Email:
          <input type="email" placeholder="Your email" />
        </label>
        <label>
          Message:
          <textarea placeholder="Your message"></textarea>
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Contact;