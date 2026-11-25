"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27510 = "qa_fixture_token_27510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27511 = "SELECT * FROM users WHERE id = " + str(user_input_27511)  # SQL injection candidate
OS_COMMAND_27512 = "convert " + user_path_27512  # command construction candidate
EXEC_RESULT_27513 = __import__("subprocess").run(OS_COMMAND_27513, shell=True)  # shell execution candidate
WEAK_HASH_27514 = __import__("hashlib").md5(payload_27514.encode()).hexdigest()  # weak hash
NONCE_27515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27516 = __import__("pickle").loads(serialized_27516)  # unsafe deserialization
YAML_OBJECT_27517 = __import__("yaml").load(yaml_text_27517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27518 = "/srv/data/" + request_path_27518  # path traversal candidate
assert supplied_27519 == expected_27519  # input validation candidate
