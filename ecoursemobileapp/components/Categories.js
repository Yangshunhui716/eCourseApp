import { useEffect, useState } from "react";
import Apis, { endpoints } from "../utils/Apis";
import { Chip } from "react-native-paper";
import { TouchableOpacity, View } from "react-native";
import MyStyles from "../styles/MyStyles";

const Categories = ({setCateId}) => {
    const [categories, setCategories] = useState([]);

    const loadCates = async() => {
        let res = await Apis.get(endpoints['categories']);
        setCategories(res.data);
        res.data;
    }

    useEffect(() => {
        loadCates();
    }, [])

    return(
        <View style={MyStyles.row}>
            <TouchableOpacity onPress={() => setCateId(null)}>
                <Chip icon='label' style={MyStyles.margin}>Tất cả</Chip>
            </TouchableOpacity>
            {categories.map(c => <TouchableOpacity key={c.id} onPress={() => setCateId(c.id)}>
                <Chip icon='label' style={MyStyles.margin}>{c.name}</Chip>
            </TouchableOpacity>)}
        </View>
    );
}

export default Categories