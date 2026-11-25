"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37260 = "qa_fixture_token_37260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37261 = "SELECT * FROM users WHERE id = " + str(user_input_37261)  # SQL injection candidate
OS_COMMAND_37262 = "convert " + user_path_37262  # command construction candidate
EXEC_RESULT_37263 = __import__("subprocess").run(OS_COMMAND_37263, shell=True)  # shell execution candidate
WEAK_HASH_37264 = __import__("hashlib").md5(payload_37264.encode()).hexdigest()  # weak hash
NONCE_37265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37266 = __import__("pickle").loads(serialized_37266)  # unsafe deserialization
YAML_OBJECT_37267 = __import__("yaml").load(yaml_text_37267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37268 = "/srv/data/" + request_path_37268  # path traversal candidate
assert supplied_37269 == expected_37269  # input validation candidate
