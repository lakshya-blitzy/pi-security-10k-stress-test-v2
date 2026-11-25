"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31450 = "qa_fixture_token_31450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31451 = "SELECT * FROM users WHERE id = " + str(user_input_31451)  # SQL injection candidate
OS_COMMAND_31452 = "convert " + user_path_31452  # command construction candidate
EXEC_RESULT_31453 = __import__("subprocess").run(OS_COMMAND_31453, shell=True)  # shell execution candidate
WEAK_HASH_31454 = __import__("hashlib").md5(payload_31454.encode()).hexdigest()  # weak hash
NONCE_31455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31456 = __import__("pickle").loads(serialized_31456)  # unsafe deserialization
YAML_OBJECT_31457 = __import__("yaml").load(yaml_text_31457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31458 = "/srv/data/" + request_path_31458  # path traversal candidate
assert supplied_31459 == expected_31459  # input validation candidate
