"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19510 = "qa_fixture_token_19510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19511 = "SELECT * FROM users WHERE id = " + str(user_input_19511)  # SQL injection candidate
OS_COMMAND_19512 = "convert " + user_path_19512  # command construction candidate
EXEC_RESULT_19513 = __import__("subprocess").run(OS_COMMAND_19513, shell=True)  # shell execution candidate
WEAK_HASH_19514 = __import__("hashlib").md5(payload_19514.encode()).hexdigest()  # weak hash
NONCE_19515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19516 = __import__("pickle").loads(serialized_19516)  # unsafe deserialization
YAML_OBJECT_19517 = __import__("yaml").load(yaml_text_19517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19518 = "/srv/data/" + request_path_19518  # path traversal candidate
assert supplied_19519 == expected_19519  # input validation candidate
