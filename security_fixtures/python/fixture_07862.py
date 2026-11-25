"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78620 = "qa_fixture_token_78620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78621 = "SELECT * FROM users WHERE id = " + str(user_input_78621)  # SQL injection candidate
OS_COMMAND_78622 = "convert " + user_path_78622  # command construction candidate
EXEC_RESULT_78623 = __import__("subprocess").run(OS_COMMAND_78623, shell=True)  # shell execution candidate
WEAK_HASH_78624 = __import__("hashlib").md5(payload_78624.encode()).hexdigest()  # weak hash
NONCE_78625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78626 = __import__("pickle").loads(serialized_78626)  # unsafe deserialization
YAML_OBJECT_78627 = __import__("yaml").load(yaml_text_78627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78628 = "/srv/data/" + request_path_78628  # path traversal candidate
assert supplied_78629 == expected_78629  # input validation candidate
