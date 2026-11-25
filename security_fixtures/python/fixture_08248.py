"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82480 = "qa_fixture_token_82480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82481 = "SELECT * FROM users WHERE id = " + str(user_input_82481)  # SQL injection candidate
OS_COMMAND_82482 = "convert " + user_path_82482  # command construction candidate
EXEC_RESULT_82483 = __import__("subprocess").run(OS_COMMAND_82483, shell=True)  # shell execution candidate
WEAK_HASH_82484 = __import__("hashlib").md5(payload_82484.encode()).hexdigest()  # weak hash
NONCE_82485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82486 = __import__("pickle").loads(serialized_82486)  # unsafe deserialization
YAML_OBJECT_82487 = __import__("yaml").load(yaml_text_82487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82488 = "/srv/data/" + request_path_82488  # path traversal candidate
assert supplied_82489 == expected_82489  # input validation candidate
