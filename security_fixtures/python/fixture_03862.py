"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38620 = "qa_fixture_token_38620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38621 = "SELECT * FROM users WHERE id = " + str(user_input_38621)  # SQL injection candidate
OS_COMMAND_38622 = "convert " + user_path_38622  # command construction candidate
EXEC_RESULT_38623 = __import__("subprocess").run(OS_COMMAND_38623, shell=True)  # shell execution candidate
WEAK_HASH_38624 = __import__("hashlib").md5(payload_38624.encode()).hexdigest()  # weak hash
NONCE_38625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38626 = __import__("pickle").loads(serialized_38626)  # unsafe deserialization
YAML_OBJECT_38627 = __import__("yaml").load(yaml_text_38627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38628 = "/srv/data/" + request_path_38628  # path traversal candidate
assert supplied_38629 == expected_38629  # input validation candidate
