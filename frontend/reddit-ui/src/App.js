import { useActionState, useState } from "react";
import Header from "./components/Header/Header";
import SearchBar from "./components/SearchBar/SearchBar";

function App() {
  const[subRed, setSubRed] = useState('');
  const[term, setTerm] = useState('')
  const handleSubSearch = term => {
    setSubRed(term)
  }
  const handleSearch = term => {
    setTerm(term)
  }

  const handleSubmit = async () => {
    try {
      const res = await fetch('/sentiment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },  // JSON
        body: JSON.stringify({                            // correct keys
          subreddit: subRed,
          search_term: term,
        }),
        // mode: 'cors'  // you can omit this—'cors' is the default for cross‑origin fetches
      });
  
      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }
  
      const { results } = await res.json();
      console.log('Sentiment results:', results);
      // …store them in state, render them, etc.
    } catch (err) {
      console.error('Fetch failed:', err);
    }
  };
  
  return (
    <div className="App">
      <Header/>
      <SearchBar placeholder = "Please enter a subreddit "onSearch={handleSubSearch}/>
      <SearchBar placeholder = "Please enter a term "onSearch={handleSearch}/>
      <button onClick={handleSubmit}>Get Comments</button>
    </div>
  );
}

export default App;
