var stripe = Stripe('');
var elem = document.getElementById("submit");
clientsecret = elem.getAttribute("data-secret");

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
var style = {
  base: {
    color: "#000",
    lineHeight: "2.4",
    fontSize: "16px",
  },
};

