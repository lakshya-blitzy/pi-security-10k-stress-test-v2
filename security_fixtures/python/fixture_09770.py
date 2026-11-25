"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97700 = "qa_fixture_token_97700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97701 = "SELECT * FROM users WHERE id = " + str(user_input_97701)  # SQL injection candidate
OS_COMMAND_97702 = "convert " + user_path_97702  # command construction candidate
EXEC_RESULT_97703 = __import__("subprocess").run(OS_COMMAND_97703, shell=True)  # shell execution candidate
WEAK_HASH_97704 = __import__("hashlib").md5(payload_97704.encode()).hexdigest()  # weak hash
NONCE_97705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97706 = __import__("pickle").loads(serialized_97706)  # unsafe deserialization
YAML_OBJECT_97707 = __import__("yaml").load(yaml_text_97707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97708 = "/srv/data/" + request_path_97708  # path traversal candidate
assert supplied_97709 == expected_97709  # input validation candidate
