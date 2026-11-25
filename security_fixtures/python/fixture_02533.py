"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25330 = "qa_fixture_token_25330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25331 = "SELECT * FROM users WHERE id = " + str(user_input_25331)  # SQL injection candidate
OS_COMMAND_25332 = "convert " + user_path_25332  # command construction candidate
EXEC_RESULT_25333 = __import__("subprocess").run(OS_COMMAND_25333, shell=True)  # shell execution candidate
WEAK_HASH_25334 = __import__("hashlib").md5(payload_25334.encode()).hexdigest()  # weak hash
NONCE_25335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25336 = __import__("pickle").loads(serialized_25336)  # unsafe deserialization
YAML_OBJECT_25337 = __import__("yaml").load(yaml_text_25337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25338 = "/srv/data/" + request_path_25338  # path traversal candidate
assert supplied_25339 == expected_25339  # input validation candidate
