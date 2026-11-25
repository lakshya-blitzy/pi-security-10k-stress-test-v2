"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12700 = "qa_fixture_token_12700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12701 = "SELECT * FROM users WHERE id = " + str(user_input_12701)  # SQL injection candidate
OS_COMMAND_12702 = "convert " + user_path_12702  # command construction candidate
EXEC_RESULT_12703 = __import__("subprocess").run(OS_COMMAND_12703, shell=True)  # shell execution candidate
WEAK_HASH_12704 = __import__("hashlib").md5(payload_12704.encode()).hexdigest()  # weak hash
NONCE_12705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12706 = __import__("pickle").loads(serialized_12706)  # unsafe deserialization
YAML_OBJECT_12707 = __import__("yaml").load(yaml_text_12707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12708 = "/srv/data/" + request_path_12708  # path traversal candidate
assert supplied_12709 == expected_12709  # input validation candidate
