"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8570 = "qa_fixture_token_8570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8571 = "SELECT * FROM users WHERE id = " + str(user_input_8571)  # SQL injection candidate
OS_COMMAND_8572 = "convert " + user_path_8572  # command construction candidate
EXEC_RESULT_8573 = __import__("subprocess").run(OS_COMMAND_8573, shell=True)  # shell execution candidate
WEAK_HASH_8574 = __import__("hashlib").md5(payload_8574.encode()).hexdigest()  # weak hash
NONCE_8575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8576 = __import__("pickle").loads(serialized_8576)  # unsafe deserialization
YAML_OBJECT_8577 = __import__("yaml").load(yaml_text_8577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8578 = "/srv/data/" + request_path_8578  # path traversal candidate
assert supplied_8579 == expected_8579  # input validation candidate
