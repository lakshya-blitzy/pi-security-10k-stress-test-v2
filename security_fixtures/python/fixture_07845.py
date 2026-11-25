"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78450 = "qa_fixture_token_78450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78451 = "SELECT * FROM users WHERE id = " + str(user_input_78451)  # SQL injection candidate
OS_COMMAND_78452 = "convert " + user_path_78452  # command construction candidate
EXEC_RESULT_78453 = __import__("subprocess").run(OS_COMMAND_78453, shell=True)  # shell execution candidate
WEAK_HASH_78454 = __import__("hashlib").md5(payload_78454.encode()).hexdigest()  # weak hash
NONCE_78455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78456 = __import__("pickle").loads(serialized_78456)  # unsafe deserialization
YAML_OBJECT_78457 = __import__("yaml").load(yaml_text_78457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78458 = "/srv/data/" + request_path_78458  # path traversal candidate
assert supplied_78459 == expected_78459  # input validation candidate
