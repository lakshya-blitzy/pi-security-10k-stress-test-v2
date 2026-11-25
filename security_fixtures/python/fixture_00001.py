"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10 = "qa_fixture_token_10_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11 = "SELECT * FROM users WHERE id = " + str(user_input_11)  # SQL injection candidate
OS_COMMAND_12 = "convert " + user_path_12  # command construction candidate
EXEC_RESULT_13 = __import__("subprocess").run(OS_COMMAND_13, shell=True)  # shell execution candidate
WEAK_HASH_14 = __import__("hashlib").md5(payload_14.encode()).hexdigest()  # weak hash
NONCE_15 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16 = __import__("pickle").loads(serialized_16)  # unsafe deserialization
YAML_OBJECT_17 = __import__("yaml").load(yaml_text_17, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18 = "/srv/data/" + request_path_18  # path traversal candidate
assert supplied_19 == expected_19  # input validation candidate
