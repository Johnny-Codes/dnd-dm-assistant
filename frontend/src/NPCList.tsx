import { useState } from 'react';
import { useGetNpcsQuery } from './npcApi'

const NPCList = () => {

    const [visibleNpcIds, setVisibleNpcIds] = useState([]);

    const toggleVisibility = (id) => {
        setVisibleNpcIds((prevVisibleNpcIds) =>
            prevVisibleNpcIds.includes(id)
                ? prevVisibleNpcIds.filter((npcId) => npcId !== id)
                : [...prevVisibleNpcIds, id]
        );
    };
    const { data, error, isLoading } = useGetNpcsQuery()
    if (isLoading) {
        return <div>Loading...</div>
    }

    if (error) {
        return <div>Error: fuck</div>
    }

    console.log('data', data)

    return (
        <div>
            {data?.map((npc) => (
                <div key={npc.id}>
                    <div onClick={() => toggleVisibility(npc.id)} style={{ cursor: 'pointer' }}>
                        {visibleNpcIds.includes(npc.id) ? '▼' : '▶'} {npc.name}
                    </div>
                    {visibleNpcIds.includes(npc.id) && (
                        <div>
                            <p><button>Edit</button> <button>Details</button></p>
                            <p>Race: {npc.race}</p>
                            <p>Personality: {npc.personality}</p>
                            <p>Physical Description: {npc.physical_description}</p>
                            <p>Role Playing Tips:
                            <ul>
                            {npc.role_playing_tips.map((tip) => (
                                
                                <li key={tip.id}>
                                    {tip.tip}
                                </li>
                            ))}
                            </ul>
                            </p>
                        </div>
                    )}
                </div>
            ))}
        </div>
    )
}

export default NPCList;