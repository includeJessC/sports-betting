/*
 * Sports betting
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 0.1.9
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.42
 *
 * Do not edit the class manually.
 *
 */
import {ApiClient} from '../ApiClient';

/**
 * The CreateCompetitionBody model module.
 * @module model/CreateCompetitionBody
 * @version 0.1.9
 */
export class CreateCompetitionBody {
  /**
   * Constructs a new <code>CreateCompetitionBody</code>.
   * @alias module:model/CreateCompetitionBody
   * @class
   * @param parsingRef {String} 
   */
  constructor(parsingRef) {
    this.parsingRef = parsingRef;
  }

  /**
   * Constructs a <code>CreateCompetitionBody</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/CreateCompetitionBody} obj Optional instance to populate.
   * @return {module:model/CreateCompetitionBody} The populated <code>CreateCompetitionBody</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new CreateCompetitionBody();
      if (data.hasOwnProperty('parsing_ref'))
        obj.parsingRef = ApiClient.convertToType(data['parsing_ref'], 'String');
    }
    return obj;
  }
}

/**
 * @member {String} parsingRef
 */
CreateCompetitionBody.prototype.parsingRef = undefined;

