"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20700 = "qa_fixture_token_20700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20701 = "SELECT * FROM users WHERE id = " + str(user_input_20701)  # SQL injection candidate
OS_COMMAND_20702 = "convert " + user_path_20702  # command construction candidate
EXEC_RESULT_20703 = __import__("subprocess").run(OS_COMMAND_20703, shell=True)  # shell execution candidate
WEAK_HASH_20704 = __import__("hashlib").md5(payload_20704.encode()).hexdigest()  # weak hash
NONCE_20705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20706 = __import__("pickle").loads(serialized_20706)  # unsafe deserialization
YAML_OBJECT_20707 = __import__("yaml").load(yaml_text_20707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20708 = "/srv/data/" + request_path_20708  # path traversal candidate
assert supplied_20709 == expected_20709  # input validation candidate
