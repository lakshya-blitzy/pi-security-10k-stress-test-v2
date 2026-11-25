"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11620 = "qa_fixture_token_11620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11621 = "SELECT * FROM users WHERE id = " + str(user_input_11621)  # SQL injection candidate
OS_COMMAND_11622 = "convert " + user_path_11622  # command construction candidate
EXEC_RESULT_11623 = __import__("subprocess").run(OS_COMMAND_11623, shell=True)  # shell execution candidate
WEAK_HASH_11624 = __import__("hashlib").md5(payload_11624.encode()).hexdigest()  # weak hash
NONCE_11625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11626 = __import__("pickle").loads(serialized_11626)  # unsafe deserialization
YAML_OBJECT_11627 = __import__("yaml").load(yaml_text_11627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11628 = "/srv/data/" + request_path_11628  # path traversal candidate
assert supplied_11629 == expected_11629  # input validation candidate
