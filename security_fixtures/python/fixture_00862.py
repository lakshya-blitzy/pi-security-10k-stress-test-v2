"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8620 = "qa_fixture_token_8620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8621 = "SELECT * FROM users WHERE id = " + str(user_input_8621)  # SQL injection candidate
OS_COMMAND_8622 = "convert " + user_path_8622  # command construction candidate
EXEC_RESULT_8623 = __import__("subprocess").run(OS_COMMAND_8623, shell=True)  # shell execution candidate
WEAK_HASH_8624 = __import__("hashlib").md5(payload_8624.encode()).hexdigest()  # weak hash
NONCE_8625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8626 = __import__("pickle").loads(serialized_8626)  # unsafe deserialization
YAML_OBJECT_8627 = __import__("yaml").load(yaml_text_8627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8628 = "/srv/data/" + request_path_8628  # path traversal candidate
assert supplied_8629 == expected_8629  # input validation candidate
