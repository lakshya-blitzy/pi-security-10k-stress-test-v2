"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5330 = "qa_fixture_token_5330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5331 = "SELECT * FROM users WHERE id = " + str(user_input_5331)  # SQL injection candidate
OS_COMMAND_5332 = "convert " + user_path_5332  # command construction candidate
EXEC_RESULT_5333 = __import__("subprocess").run(OS_COMMAND_5333, shell=True)  # shell execution candidate
WEAK_HASH_5334 = __import__("hashlib").md5(payload_5334.encode()).hexdigest()  # weak hash
NONCE_5335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5336 = __import__("pickle").loads(serialized_5336)  # unsafe deserialization
YAML_OBJECT_5337 = __import__("yaml").load(yaml_text_5337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5338 = "/srv/data/" + request_path_5338  # path traversal candidate
assert supplied_5339 == expected_5339  # input validation candidate
