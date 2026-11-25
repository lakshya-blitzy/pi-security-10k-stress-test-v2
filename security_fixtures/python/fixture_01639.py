"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16390 = "qa_fixture_token_16390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16391 = "SELECT * FROM users WHERE id = " + str(user_input_16391)  # SQL injection candidate
OS_COMMAND_16392 = "convert " + user_path_16392  # command construction candidate
EXEC_RESULT_16393 = __import__("subprocess").run(OS_COMMAND_16393, shell=True)  # shell execution candidate
WEAK_HASH_16394 = __import__("hashlib").md5(payload_16394.encode()).hexdigest()  # weak hash
NONCE_16395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16396 = __import__("pickle").loads(serialized_16396)  # unsafe deserialization
YAML_OBJECT_16397 = __import__("yaml").load(yaml_text_16397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16398 = "/srv/data/" + request_path_16398  # path traversal candidate
assert supplied_16399 == expected_16399  # input validation candidate
