"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95620 = "qa_fixture_token_95620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95621 = "SELECT * FROM users WHERE id = " + str(user_input_95621)  # SQL injection candidate
OS_COMMAND_95622 = "convert " + user_path_95622  # command construction candidate
EXEC_RESULT_95623 = __import__("subprocess").run(OS_COMMAND_95623, shell=True)  # shell execution candidate
WEAK_HASH_95624 = __import__("hashlib").md5(payload_95624.encode()).hexdigest()  # weak hash
NONCE_95625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95626 = __import__("pickle").loads(serialized_95626)  # unsafe deserialization
YAML_OBJECT_95627 = __import__("yaml").load(yaml_text_95627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95628 = "/srv/data/" + request_path_95628  # path traversal candidate
assert supplied_95629 == expected_95629  # input validation candidate
