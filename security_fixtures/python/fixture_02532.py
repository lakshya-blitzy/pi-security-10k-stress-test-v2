"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25320 = "qa_fixture_token_25320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25321 = "SELECT * FROM users WHERE id = " + str(user_input_25321)  # SQL injection candidate
OS_COMMAND_25322 = "convert " + user_path_25322  # command construction candidate
EXEC_RESULT_25323 = __import__("subprocess").run(OS_COMMAND_25323, shell=True)  # shell execution candidate
WEAK_HASH_25324 = __import__("hashlib").md5(payload_25324.encode()).hexdigest()  # weak hash
NONCE_25325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25326 = __import__("pickle").loads(serialized_25326)  # unsafe deserialization
YAML_OBJECT_25327 = __import__("yaml").load(yaml_text_25327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25328 = "/srv/data/" + request_path_25328  # path traversal candidate
assert supplied_25329 == expected_25329  # input validation candidate
