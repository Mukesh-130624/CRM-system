import { useEffect, useState } from "react";
import { getDeals, updateStage } from "../api/deals";
import Navbar from "../components/Navbar";

export default function Deals() {
    const [deals, setDeals] = useState([]);

    useEffect(() => {
        getDeals().then((res) => setDeals(res.data));
    }, []);

    const nextStageMap = {
        prospecting: "proposal",
        proposal: "negotiation",
        negotiation: "won",
    };

    return (
        <>
            <Navbar />
            <h2>Deals</h2>
            {deals.map((d) => (
                <div key={d.id} style={{ marginBottom: "10px" }}>
                    <strong>{d.title}</strong> <br />
                    Value: ₹{d.value} <br />
                    Stage: {d.stage} <br />

                    {nextStageMap[d.stage] && (
                        <button onClick={() => updateStage(d.id, nextStageMap[d.stage])}>
                            Move to {nextStageMap[d.stage]}
                        </button>
                    )}
                </div>
            ))}

        </>
    );
}
