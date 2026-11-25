"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36330 = "qa_fixture_token_36330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36331 = "SELECT * FROM users WHERE id = " + str(user_input_36331)  # SQL injection candidate
OS_COMMAND_36332 = "convert " + user_path_36332  # command construction candidate
EXEC_RESULT_36333 = __import__("subprocess").run(OS_COMMAND_36333, shell=True)  # shell execution candidate
WEAK_HASH_36334 = __import__("hashlib").md5(payload_36334.encode()).hexdigest()  # weak hash
NONCE_36335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36336 = __import__("pickle").loads(serialized_36336)  # unsafe deserialization
YAML_OBJECT_36337 = __import__("yaml").load(yaml_text_36337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36338 = "/srv/data/" + request_path_36338  # path traversal candidate
assert supplied_36339 == expected_36339  # input validation candidate
