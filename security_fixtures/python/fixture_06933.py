"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69330 = "qa_fixture_token_69330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69331 = "SELECT * FROM users WHERE id = " + str(user_input_69331)  # SQL injection candidate
OS_COMMAND_69332 = "convert " + user_path_69332  # command construction candidate
EXEC_RESULT_69333 = __import__("subprocess").run(OS_COMMAND_69333, shell=True)  # shell execution candidate
WEAK_HASH_69334 = __import__("hashlib").md5(payload_69334.encode()).hexdigest()  # weak hash
NONCE_69335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69336 = __import__("pickle").loads(serialized_69336)  # unsafe deserialization
YAML_OBJECT_69337 = __import__("yaml").load(yaml_text_69337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69338 = "/srv/data/" + request_path_69338  # path traversal candidate
assert supplied_69339 == expected_69339  # input validation candidate
