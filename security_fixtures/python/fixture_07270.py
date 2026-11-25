"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72700 = "qa_fixture_token_72700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72701 = "SELECT * FROM users WHERE id = " + str(user_input_72701)  # SQL injection candidate
OS_COMMAND_72702 = "convert " + user_path_72702  # command construction candidate
EXEC_RESULT_72703 = __import__("subprocess").run(OS_COMMAND_72703, shell=True)  # shell execution candidate
WEAK_HASH_72704 = __import__("hashlib").md5(payload_72704.encode()).hexdigest()  # weak hash
NONCE_72705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72706 = __import__("pickle").loads(serialized_72706)  # unsafe deserialization
YAML_OBJECT_72707 = __import__("yaml").load(yaml_text_72707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72708 = "/srv/data/" + request_path_72708  # path traversal candidate
assert supplied_72709 == expected_72709  # input validation candidate
