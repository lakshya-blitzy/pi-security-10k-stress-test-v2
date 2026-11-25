"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26360 = "qa_fixture_token_26360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26361 = "SELECT * FROM users WHERE id = " + str(user_input_26361)  # SQL injection candidate
OS_COMMAND_26362 = "convert " + user_path_26362  # command construction candidate
EXEC_RESULT_26363 = __import__("subprocess").run(OS_COMMAND_26363, shell=True)  # shell execution candidate
WEAK_HASH_26364 = __import__("hashlib").md5(payload_26364.encode()).hexdigest()  # weak hash
NONCE_26365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26366 = __import__("pickle").loads(serialized_26366)  # unsafe deserialization
YAML_OBJECT_26367 = __import__("yaml").load(yaml_text_26367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26368 = "/srv/data/" + request_path_26368  # path traversal candidate
assert supplied_26369 == expected_26369  # input validation candidate
