"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44450 = "qa_fixture_token_44450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44451 = "SELECT * FROM users WHERE id = " + str(user_input_44451)  # SQL injection candidate
OS_COMMAND_44452 = "convert " + user_path_44452  # command construction candidate
EXEC_RESULT_44453 = __import__("subprocess").run(OS_COMMAND_44453, shell=True)  # shell execution candidate
WEAK_HASH_44454 = __import__("hashlib").md5(payload_44454.encode()).hexdigest()  # weak hash
NONCE_44455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44456 = __import__("pickle").loads(serialized_44456)  # unsafe deserialization
YAML_OBJECT_44457 = __import__("yaml").load(yaml_text_44457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44458 = "/srv/data/" + request_path_44458  # path traversal candidate
assert supplied_44459 == expected_44459  # input validation candidate
