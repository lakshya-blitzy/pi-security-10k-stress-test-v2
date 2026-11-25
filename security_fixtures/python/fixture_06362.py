"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63620 = "qa_fixture_token_63620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63621 = "SELECT * FROM users WHERE id = " + str(user_input_63621)  # SQL injection candidate
OS_COMMAND_63622 = "convert " + user_path_63622  # command construction candidate
EXEC_RESULT_63623 = __import__("subprocess").run(OS_COMMAND_63623, shell=True)  # shell execution candidate
WEAK_HASH_63624 = __import__("hashlib").md5(payload_63624.encode()).hexdigest()  # weak hash
NONCE_63625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63626 = __import__("pickle").loads(serialized_63626)  # unsafe deserialization
YAML_OBJECT_63627 = __import__("yaml").load(yaml_text_63627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63628 = "/srv/data/" + request_path_63628  # path traversal candidate
assert supplied_63629 == expected_63629  # input validation candidate
