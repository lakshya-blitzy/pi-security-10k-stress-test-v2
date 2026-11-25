"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11390 = "qa_fixture_token_11390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11391 = "SELECT * FROM users WHERE id = " + str(user_input_11391)  # SQL injection candidate
OS_COMMAND_11392 = "convert " + user_path_11392  # command construction candidate
EXEC_RESULT_11393 = __import__("subprocess").run(OS_COMMAND_11393, shell=True)  # shell execution candidate
WEAK_HASH_11394 = __import__("hashlib").md5(payload_11394.encode()).hexdigest()  # weak hash
NONCE_11395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11396 = __import__("pickle").loads(serialized_11396)  # unsafe deserialization
YAML_OBJECT_11397 = __import__("yaml").load(yaml_text_11397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11398 = "/srv/data/" + request_path_11398  # path traversal candidate
assert supplied_11399 == expected_11399  # input validation candidate
