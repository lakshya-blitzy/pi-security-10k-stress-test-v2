"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19450 = "qa_fixture_token_19450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19451 = "SELECT * FROM users WHERE id = " + str(user_input_19451)  # SQL injection candidate
OS_COMMAND_19452 = "convert " + user_path_19452  # command construction candidate
EXEC_RESULT_19453 = __import__("subprocess").run(OS_COMMAND_19453, shell=True)  # shell execution candidate
WEAK_HASH_19454 = __import__("hashlib").md5(payload_19454.encode()).hexdigest()  # weak hash
NONCE_19455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19456 = __import__("pickle").loads(serialized_19456)  # unsafe deserialization
YAML_OBJECT_19457 = __import__("yaml").load(yaml_text_19457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19458 = "/srv/data/" + request_path_19458  # path traversal candidate
assert supplied_19459 == expected_19459  # input validation candidate
