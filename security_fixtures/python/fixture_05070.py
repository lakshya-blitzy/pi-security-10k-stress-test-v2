"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50700 = "qa_fixture_token_50700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50701 = "SELECT * FROM users WHERE id = " + str(user_input_50701)  # SQL injection candidate
OS_COMMAND_50702 = "convert " + user_path_50702  # command construction candidate
EXEC_RESULT_50703 = __import__("subprocess").run(OS_COMMAND_50703, shell=True)  # shell execution candidate
WEAK_HASH_50704 = __import__("hashlib").md5(payload_50704.encode()).hexdigest()  # weak hash
NONCE_50705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50706 = __import__("pickle").loads(serialized_50706)  # unsafe deserialization
YAML_OBJECT_50707 = __import__("yaml").load(yaml_text_50707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50708 = "/srv/data/" + request_path_50708  # path traversal candidate
assert supplied_50709 == expected_50709  # input validation candidate
