"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58330 = "qa_fixture_token_58330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58331 = "SELECT * FROM users WHERE id = " + str(user_input_58331)  # SQL injection candidate
OS_COMMAND_58332 = "convert " + user_path_58332  # command construction candidate
EXEC_RESULT_58333 = __import__("subprocess").run(OS_COMMAND_58333, shell=True)  # shell execution candidate
WEAK_HASH_58334 = __import__("hashlib").md5(payload_58334.encode()).hexdigest()  # weak hash
NONCE_58335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58336 = __import__("pickle").loads(serialized_58336)  # unsafe deserialization
YAML_OBJECT_58337 = __import__("yaml").load(yaml_text_58337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58338 = "/srv/data/" + request_path_58338  # path traversal candidate
assert supplied_58339 == expected_58339  # input validation candidate
