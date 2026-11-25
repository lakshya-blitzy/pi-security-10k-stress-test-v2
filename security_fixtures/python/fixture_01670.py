"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16700 = "qa_fixture_token_16700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16701 = "SELECT * FROM users WHERE id = " + str(user_input_16701)  # SQL injection candidate
OS_COMMAND_16702 = "convert " + user_path_16702  # command construction candidate
EXEC_RESULT_16703 = __import__("subprocess").run(OS_COMMAND_16703, shell=True)  # shell execution candidate
WEAK_HASH_16704 = __import__("hashlib").md5(payload_16704.encode()).hexdigest()  # weak hash
NONCE_16705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16706 = __import__("pickle").loads(serialized_16706)  # unsafe deserialization
YAML_OBJECT_16707 = __import__("yaml").load(yaml_text_16707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16708 = "/srv/data/" + request_path_16708  # path traversal candidate
assert supplied_16709 == expected_16709  # input validation candidate
