# SportsBetting.DefaultApi

All URIs are relative to *http://127.0.0.1:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**competitionsGet**](DefaultApi.md#competitionsGet) | **GET** /competitions | 
[**competitionsInfoGet**](DefaultApi.md#competitionsInfoGet) | **GET** /competitions_info | 
[**competitionsInfoPost**](DefaultApi.md#competitionsInfoPost) | **POST** /competitions_info | 
[**createBetPost**](DefaultApi.md#createBetPost) | **POST** /create/bet | 
[**createCompetitionPost**](DefaultApi.md#createCompetitionPost) | **POST** /create/competition | 
[**createMatchPost**](DefaultApi.md#createMatchPost) | **POST** /create/match | 
[**matchInfoGet**](DefaultApi.md#matchInfoGet) | **GET** /match_info | 
[**userGet**](DefaultApi.md#userGet) | **GET** /user | 
[**userLoginPost**](DefaultApi.md#userLoginPost) | **POST** /user_login | 
[**userPut**](DefaultApi.md#userPut) | **PUT** /user | 
[**userRegisterApprovePost**](DefaultApi.md#userRegisterApprovePost) | **POST** /user_register_approve | 
[**userRegisterPost**](DefaultApi.md#userRegisterPost) | **POST** /user_register | 

<a name="competitionsGet"></a>
# **competitionsGet**
> InlineResponse200 competitionsGet(id)



Получает все соревнования пользователя.

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let id = "id_example"; // String | 

apiInstance.competitionsGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="competitionsInfoGet"></a>
# **competitionsInfoGet**
> Competition competitionsInfoGet(competitionId, id)



Отдает информаицю о соревновании для этого пользовтеля.

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let competitionId = "competitionId_example"; // String | 
let id = "id_example"; // String | 

apiInstance.competitionsInfoGet(competitionId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **competitionId** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**Competition**](Competition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="competitionsInfoPost"></a>
# **competitionsInfoPost**
> Competition competitionsInfoPost(competitionId, id)



Добавляет пользователя в участие в соревнование.

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let competitionId = "competitionId_example"; // String | 
let id = "id_example"; // String | 

apiInstance.competitionsInfoPost(competitionId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **competitionId** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**Competition**](Competition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="createBetPost"></a>
# **createBetPost**
> Match createBetPost(id, matchId, opts)



Делает ставку.

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let id = "id_example"; // String | 
let matchId = "matchId_example"; // String | 
let opts = { 
  'body': new SportsBetting.CreateBetBody() // CreateBetBody | 
};
apiInstance.createBetPost(id, matchId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **matchId** | **String**|  | 
 **body** | [**CreateBetBody**](CreateBetBody.md)|  | [optional] 

### Return type

[**Match**](Match.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createCompetitionPost"></a>
# **createCompetitionPost**
> Competition createCompetitionPost(id, opts)



Создает новое соревнование.

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let id = "id_example"; // String | 
let opts = { 
  'body': new SportsBetting.CreateCompetitionBody() // CreateCompetitionBody | 
};
apiInstance.createCompetitionPost(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **body** | [**CreateCompetitionBody**](CreateCompetitionBody.md)|  | [optional] 

### Return type

[**Competition**](Competition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createMatchPost"></a>
# **createMatchPost**
> Match createMatchPost(id, competionId, opts)



Создает новый матч.

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let id = "id_example"; // String | 
let competionId = "competionId_example"; // String | 
let opts = { 
  'body': new SportsBetting.CreateMatchBody() // CreateMatchBody | 
};
apiInstance.createMatchPost(id, competionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **competionId** | **String**|  | 
 **body** | [**CreateMatchBody**](CreateMatchBody.md)|  | [optional] 

### Return type

[**Match**](Match.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="matchInfoGet"></a>
# **matchInfoGet**
> Match matchInfoGet(matchId, id)



Отдает информаицю о матче для этого пользовтеля.

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let matchId = "matchId_example"; // String | 
let id = "id_example"; // String | 

apiInstance.matchInfoGet(matchId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matchId** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**Match**](Match.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="userGet"></a>
# **userGet**
> UserInfo userGet(id)



Выдача информации о пользователе

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let id = "id_example"; // String | 

apiInstance.userGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="userLoginPost"></a>
# **userLoginPost**
> InlineResponse2001 userLoginPost(opts)



Залогинивает пользователя с заданными данными.

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let opts = { 
  'body': new SportsBetting.BaseUserInfo() // BaseUserInfo | 
};
apiInstance.userLoginPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseUserInfo**](BaseUserInfo.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="userPut"></a>
# **userPut**
> UserInfo userPut(id, opts)



Изменение информации о пользователе.

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let id = "id_example"; // String | 
let opts = { 
  'body': new SportsBetting.UserMeta() // UserMeta | 
};
apiInstance.userPut(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **body** | [**UserMeta**](UserMeta.md)|  | [optional] 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="userRegisterApprovePost"></a>
# **userRegisterApprovePost**
> UserInfo userRegisterApprovePost(opts)



Подтверждает регистрацию пользователя (страница с вводом слова регистрации).

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let opts = { 
  'body': new SportsBetting.RegisterApprove() // RegisterApprove | 
};
apiInstance.userRegisterApprovePost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterApprove**](RegisterApprove.md)|  | [optional] 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="userRegisterPost"></a>
# **userRegisterPost**
> userRegisterPost(opts)



Регистрирует пользователя с заданными данными.

### Example
```javascript
import {SportsBetting} from 'sports_betting';

let apiInstance = new SportsBetting.DefaultApi();
let opts = { 
  'body': new SportsBetting.UserInfo() // UserInfo | 
};
apiInstance.userRegisterPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserInfo**](UserInfo.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

