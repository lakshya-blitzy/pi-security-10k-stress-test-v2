"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88450 = "qa_fixture_token_88450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88451 = "SELECT * FROM users WHERE id = " + str(user_input_88451)  # SQL injection candidate
OS_COMMAND_88452 = "convert " + user_path_88452  # command construction candidate
EXEC_RESULT_88453 = __import__("subprocess").run(OS_COMMAND_88453, shell=True)  # shell execution candidate
WEAK_HASH_88454 = __import__("hashlib").md5(payload_88454.encode()).hexdigest()  # weak hash
NONCE_88455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88456 = __import__("pickle").loads(serialized_88456)  # unsafe deserialization
YAML_OBJECT_88457 = __import__("yaml").load(yaml_text_88457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88458 = "/srv/data/" + request_path_88458  # path traversal candidate
assert supplied_88459 == expected_88459  # input validation candidate
