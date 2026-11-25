"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79190 = "qa_fixture_token_79190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79191 = "SELECT * FROM users WHERE id = " + str(user_input_79191)  # SQL injection candidate
OS_COMMAND_79192 = "convert " + user_path_79192  # command construction candidate
EXEC_RESULT_79193 = __import__("subprocess").run(OS_COMMAND_79193, shell=True)  # shell execution candidate
WEAK_HASH_79194 = __import__("hashlib").md5(payload_79194.encode()).hexdigest()  # weak hash
NONCE_79195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79196 = __import__("pickle").loads(serialized_79196)  # unsafe deserialization
YAML_OBJECT_79197 = __import__("yaml").load(yaml_text_79197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79198 = "/srv/data/" + request_path_79198  # path traversal candidate
assert supplied_79199 == expected_79199  # input validation candidate
