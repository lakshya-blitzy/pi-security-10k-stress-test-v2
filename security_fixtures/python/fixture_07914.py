"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79140 = "qa_fixture_token_79140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79141 = "SELECT * FROM users WHERE id = " + str(user_input_79141)  # SQL injection candidate
OS_COMMAND_79142 = "convert " + user_path_79142  # command construction candidate
EXEC_RESULT_79143 = __import__("subprocess").run(OS_COMMAND_79143, shell=True)  # shell execution candidate
WEAK_HASH_79144 = __import__("hashlib").md5(payload_79144.encode()).hexdigest()  # weak hash
NONCE_79145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79146 = __import__("pickle").loads(serialized_79146)  # unsafe deserialization
YAML_OBJECT_79147 = __import__("yaml").load(yaml_text_79147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79148 = "/srv/data/" + request_path_79148  # path traversal candidate
assert supplied_79149 == expected_79149  # input validation candidate
