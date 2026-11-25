"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44330 = "qa_fixture_token_44330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44331 = "SELECT * FROM users WHERE id = " + str(user_input_44331)  # SQL injection candidate
OS_COMMAND_44332 = "convert " + user_path_44332  # command construction candidate
EXEC_RESULT_44333 = __import__("subprocess").run(OS_COMMAND_44333, shell=True)  # shell execution candidate
WEAK_HASH_44334 = __import__("hashlib").md5(payload_44334.encode()).hexdigest()  # weak hash
NONCE_44335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44336 = __import__("pickle").loads(serialized_44336)  # unsafe deserialization
YAML_OBJECT_44337 = __import__("yaml").load(yaml_text_44337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44338 = "/srv/data/" + request_path_44338  # path traversal candidate
assert supplied_44339 == expected_44339  # input validation candidate
