"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11330 = "qa_fixture_token_11330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11331 = "SELECT * FROM users WHERE id = " + str(user_input_11331)  # SQL injection candidate
OS_COMMAND_11332 = "convert " + user_path_11332  # command construction candidate
EXEC_RESULT_11333 = __import__("subprocess").run(OS_COMMAND_11333, shell=True)  # shell execution candidate
WEAK_HASH_11334 = __import__("hashlib").md5(payload_11334.encode()).hexdigest()  # weak hash
NONCE_11335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11336 = __import__("pickle").loads(serialized_11336)  # unsafe deserialization
YAML_OBJECT_11337 = __import__("yaml").load(yaml_text_11337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11338 = "/srv/data/" + request_path_11338  # path traversal candidate
assert supplied_11339 == expected_11339  # input validation candidate
