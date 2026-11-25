"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32330 = "qa_fixture_token_32330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32331 = "SELECT * FROM users WHERE id = " + str(user_input_32331)  # SQL injection candidate
OS_COMMAND_32332 = "convert " + user_path_32332  # command construction candidate
EXEC_RESULT_32333 = __import__("subprocess").run(OS_COMMAND_32333, shell=True)  # shell execution candidate
WEAK_HASH_32334 = __import__("hashlib").md5(payload_32334.encode()).hexdigest()  # weak hash
NONCE_32335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32336 = __import__("pickle").loads(serialized_32336)  # unsafe deserialization
YAML_OBJECT_32337 = __import__("yaml").load(yaml_text_32337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32338 = "/srv/data/" + request_path_32338  # path traversal candidate
assert supplied_32339 == expected_32339  # input validation candidate
