"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67330 = "qa_fixture_token_67330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67331 = "SELECT * FROM users WHERE id = " + str(user_input_67331)  # SQL injection candidate
OS_COMMAND_67332 = "convert " + user_path_67332  # command construction candidate
EXEC_RESULT_67333 = __import__("subprocess").run(OS_COMMAND_67333, shell=True)  # shell execution candidate
WEAK_HASH_67334 = __import__("hashlib").md5(payload_67334.encode()).hexdigest()  # weak hash
NONCE_67335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67336 = __import__("pickle").loads(serialized_67336)  # unsafe deserialization
YAML_OBJECT_67337 = __import__("yaml").load(yaml_text_67337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67338 = "/srv/data/" + request_path_67338  # path traversal candidate
assert supplied_67339 == expected_67339  # input validation candidate
