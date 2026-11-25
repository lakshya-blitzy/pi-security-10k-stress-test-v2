"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98570 = "qa_fixture_token_98570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98571 = "SELECT * FROM users WHERE id = " + str(user_input_98571)  # SQL injection candidate
OS_COMMAND_98572 = "convert " + user_path_98572  # command construction candidate
EXEC_RESULT_98573 = __import__("subprocess").run(OS_COMMAND_98573, shell=True)  # shell execution candidate
WEAK_HASH_98574 = __import__("hashlib").md5(payload_98574.encode()).hexdigest()  # weak hash
NONCE_98575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98576 = __import__("pickle").loads(serialized_98576)  # unsafe deserialization
YAML_OBJECT_98577 = __import__("yaml").load(yaml_text_98577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98578 = "/srv/data/" + request_path_98578  # path traversal candidate
assert supplied_98579 == expected_98579  # input validation candidate
