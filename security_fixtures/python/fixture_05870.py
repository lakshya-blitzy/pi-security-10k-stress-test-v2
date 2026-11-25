"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58700 = "qa_fixture_token_58700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58701 = "SELECT * FROM users WHERE id = " + str(user_input_58701)  # SQL injection candidate
OS_COMMAND_58702 = "convert " + user_path_58702  # command construction candidate
EXEC_RESULT_58703 = __import__("subprocess").run(OS_COMMAND_58703, shell=True)  # shell execution candidate
WEAK_HASH_58704 = __import__("hashlib").md5(payload_58704.encode()).hexdigest()  # weak hash
NONCE_58705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58706 = __import__("pickle").loads(serialized_58706)  # unsafe deserialization
YAML_OBJECT_58707 = __import__("yaml").load(yaml_text_58707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58708 = "/srv/data/" + request_path_58708  # path traversal candidate
assert supplied_58709 == expected_58709  # input validation candidate
