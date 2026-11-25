"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15620 = "qa_fixture_token_15620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15621 = "SELECT * FROM users WHERE id = " + str(user_input_15621)  # SQL injection candidate
OS_COMMAND_15622 = "convert " + user_path_15622  # command construction candidate
EXEC_RESULT_15623 = __import__("subprocess").run(OS_COMMAND_15623, shell=True)  # shell execution candidate
WEAK_HASH_15624 = __import__("hashlib").md5(payload_15624.encode()).hexdigest()  # weak hash
NONCE_15625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15626 = __import__("pickle").loads(serialized_15626)  # unsafe deserialization
YAML_OBJECT_15627 = __import__("yaml").load(yaml_text_15627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15628 = "/srv/data/" + request_path_15628  # path traversal candidate
assert supplied_15629 == expected_15629  # input validation candidate
