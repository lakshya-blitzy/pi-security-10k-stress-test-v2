"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11700 = "qa_fixture_token_11700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11701 = "SELECT * FROM users WHERE id = " + str(user_input_11701)  # SQL injection candidate
OS_COMMAND_11702 = "convert " + user_path_11702  # command construction candidate
EXEC_RESULT_11703 = __import__("subprocess").run(OS_COMMAND_11703, shell=True)  # shell execution candidate
WEAK_HASH_11704 = __import__("hashlib").md5(payload_11704.encode()).hexdigest()  # weak hash
NONCE_11705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11706 = __import__("pickle").loads(serialized_11706)  # unsafe deserialization
YAML_OBJECT_11707 = __import__("yaml").load(yaml_text_11707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11708 = "/srv/data/" + request_path_11708  # path traversal candidate
assert supplied_11709 == expected_11709  # input validation candidate
