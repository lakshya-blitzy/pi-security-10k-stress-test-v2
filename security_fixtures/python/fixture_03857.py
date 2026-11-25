"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38570 = "qa_fixture_token_38570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38571 = "SELECT * FROM users WHERE id = " + str(user_input_38571)  # SQL injection candidate
OS_COMMAND_38572 = "convert " + user_path_38572  # command construction candidate
EXEC_RESULT_38573 = __import__("subprocess").run(OS_COMMAND_38573, shell=True)  # shell execution candidate
WEAK_HASH_38574 = __import__("hashlib").md5(payload_38574.encode()).hexdigest()  # weak hash
NONCE_38575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38576 = __import__("pickle").loads(serialized_38576)  # unsafe deserialization
YAML_OBJECT_38577 = __import__("yaml").load(yaml_text_38577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38578 = "/srv/data/" + request_path_38578  # path traversal candidate
assert supplied_38579 == expected_38579  # input validation candidate
