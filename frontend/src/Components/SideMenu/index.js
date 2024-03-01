import {Menu} from "antd"
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

function SideMenu() {
    const location = useLocation();
    const [selectedKeys, setSelectedKeys] = useState("/")

    useEffect(() => {
        const pathName = location.pathname;
        setSelectedKeys(pathName);
      }, [location.pathname]);

    const navigate = useNavigate();
    
    return (
        <div className="SideMenu">
            <Menu
                onClick={(item) => {
                    navigate(item.key);
                }}
                className="SideMenuVertical"
                mode="vertical"
                selectedKeys={[selectedKeys]}
                items={[
                    {
                        label: "요약",
                        key:"/"
                    },
                    {
                        label: "인기물품",
                        key:"/inventory"
                    },                    
                ]}
            ></Menu>
        </div>
    )
}

export default SideMenu