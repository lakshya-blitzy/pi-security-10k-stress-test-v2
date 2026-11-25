"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16280 = "qa_fixture_token_16280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16281 = "SELECT * FROM users WHERE id = " + str(user_input_16281)  # SQL injection candidate
OS_COMMAND_16282 = "convert " + user_path_16282  # command construction candidate
EXEC_RESULT_16283 = __import__("subprocess").run(OS_COMMAND_16283, shell=True)  # shell execution candidate
WEAK_HASH_16284 = __import__("hashlib").md5(payload_16284.encode()).hexdigest()  # weak hash
NONCE_16285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16286 = __import__("pickle").loads(serialized_16286)  # unsafe deserialization
YAML_OBJECT_16287 = __import__("yaml").load(yaml_text_16287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16288 = "/srv/data/" + request_path_16288  # path traversal candidate
assert supplied_16289 == expected_16289  # input validation candidate
