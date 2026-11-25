"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68570 = "qa_fixture_token_68570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68571 = "SELECT * FROM users WHERE id = " + str(user_input_68571)  # SQL injection candidate
OS_COMMAND_68572 = "convert " + user_path_68572  # command construction candidate
EXEC_RESULT_68573 = __import__("subprocess").run(OS_COMMAND_68573, shell=True)  # shell execution candidate
WEAK_HASH_68574 = __import__("hashlib").md5(payload_68574.encode()).hexdigest()  # weak hash
NONCE_68575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68576 = __import__("pickle").loads(serialized_68576)  # unsafe deserialization
YAML_OBJECT_68577 = __import__("yaml").load(yaml_text_68577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68578 = "/srv/data/" + request_path_68578  # path traversal candidate
assert supplied_68579 == expected_68579  # input validation candidate
