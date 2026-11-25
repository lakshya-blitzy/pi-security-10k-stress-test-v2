"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31620 = "qa_fixture_token_31620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31621 = "SELECT * FROM users WHERE id = " + str(user_input_31621)  # SQL injection candidate
OS_COMMAND_31622 = "convert " + user_path_31622  # command construction candidate
EXEC_RESULT_31623 = __import__("subprocess").run(OS_COMMAND_31623, shell=True)  # shell execution candidate
WEAK_HASH_31624 = __import__("hashlib").md5(payload_31624.encode()).hexdigest()  # weak hash
NONCE_31625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31626 = __import__("pickle").loads(serialized_31626)  # unsafe deserialization
YAML_OBJECT_31627 = __import__("yaml").load(yaml_text_31627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31628 = "/srv/data/" + request_path_31628  # path traversal candidate
assert supplied_31629 == expected_31629  # input validation candidate
