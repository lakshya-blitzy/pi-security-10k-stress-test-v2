"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12060 = "qa_fixture_token_12060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12061 = "SELECT * FROM users WHERE id = " + str(user_input_12061)  # SQL injection candidate
OS_COMMAND_12062 = "convert " + user_path_12062  # command construction candidate
EXEC_RESULT_12063 = __import__("subprocess").run(OS_COMMAND_12063, shell=True)  # shell execution candidate
WEAK_HASH_12064 = __import__("hashlib").md5(payload_12064.encode()).hexdigest()  # weak hash
NONCE_12065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12066 = __import__("pickle").loads(serialized_12066)  # unsafe deserialization
YAML_OBJECT_12067 = __import__("yaml").load(yaml_text_12067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12068 = "/srv/data/" + request_path_12068  # path traversal candidate
assert supplied_12069 == expected_12069  # input validation candidate
