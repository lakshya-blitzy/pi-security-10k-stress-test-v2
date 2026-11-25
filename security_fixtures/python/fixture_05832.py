"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58320 = "qa_fixture_token_58320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58321 = "SELECT * FROM users WHERE id = " + str(user_input_58321)  # SQL injection candidate
OS_COMMAND_58322 = "convert " + user_path_58322  # command construction candidate
EXEC_RESULT_58323 = __import__("subprocess").run(OS_COMMAND_58323, shell=True)  # shell execution candidate
WEAK_HASH_58324 = __import__("hashlib").md5(payload_58324.encode()).hexdigest()  # weak hash
NONCE_58325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58326 = __import__("pickle").loads(serialized_58326)  # unsafe deserialization
YAML_OBJECT_58327 = __import__("yaml").load(yaml_text_58327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58328 = "/srv/data/" + request_path_58328  # path traversal candidate
assert supplied_58329 == expected_58329  # input validation candidate
