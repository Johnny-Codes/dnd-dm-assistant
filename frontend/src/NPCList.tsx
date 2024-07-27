import {useState} from 'react'


const NPCList = () => {

    const [count, setCount] = useState(100)

    return (`NPMList ${count}`)
}

export default NPCList;