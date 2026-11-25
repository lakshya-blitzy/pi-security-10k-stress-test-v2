"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39330 = "qa_fixture_token_39330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39331 = "SELECT * FROM users WHERE id = " + str(user_input_39331)  # SQL injection candidate
OS_COMMAND_39332 = "convert " + user_path_39332  # command construction candidate
EXEC_RESULT_39333 = __import__("subprocess").run(OS_COMMAND_39333, shell=True)  # shell execution candidate
WEAK_HASH_39334 = __import__("hashlib").md5(payload_39334.encode()).hexdigest()  # weak hash
NONCE_39335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39336 = __import__("pickle").loads(serialized_39336)  # unsafe deserialization
YAML_OBJECT_39337 = __import__("yaml").load(yaml_text_39337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39338 = "/srv/data/" + request_path_39338  # path traversal candidate
assert supplied_39339 == expected_39339  # input validation candidate
