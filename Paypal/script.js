// Get the input elements
const amountInput = document.getElementById('amount');
const currencySelect = document.getElementById('currency');
const billTypeButton = document.getElementById('bill-type-btn');

// Calculate the PayPal fee
function calculateFee() {
  const amount = parseFloat(amountInput.value);
  const currency = currencySelect.value;
  const feeRate = getFeeRate(currency);
  const fee = amount * feeRate;
  const total = amount + fee;
  const feeFormatted = formatCurrency(fee, currency);
  const totalFormatted = formatCurrency(total, currency);
  alert(`PayPal fee: ${feeFormatted}\nTotal amount: ${totalFormatted}`);
}

// Get the fee rate based on the currency
function getFeeRate(currency) {
  if (currency === 'USD') {
    return 0.029;
  } else if (currency === 'EUR') {
    return 0.035;
  } else {
    return 0.039;
  }
}

// Format the currency
function formatCurrency(amount, currency) {
  if (currency === 'USD') {
    return `$${amount.toFixed(2)}`;
  } else if (currency === 'EUR') {
    return `€${amount.toFixed(2)}`;
  } else {
    return `${amount.toFixed(2)} ${currency}`;
  }
}

// Show the popup window for selecting the bill type
billTypeButton.addEventListener('click', () => {
  const billType = prompt('What type of bill is this?');
  alert(`You selected ${billType} as the bill type.`);
});
