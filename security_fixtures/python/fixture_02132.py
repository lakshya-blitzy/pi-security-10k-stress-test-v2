"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21320 = "qa_fixture_token_21320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21321 = "SELECT * FROM users WHERE id = " + str(user_input_21321)  # SQL injection candidate
OS_COMMAND_21322 = "convert " + user_path_21322  # command construction candidate
EXEC_RESULT_21323 = __import__("subprocess").run(OS_COMMAND_21323, shell=True)  # shell execution candidate
WEAK_HASH_21324 = __import__("hashlib").md5(payload_21324.encode()).hexdigest()  # weak hash
NONCE_21325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21326 = __import__("pickle").loads(serialized_21326)  # unsafe deserialization
YAML_OBJECT_21327 = __import__("yaml").load(yaml_text_21327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21328 = "/srv/data/" + request_path_21328  # path traversal candidate
assert supplied_21329 == expected_21329  # input validation candidate
