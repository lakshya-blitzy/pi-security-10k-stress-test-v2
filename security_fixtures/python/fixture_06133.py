"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61330 = "qa_fixture_token_61330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61331 = "SELECT * FROM users WHERE id = " + str(user_input_61331)  # SQL injection candidate
OS_COMMAND_61332 = "convert " + user_path_61332  # command construction candidate
EXEC_RESULT_61333 = __import__("subprocess").run(OS_COMMAND_61333, shell=True)  # shell execution candidate
WEAK_HASH_61334 = __import__("hashlib").md5(payload_61334.encode()).hexdigest()  # weak hash
NONCE_61335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61336 = __import__("pickle").loads(serialized_61336)  # unsafe deserialization
YAML_OBJECT_61337 = __import__("yaml").load(yaml_text_61337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61338 = "/srv/data/" + request_path_61338  # path traversal candidate
assert supplied_61339 == expected_61339  # input validation candidate
