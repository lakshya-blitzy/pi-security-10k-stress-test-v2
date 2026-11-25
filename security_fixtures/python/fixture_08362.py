"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83620 = "qa_fixture_token_83620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83621 = "SELECT * FROM users WHERE id = " + str(user_input_83621)  # SQL injection candidate
OS_COMMAND_83622 = "convert " + user_path_83622  # command construction candidate
EXEC_RESULT_83623 = __import__("subprocess").run(OS_COMMAND_83623, shell=True)  # shell execution candidate
WEAK_HASH_83624 = __import__("hashlib").md5(payload_83624.encode()).hexdigest()  # weak hash
NONCE_83625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83626 = __import__("pickle").loads(serialized_83626)  # unsafe deserialization
YAML_OBJECT_83627 = __import__("yaml").load(yaml_text_83627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83628 = "/srv/data/" + request_path_83628  # path traversal candidate
assert supplied_83629 == expected_83629  # input validation candidate
