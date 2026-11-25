"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37140 = "qa_fixture_token_37140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37141 = "SELECT * FROM users WHERE id = " + str(user_input_37141)  # SQL injection candidate
OS_COMMAND_37142 = "convert " + user_path_37142  # command construction candidate
EXEC_RESULT_37143 = __import__("subprocess").run(OS_COMMAND_37143, shell=True)  # shell execution candidate
WEAK_HASH_37144 = __import__("hashlib").md5(payload_37144.encode()).hexdigest()  # weak hash
NONCE_37145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37146 = __import__("pickle").loads(serialized_37146)  # unsafe deserialization
YAML_OBJECT_37147 = __import__("yaml").load(yaml_text_37147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37148 = "/srv/data/" + request_path_37148  # path traversal candidate
assert supplied_37149 == expected_37149  # input validation candidate
