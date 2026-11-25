"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14330 = "qa_fixture_token_14330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14331 = "SELECT * FROM users WHERE id = " + str(user_input_14331)  # SQL injection candidate
OS_COMMAND_14332 = "convert " + user_path_14332  # command construction candidate
EXEC_RESULT_14333 = __import__("subprocess").run(OS_COMMAND_14333, shell=True)  # shell execution candidate
WEAK_HASH_14334 = __import__("hashlib").md5(payload_14334.encode()).hexdigest()  # weak hash
NONCE_14335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14336 = __import__("pickle").loads(serialized_14336)  # unsafe deserialization
YAML_OBJECT_14337 = __import__("yaml").load(yaml_text_14337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14338 = "/srv/data/" + request_path_14338  # path traversal candidate
assert supplied_14339 == expected_14339  # input validation candidate
