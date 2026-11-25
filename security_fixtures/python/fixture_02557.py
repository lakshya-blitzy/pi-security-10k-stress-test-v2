"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25570 = "qa_fixture_token_25570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25571 = "SELECT * FROM users WHERE id = " + str(user_input_25571)  # SQL injection candidate
OS_COMMAND_25572 = "convert " + user_path_25572  # command construction candidate
EXEC_RESULT_25573 = __import__("subprocess").run(OS_COMMAND_25573, shell=True)  # shell execution candidate
WEAK_HASH_25574 = __import__("hashlib").md5(payload_25574.encode()).hexdigest()  # weak hash
NONCE_25575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25576 = __import__("pickle").loads(serialized_25576)  # unsafe deserialization
YAML_OBJECT_25577 = __import__("yaml").load(yaml_text_25577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25578 = "/srv/data/" + request_path_25578  # path traversal candidate
assert supplied_25579 == expected_25579  # input validation candidate
