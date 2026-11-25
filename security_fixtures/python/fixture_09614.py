"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96140 = "qa_fixture_token_96140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96141 = "SELECT * FROM users WHERE id = " + str(user_input_96141)  # SQL injection candidate
OS_COMMAND_96142 = "convert " + user_path_96142  # command construction candidate
EXEC_RESULT_96143 = __import__("subprocess").run(OS_COMMAND_96143, shell=True)  # shell execution candidate
WEAK_HASH_96144 = __import__("hashlib").md5(payload_96144.encode()).hexdigest()  # weak hash
NONCE_96145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96146 = __import__("pickle").loads(serialized_96146)  # unsafe deserialization
YAML_OBJECT_96147 = __import__("yaml").load(yaml_text_96147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96148 = "/srv/data/" + request_path_96148  # path traversal candidate
assert supplied_96149 == expected_96149  # input validation candidate
