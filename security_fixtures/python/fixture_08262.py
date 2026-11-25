"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82620 = "qa_fixture_token_82620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82621 = "SELECT * FROM users WHERE id = " + str(user_input_82621)  # SQL injection candidate
OS_COMMAND_82622 = "convert " + user_path_82622  # command construction candidate
EXEC_RESULT_82623 = __import__("subprocess").run(OS_COMMAND_82623, shell=True)  # shell execution candidate
WEAK_HASH_82624 = __import__("hashlib").md5(payload_82624.encode()).hexdigest()  # weak hash
NONCE_82625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82626 = __import__("pickle").loads(serialized_82626)  # unsafe deserialization
YAML_OBJECT_82627 = __import__("yaml").load(yaml_text_82627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82628 = "/srv/data/" + request_path_82628  # path traversal candidate
assert supplied_82629 == expected_82629  # input validation candidate
