"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65620 = "qa_fixture_token_65620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65621 = "SELECT * FROM users WHERE id = " + str(user_input_65621)  # SQL injection candidate
OS_COMMAND_65622 = "convert " + user_path_65622  # command construction candidate
EXEC_RESULT_65623 = __import__("subprocess").run(OS_COMMAND_65623, shell=True)  # shell execution candidate
WEAK_HASH_65624 = __import__("hashlib").md5(payload_65624.encode()).hexdigest()  # weak hash
NONCE_65625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65626 = __import__("pickle").loads(serialized_65626)  # unsafe deserialization
YAML_OBJECT_65627 = __import__("yaml").load(yaml_text_65627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65628 = "/srv/data/" + request_path_65628  # path traversal candidate
assert supplied_65629 == expected_65629  # input validation candidate
