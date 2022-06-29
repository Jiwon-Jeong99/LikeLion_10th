import React from 'react'
import styled from "styled-components"
import data from "./data.json"
import "./Box.css"

const StyledBox = styled.button

`
margin:0;
border : 1px solid transparent;
width:30vh;
height:30vh;
font-size:15px;
background-color:white;
text-align:left;
margin:0vh 2vh 2vh 0vh;
`

const Box = () => {
    // t:보여지는 거, i:인덱스 -> key로 가져와서 t를 보여준다
    return <>{data.products.map((product)=>(
        <StyledBox key={product.id}>
            <img src={product.img} alt="no img"></img>
            <p><b>{product.title}</b></p>
            <p className="address">{product.address}</p>
            <p className="price">{product.price}</p>
        </StyledBox>
    ))}
    </>
}

export default Box