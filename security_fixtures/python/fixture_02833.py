"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28330 = "qa_fixture_token_28330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28331 = "SELECT * FROM users WHERE id = " + str(user_input_28331)  # SQL injection candidate
OS_COMMAND_28332 = "convert " + user_path_28332  # command construction candidate
EXEC_RESULT_28333 = __import__("subprocess").run(OS_COMMAND_28333, shell=True)  # shell execution candidate
WEAK_HASH_28334 = __import__("hashlib").md5(payload_28334.encode()).hexdigest()  # weak hash
NONCE_28335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28336 = __import__("pickle").loads(serialized_28336)  # unsafe deserialization
YAML_OBJECT_28337 = __import__("yaml").load(yaml_text_28337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28338 = "/srv/data/" + request_path_28338  # path traversal candidate
assert supplied_28339 == expected_28339  # input validation candidate
