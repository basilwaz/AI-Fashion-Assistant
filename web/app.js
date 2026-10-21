const form = document.querySelector('#preferences');
const status = document.querySelector('#status');
const results = document.querySelector('#results');
const button = form.querySelector('button');
const dollars = cents => (cents / 100).toLocaleString('en-US', {style: 'currency', currency: 'USD'});

function outfitCard(outfit) {
  const article = document.createElement('article');
  const heading = document.createElement('h2');
  heading.textContent = `${outfit.name}: ${dollars(outfit.total_cents)}`;
  const list = document.createElement('ul');
  outfit.items.forEach(item => {
    const row = document.createElement('li');
    row.textContent = `${item.name} (${item.brand}): ${dollars(item.price_cents)}`;
    list.append(row);
  });
  article.append(heading, list);
  return article;
}

form.addEventListener('submit', async event => {
  event.preventDefault();
  button.disabled = true;
  results.replaceChildren();
  status.textContent = 'Finding matching outfits...';
  try {
    const query = new URLSearchParams(new FormData(form));
    const response = await fetch(`/api/recommend?${query}`);
    const data = await response.json();
    if (!response.ok) throw new Error(data.error);
    status.textContent = `${data.outfits.length} matching outfits. Try a larger budget or different preferences if none match.`;
    results.replaceChildren(...data.outfits.map(outfitCard));
  } catch (error) {
    status.textContent = error.message || 'Could not load outfits. Check that the Python server is running.';
  } finally {
    button.disabled = false;
  }
});
