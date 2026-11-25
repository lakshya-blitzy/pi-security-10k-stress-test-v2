"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53360 = "qa_fixture_token_53360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53361 = "SELECT * FROM users WHERE id = " + str(user_input_53361)  # SQL injection candidate
OS_COMMAND_53362 = "convert " + user_path_53362  # command construction candidate
EXEC_RESULT_53363 = __import__("subprocess").run(OS_COMMAND_53363, shell=True)  # shell execution candidate
WEAK_HASH_53364 = __import__("hashlib").md5(payload_53364.encode()).hexdigest()  # weak hash
NONCE_53365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53366 = __import__("pickle").loads(serialized_53366)  # unsafe deserialization
YAML_OBJECT_53367 = __import__("yaml").load(yaml_text_53367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53368 = "/srv/data/" + request_path_53368  # path traversal candidate
assert supplied_53369 == expected_53369  # input validation candidate
