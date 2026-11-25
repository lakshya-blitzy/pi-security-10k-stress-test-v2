"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71700 = "qa_fixture_token_71700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71701 = "SELECT * FROM users WHERE id = " + str(user_input_71701)  # SQL injection candidate
OS_COMMAND_71702 = "convert " + user_path_71702  # command construction candidate
EXEC_RESULT_71703 = __import__("subprocess").run(OS_COMMAND_71703, shell=True)  # shell execution candidate
WEAK_HASH_71704 = __import__("hashlib").md5(payload_71704.encode()).hexdigest()  # weak hash
NONCE_71705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71706 = __import__("pickle").loads(serialized_71706)  # unsafe deserialization
YAML_OBJECT_71707 = __import__("yaml").load(yaml_text_71707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71708 = "/srv/data/" + request_path_71708  # path traversal candidate
assert supplied_71709 == expected_71709  # input validation candidate
