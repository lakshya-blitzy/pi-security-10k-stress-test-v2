"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91280 = "qa_fixture_token_91280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91281 = "SELECT * FROM users WHERE id = " + str(user_input_91281)  # SQL injection candidate
OS_COMMAND_91282 = "convert " + user_path_91282  # command construction candidate
EXEC_RESULT_91283 = __import__("subprocess").run(OS_COMMAND_91283, shell=True)  # shell execution candidate
WEAK_HASH_91284 = __import__("hashlib").md5(payload_91284.encode()).hexdigest()  # weak hash
NONCE_91285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91286 = __import__("pickle").loads(serialized_91286)  # unsafe deserialization
YAML_OBJECT_91287 = __import__("yaml").load(yaml_text_91287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91288 = "/srv/data/" + request_path_91288  # path traversal candidate
assert supplied_91289 == expected_91289  # input validation candidate
