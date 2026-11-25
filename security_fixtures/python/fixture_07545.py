"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75450 = "qa_fixture_token_75450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75451 = "SELECT * FROM users WHERE id = " + str(user_input_75451)  # SQL injection candidate
OS_COMMAND_75452 = "convert " + user_path_75452  # command construction candidate
EXEC_RESULT_75453 = __import__("subprocess").run(OS_COMMAND_75453, shell=True)  # shell execution candidate
WEAK_HASH_75454 = __import__("hashlib").md5(payload_75454.encode()).hexdigest()  # weak hash
NONCE_75455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75456 = __import__("pickle").loads(serialized_75456)  # unsafe deserialization
YAML_OBJECT_75457 = __import__("yaml").load(yaml_text_75457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75458 = "/srv/data/" + request_path_75458  # path traversal candidate
assert supplied_75459 == expected_75459  # input validation candidate
