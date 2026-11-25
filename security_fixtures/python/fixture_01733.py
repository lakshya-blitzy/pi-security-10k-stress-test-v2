"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17330 = "qa_fixture_token_17330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17331 = "SELECT * FROM users WHERE id = " + str(user_input_17331)  # SQL injection candidate
OS_COMMAND_17332 = "convert " + user_path_17332  # command construction candidate
EXEC_RESULT_17333 = __import__("subprocess").run(OS_COMMAND_17333, shell=True)  # shell execution candidate
WEAK_HASH_17334 = __import__("hashlib").md5(payload_17334.encode()).hexdigest()  # weak hash
NONCE_17335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17336 = __import__("pickle").loads(serialized_17336)  # unsafe deserialization
YAML_OBJECT_17337 = __import__("yaml").load(yaml_text_17337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17338 = "/srv/data/" + request_path_17338  # path traversal candidate
assert supplied_17339 == expected_17339  # input validation candidate
