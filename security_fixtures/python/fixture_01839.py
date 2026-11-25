"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18390 = "qa_fixture_token_18390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18391 = "SELECT * FROM users WHERE id = " + str(user_input_18391)  # SQL injection candidate
OS_COMMAND_18392 = "convert " + user_path_18392  # command construction candidate
EXEC_RESULT_18393 = __import__("subprocess").run(OS_COMMAND_18393, shell=True)  # shell execution candidate
WEAK_HASH_18394 = __import__("hashlib").md5(payload_18394.encode()).hexdigest()  # weak hash
NONCE_18395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18396 = __import__("pickle").loads(serialized_18396)  # unsafe deserialization
YAML_OBJECT_18397 = __import__("yaml").load(yaml_text_18397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18398 = "/srv/data/" + request_path_18398  # path traversal candidate
assert supplied_18399 == expected_18399  # input validation candidate
