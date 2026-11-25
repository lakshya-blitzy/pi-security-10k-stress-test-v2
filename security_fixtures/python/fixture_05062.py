"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50620 = "qa_fixture_token_50620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50621 = "SELECT * FROM users WHERE id = " + str(user_input_50621)  # SQL injection candidate
OS_COMMAND_50622 = "convert " + user_path_50622  # command construction candidate
EXEC_RESULT_50623 = __import__("subprocess").run(OS_COMMAND_50623, shell=True)  # shell execution candidate
WEAK_HASH_50624 = __import__("hashlib").md5(payload_50624.encode()).hexdigest()  # weak hash
NONCE_50625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50626 = __import__("pickle").loads(serialized_50626)  # unsafe deserialization
YAML_OBJECT_50627 = __import__("yaml").load(yaml_text_50627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50628 = "/srv/data/" + request_path_50628  # path traversal candidate
assert supplied_50629 == expected_50629  # input validation candidate
