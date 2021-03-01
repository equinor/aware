import React, { useState } from 'react'
import styled from 'styled-components'

import {getBackgroundColor, LogLine, THTriggered, TH}  from './EventContainer'


const TABLE = styled.table`
    border: 0;
    border-collapse: collapse;
    margin: auto;
    padding: 0;
    width: 90%;
    table-layout: fixed;
`

const THEAD = styled.thead`
display: none;
`

const TR = styled.tr`
display: block;
border: 1px solid black;
border-bottom: none;
padding: 1em 1em .5em;
background: ${props => getBackgroundColor(props.background)};
`

const TRLOG = styled.tr`
display: block;
border-left: 1px solid black;
border-right: 1px solid black;
padding: 1em 1em .5em;
`

const TD = styled.td`
display: flex;
justify-content: space-between;
align-items: flex-end;
font-size: .8em;
line-height: 1.35em;
text-wrap: normal;
text-align: right;
word-wrap: break-word;
`

const TDMSG = styled.td`
align-items: flex-start;
font-size: .8em;
line-height: 1.35em;
word-wrap: break-word;
width: 70%;
`

export const LogContainer = styled.td`
  background-color: #131212;
  width: 100%;
  overflow: auto;
`

function EventRowMobileView({event}) {
  const [logsVisible, setLogsVisible] = useState(false)
  const BG = getBackgroundColor(event.severity)

  return (
      <tbody>
        <TR
            background={event.severity}
            onClick={() => setLogsVisible(!logsVisible)}
            style={{ cursor: "pointer"}}
        >
          <TD data-label="Alertname"> <b>Alertname:</b> {event.alertname}</TD>
          <TD><b>Namespace:</b> {event.namespace}</TD>
          <TD><b>Source:</b> {event.source}</TD>
          <TDMSG><p style={{float: 'left'}}> <b>Message:</b></p> <p style={{float: "right", width: '70%'}}> {event.message}</p></TDMSG>
          <TD><b>Triggered:</b> {event.triggered}</TD>
        </TR>
        <TRLOG style={ {backgroundColor: BG}}>
          {logsVisible &&
          <LogContainer colSpan={5}>
            <div style={{ maxHeight: "600px" }}>
              {event.logs.map(line => (
                  <LogLine>{line}</LogLine>
              ))}
            </div>
          </LogContainer>
          }
        </TRLOG>
      </tbody>
  )
}

function EventContainerMobileView({ events }) {
  return (
      <div style={{ overflow: 'auto' }}>
        <TABLE>
          <THEAD>
            <TR>
              <TH scope="col">Alertname</TH>
              <TH scope="col">Namespace/Host</TH>
              <TH>Source</TH>
              <TH>Message</TH>
              <THTriggered>Triggered</THTriggered>
            </TR>
          </THEAD>
          {events.map(event => (
              <EventRowMobileView event={event}/>
          ))}  
        </TABLE>
      </div>)
      
  
}

export default EventContainerMobileView
