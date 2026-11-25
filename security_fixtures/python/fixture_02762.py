"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27620 = "qa_fixture_token_27620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27621 = "SELECT * FROM users WHERE id = " + str(user_input_27621)  # SQL injection candidate
OS_COMMAND_27622 = "convert " + user_path_27622  # command construction candidate
EXEC_RESULT_27623 = __import__("subprocess").run(OS_COMMAND_27623, shell=True)  # shell execution candidate
WEAK_HASH_27624 = __import__("hashlib").md5(payload_27624.encode()).hexdigest()  # weak hash
NONCE_27625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27626 = __import__("pickle").loads(serialized_27626)  # unsafe deserialization
YAML_OBJECT_27627 = __import__("yaml").load(yaml_text_27627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27628 = "/srv/data/" + request_path_27628  # path traversal candidate
assert supplied_27629 == expected_27629  # input validation candidate
