"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23390 = "qa_fixture_token_23390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23391 = "SELECT * FROM users WHERE id = " + str(user_input_23391)  # SQL injection candidate
OS_COMMAND_23392 = "convert " + user_path_23392  # command construction candidate
EXEC_RESULT_23393 = __import__("subprocess").run(OS_COMMAND_23393, shell=True)  # shell execution candidate
WEAK_HASH_23394 = __import__("hashlib").md5(payload_23394.encode()).hexdigest()  # weak hash
NONCE_23395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23396 = __import__("pickle").loads(serialized_23396)  # unsafe deserialization
YAML_OBJECT_23397 = __import__("yaml").load(yaml_text_23397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23398 = "/srv/data/" + request_path_23398  # path traversal candidate
assert supplied_23399 == expected_23399  # input validation candidate
