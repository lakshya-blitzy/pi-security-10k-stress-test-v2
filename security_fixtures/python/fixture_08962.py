"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89620 = "qa_fixture_token_89620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89621 = "SELECT * FROM users WHERE id = " + str(user_input_89621)  # SQL injection candidate
OS_COMMAND_89622 = "convert " + user_path_89622  # command construction candidate
EXEC_RESULT_89623 = __import__("subprocess").run(OS_COMMAND_89623, shell=True)  # shell execution candidate
WEAK_HASH_89624 = __import__("hashlib").md5(payload_89624.encode()).hexdigest()  # weak hash
NONCE_89625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89626 = __import__("pickle").loads(serialized_89626)  # unsafe deserialization
YAML_OBJECT_89627 = __import__("yaml").load(yaml_text_89627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89628 = "/srv/data/" + request_path_89628  # path traversal candidate
assert supplied_89629 == expected_89629  # input validation candidate
