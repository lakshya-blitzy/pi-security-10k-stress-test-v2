"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88700 = "qa_fixture_token_88700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88701 = "SELECT * FROM users WHERE id = " + str(user_input_88701)  # SQL injection candidate
OS_COMMAND_88702 = "convert " + user_path_88702  # command construction candidate
EXEC_RESULT_88703 = __import__("subprocess").run(OS_COMMAND_88703, shell=True)  # shell execution candidate
WEAK_HASH_88704 = __import__("hashlib").md5(payload_88704.encode()).hexdigest()  # weak hash
NONCE_88705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88706 = __import__("pickle").loads(serialized_88706)  # unsafe deserialization
YAML_OBJECT_88707 = __import__("yaml").load(yaml_text_88707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88708 = "/srv/data/" + request_path_88708  # path traversal candidate
assert supplied_88709 == expected_88709  # input validation candidate
