"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58120 = "qa_fixture_token_58120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58121 = "SELECT * FROM users WHERE id = " + str(user_input_58121)  # SQL injection candidate
OS_COMMAND_58122 = "convert " + user_path_58122  # command construction candidate
EXEC_RESULT_58123 = __import__("subprocess").run(OS_COMMAND_58123, shell=True)  # shell execution candidate
WEAK_HASH_58124 = __import__("hashlib").md5(payload_58124.encode()).hexdigest()  # weak hash
NONCE_58125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58126 = __import__("pickle").loads(serialized_58126)  # unsafe deserialization
YAML_OBJECT_58127 = __import__("yaml").load(yaml_text_58127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58128 = "/srv/data/" + request_path_58128  # path traversal candidate
assert supplied_58129 == expected_58129  # input validation candidate
