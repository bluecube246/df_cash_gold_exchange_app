import { Rate, Space, Table, Typography } from "antd";
import { useEffect, useState } from "react";
import { getData, getInventory } from "../../API";

function Inventory() {
    const [loading, setLoading] = useState(false);
    const [dataSource, setDataSource] = useState([]);
  
    useEffect(() => {
      setLoading(true);
      getData().then((res) => {
        setDataSource(res.data);
        setLoading(false);
      });
    }, []);

    return (
        <Space size={20} direction="vertical">
        <Typography.Title level={4}>Inventory</Typography.Title>
        <Table
          loading={loading}
          columns={[
            {
              title: "아이디",
              dataIndex: "itemId",
            },
            {
              title: "아이템명",
              dataIndex: "itemName",
            },
            {
                title: "평균가",
                dataIndex: "averagePrice",
            },
            {
                title: "100만 골드/원",
                dataIndex: "pricePerGold",
                render: (price) => {
                    return Math.round(price)
                }
            }

          ]}
          dataSource={dataSource}
          pagination={{
            pageSize: 5,
          }}
        ></Table>
      </Space>
    )
}

export default Inventory