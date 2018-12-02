import React, { Component } from 'react';
import './App.css';
import {getMedicaments, getAllergies, getJson, post} from "./data/DataUtils";
import Select from 'react-select';


class App extends Component {

   constructor(props) {
        super(props);
        this.state = {
            medicamentIsChecked: false,
            allergyIsChecked: false,
            listSelect: [], // o sa am o lista pt medicamente si una pt alergii (pt select si afisat)
            list: [], // list pt afisat
            selectedValue: '',
            placeholderSelect: 'Select allergy / medicament',
            numberElem: 0,
            roButton: false,
            enButton: false,
            jsonAllergies: {}


        };

        this.handleMedicamentChange = this.handleMedicamentChange.bind(this);
        this.handleAllergyChange = this.handleAllergyChange.bind(this);
        this.handleSelectChange = this.handleSelectChange.bind(this);
        this.handleNumberElemChange = this.handleNumberElemChange.bind(this);
        this.handleEnButtonChange = this.handleEnButtonChange.bind(this);
        this.handleRoButtonChange = this.handleRoButtonChange.bind(this);
   }



   handleMedicamentChange (event) {
       console.log("Medicament", event.target.value);
       this.setState({medicamentIsChecked: event.target.value,
                           allergyIsChecked: false,
                           listSelect: Object.values(getJson("allAllergies")),
                           selectedValue: '',
                           placeholderSelect: 'Select allergy'});

   }



   handleAllergyChange (event) {
       console.log("Allergy", event.target.value);
       this.setState({allergyIsChecked: event.target.value,
                     medicamentIsChecked: false,
                     listSelect: getMedicaments(),
                     selectedValue: '',
                     placeholderSelect: 'Select medicament'});

   }


    handleSelectChange (value) {
       console.log("select::::: ", value);
       this.setState({selectedValue : value});

    }

    handleNumberElemChange (event) {
        console.log("numberElem::::: ", event.target.value);
        this.setState({numberElem : event.target.value});
    }

    handleRoButtonChange(event) {
        console.log("roButton::::: ", event.target.value);
         var obj = {
                     "allergy": this.state.allergyIsChecked,
                     "medicament": this.state.medicamentIsChecked
                   };
        this.setState({roButton : event.target.value,
                       enButton: false,
                       list:  Object.values(post("translatedLabels", obj)).map(i => i[1])});
    }

    handleEnButtonChange (event) {
//        console.log("enButton::::: ", event.target.value);
//        console.log("1::::: ", this.state.allergyIsChecked);
//        console.log("2::::: ", this.state.medicamentIsChecked);

           var obj = {
                     "allergy": this.state.allergyIsChecked,
                     "medicament": this.state.medicamentIsChecked
                   };
        this.setState({enButton : event.target.value,
                       roButton: false,
                       list:  Object.values(post("translatedLabels", obj)).map(i => i[0])});
    }

    render() {
        var flag =  {"id1": ['numeEngleza', 'numeRomana'], "id2": ['numeEngleza', 'numeRomana']};
        console.log("flag", Object.values(flag).map(i => i[1]));

        var listItems;
        const size = this.state.numberElem;
        if(size > this.state.list.length){
            listItems = "Ne pare rau, nu sunt atatea elemente in baza de date. Va rugam introduceti un numar mai mic :) "
        } else {
            if (this.state.medicamentIsChecked && this.state.selectedValue !== '') {
                   listItems = this.state.list.slice(0, size).map((number) => // o sa fie lista de alergii
                                                   <li key={number.toString()}>
                                                       {number}
                                                   </li>);
            }

            if (this.state.allergyIsChecked && this.state.selectedValue !== '') {
                    listItems = this.state.list.slice(0, size).map((number) =>
                                                   <li key={number.toString()}>
                                                        {number}
                                                    </li>
                                                    );
            }
        }

    return (
      <div className="container">
       <span>
                 &nbsp;

          <div style={{  float: 'right'}}>
                <button type="button" className="btn btn-info"  value={true}  onClick={this.handleRoButtonChange}>Ro</button>
                {"   "}
                <button type="button" className="btn btn-info"  value={true} onClick={this.handleEnButtonChange}>En</button>
          </div>
          <center><h1>Medicaments & Allergies</h1></center>

          &nbsp;
         <div  className="radio radio-info" style={{left: '25px'}}>
            <input type="radio" name="survey" id="Radios1"  value={true} onChange={this.handleMedicamentChange}/>
            <label>
              Medicament
            </label>
         </div>
         <div className="radio radio-info " style={{left: '25px'}}>
              <input type="radio" name="survey" id="Radios2"  value={true} onChange={this.handleAllergyChange}  />
            <label>
              Allergy
            </label>
         </div>
         <Select
              onChange={this.handleSelectChange}
              options={this.state.listSelect.map(data => ({label: data}))}
              placeholder={this.state.placeholderSelect}
              value={this.state.selectedValue}
         />
         &nbsp;
         <input type="number" className="form-control"   placeholder="Nr. elemente" onChange={this.handleNumberElemChange}/>
         &nbsp;
         {<ol> {listItems}</ol>}
        </span>

      </div>
    );
    }
}

export default App;
