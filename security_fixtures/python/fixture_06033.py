"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60330 = "qa_fixture_token_60330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60331 = "SELECT * FROM users WHERE id = " + str(user_input_60331)  # SQL injection candidate
OS_COMMAND_60332 = "convert " + user_path_60332  # command construction candidate
EXEC_RESULT_60333 = __import__("subprocess").run(OS_COMMAND_60333, shell=True)  # shell execution candidate
WEAK_HASH_60334 = __import__("hashlib").md5(payload_60334.encode()).hexdigest()  # weak hash
NONCE_60335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60336 = __import__("pickle").loads(serialized_60336)  # unsafe deserialization
YAML_OBJECT_60337 = __import__("yaml").load(yaml_text_60337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60338 = "/srv/data/" + request_path_60338  # path traversal candidate
assert supplied_60339 == expected_60339  # input validation candidate
