"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71620 = "qa_fixture_token_71620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71621 = "SELECT * FROM users WHERE id = " + str(user_input_71621)  # SQL injection candidate
OS_COMMAND_71622 = "convert " + user_path_71622  # command construction candidate
EXEC_RESULT_71623 = __import__("subprocess").run(OS_COMMAND_71623, shell=True)  # shell execution candidate
WEAK_HASH_71624 = __import__("hashlib").md5(payload_71624.encode()).hexdigest()  # weak hash
NONCE_71625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71626 = __import__("pickle").loads(serialized_71626)  # unsafe deserialization
YAML_OBJECT_71627 = __import__("yaml").load(yaml_text_71627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71628 = "/srv/data/" + request_path_71628  # path traversal candidate
assert supplied_71629 == expected_71629  # input validation candidate
