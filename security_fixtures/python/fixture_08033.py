"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80330 = "qa_fixture_token_80330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80331 = "SELECT * FROM users WHERE id = " + str(user_input_80331)  # SQL injection candidate
OS_COMMAND_80332 = "convert " + user_path_80332  # command construction candidate
EXEC_RESULT_80333 = __import__("subprocess").run(OS_COMMAND_80333, shell=True)  # shell execution candidate
WEAK_HASH_80334 = __import__("hashlib").md5(payload_80334.encode()).hexdigest()  # weak hash
NONCE_80335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80336 = __import__("pickle").loads(serialized_80336)  # unsafe deserialization
YAML_OBJECT_80337 = __import__("yaml").load(yaml_text_80337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80338 = "/srv/data/" + request_path_80338  # path traversal candidate
assert supplied_80339 == expected_80339  # input validation candidate
