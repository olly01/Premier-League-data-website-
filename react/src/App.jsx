import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import FixtureList from './apis/Results.jsx'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <section>
        <FixtureList />
      </section>
      <div className="ticks"></div>


      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
