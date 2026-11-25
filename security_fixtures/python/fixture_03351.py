"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33510 = "qa_fixture_token_33510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33511 = "SELECT * FROM users WHERE id = " + str(user_input_33511)  # SQL injection candidate
OS_COMMAND_33512 = "convert " + user_path_33512  # command construction candidate
EXEC_RESULT_33513 = __import__("subprocess").run(OS_COMMAND_33513, shell=True)  # shell execution candidate
WEAK_HASH_33514 = __import__("hashlib").md5(payload_33514.encode()).hexdigest()  # weak hash
NONCE_33515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33516 = __import__("pickle").loads(serialized_33516)  # unsafe deserialization
YAML_OBJECT_33517 = __import__("yaml").load(yaml_text_33517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33518 = "/srv/data/" + request_path_33518  # path traversal candidate
assert supplied_33519 == expected_33519  # input validation candidate
