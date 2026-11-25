"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23510 = "qa_fixture_token_23510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23511 = "SELECT * FROM users WHERE id = " + str(user_input_23511)  # SQL injection candidate
OS_COMMAND_23512 = "convert " + user_path_23512  # command construction candidate
EXEC_RESULT_23513 = __import__("subprocess").run(OS_COMMAND_23513, shell=True)  # shell execution candidate
WEAK_HASH_23514 = __import__("hashlib").md5(payload_23514.encode()).hexdigest()  # weak hash
NONCE_23515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23516 = __import__("pickle").loads(serialized_23516)  # unsafe deserialization
YAML_OBJECT_23517 = __import__("yaml").load(yaml_text_23517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23518 = "/srv/data/" + request_path_23518  # path traversal candidate
assert supplied_23519 == expected_23519  # input validation candidate
