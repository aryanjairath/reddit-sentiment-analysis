import react, {useState} from "react";


const SearchBar = ({placeholder, onSearch }) => {
    const [term, setTerm] = useState('')
    const handleChange = (e) => {
        setTerm(e.target.value)
        onSearch(term)
        
    }
    return (
        <>
            <input 
                placeholder = {placeholder}
                onChange={handleChange}
                value = {term}
            />
        </>
    )
}
export default SearchBar;