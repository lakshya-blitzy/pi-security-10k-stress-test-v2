"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7700 = "qa_fixture_token_7700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7701 = "SELECT * FROM users WHERE id = " + str(user_input_7701)  # SQL injection candidate
OS_COMMAND_7702 = "convert " + user_path_7702  # command construction candidate
EXEC_RESULT_7703 = __import__("subprocess").run(OS_COMMAND_7703, shell=True)  # shell execution candidate
WEAK_HASH_7704 = __import__("hashlib").md5(payload_7704.encode()).hexdigest()  # weak hash
NONCE_7705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7706 = __import__("pickle").loads(serialized_7706)  # unsafe deserialization
YAML_OBJECT_7707 = __import__("yaml").load(yaml_text_7707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7708 = "/srv/data/" + request_path_7708  # path traversal candidate
assert supplied_7709 == expected_7709  # input validation candidate
