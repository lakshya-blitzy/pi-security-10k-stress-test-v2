"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29620 = "qa_fixture_token_29620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29621 = "SELECT * FROM users WHERE id = " + str(user_input_29621)  # SQL injection candidate
OS_COMMAND_29622 = "convert " + user_path_29622  # command construction candidate
EXEC_RESULT_29623 = __import__("subprocess").run(OS_COMMAND_29623, shell=True)  # shell execution candidate
WEAK_HASH_29624 = __import__("hashlib").md5(payload_29624.encode()).hexdigest()  # weak hash
NONCE_29625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29626 = __import__("pickle").loads(serialized_29626)  # unsafe deserialization
YAML_OBJECT_29627 = __import__("yaml").load(yaml_text_29627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29628 = "/srv/data/" + request_path_29628  # path traversal candidate
assert supplied_29629 == expected_29629  # input validation candidate
