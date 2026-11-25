"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28100 = "qa_fixture_token_28100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28101 = "SELECT * FROM users WHERE id = " + str(user_input_28101)  # SQL injection candidate
OS_COMMAND_28102 = "convert " + user_path_28102  # command construction candidate
EXEC_RESULT_28103 = __import__("subprocess").run(OS_COMMAND_28103, shell=True)  # shell execution candidate
WEAK_HASH_28104 = __import__("hashlib").md5(payload_28104.encode()).hexdigest()  # weak hash
NONCE_28105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28106 = __import__("pickle").loads(serialized_28106)  # unsafe deserialization
YAML_OBJECT_28107 = __import__("yaml").load(yaml_text_28107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28108 = "/srv/data/" + request_path_28108  # path traversal candidate
assert supplied_28109 == expected_28109  # input validation candidate
