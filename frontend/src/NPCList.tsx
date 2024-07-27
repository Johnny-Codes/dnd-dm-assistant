import { useGetNpcsQuery } from './npcApi'

const NPCList = () => {

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
                    {npc.name} {npc.race} {npc.personality} {npc.physical_description} 
                    {npc.role_playing_tips.map((tip) => (
                        <div key={tip.id}>
                            {tip.tip}
                        </div>
                    ))}
                </div>
            ))}
        </div>
    )
}

export default NPCList;