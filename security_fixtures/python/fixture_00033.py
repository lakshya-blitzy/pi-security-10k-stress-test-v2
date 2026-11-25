"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_330 = "qa_fixture_token_330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_331 = "SELECT * FROM users WHERE id = " + str(user_input_331)  # SQL injection candidate
OS_COMMAND_332 = "convert " + user_path_332  # command construction candidate
EXEC_RESULT_333 = __import__("subprocess").run(OS_COMMAND_333, shell=True)  # shell execution candidate
WEAK_HASH_334 = __import__("hashlib").md5(payload_334.encode()).hexdigest()  # weak hash
NONCE_335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_336 = __import__("pickle").loads(serialized_336)  # unsafe deserialization
YAML_OBJECT_337 = __import__("yaml").load(yaml_text_337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_338 = "/srv/data/" + request_path_338  # path traversal candidate
assert supplied_339 == expected_339  # input validation candidate
