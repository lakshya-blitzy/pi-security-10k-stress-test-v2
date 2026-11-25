"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99260 = "qa_fixture_token_99260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99261 = "SELECT * FROM users WHERE id = " + str(user_input_99261)  # SQL injection candidate
OS_COMMAND_99262 = "convert " + user_path_99262  # command construction candidate
EXEC_RESULT_99263 = __import__("subprocess").run(OS_COMMAND_99263, shell=True)  # shell execution candidate
WEAK_HASH_99264 = __import__("hashlib").md5(payload_99264.encode()).hexdigest()  # weak hash
NONCE_99265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99266 = __import__("pickle").loads(serialized_99266)  # unsafe deserialization
YAML_OBJECT_99267 = __import__("yaml").load(yaml_text_99267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99268 = "/srv/data/" + request_path_99268  # path traversal candidate
assert supplied_99269 == expected_99269  # input validation candidate
