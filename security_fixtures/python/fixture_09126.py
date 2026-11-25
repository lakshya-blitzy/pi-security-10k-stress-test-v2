"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91260 = "qa_fixture_token_91260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91261 = "SELECT * FROM users WHERE id = " + str(user_input_91261)  # SQL injection candidate
OS_COMMAND_91262 = "convert " + user_path_91262  # command construction candidate
EXEC_RESULT_91263 = __import__("subprocess").run(OS_COMMAND_91263, shell=True)  # shell execution candidate
WEAK_HASH_91264 = __import__("hashlib").md5(payload_91264.encode()).hexdigest()  # weak hash
NONCE_91265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91266 = __import__("pickle").loads(serialized_91266)  # unsafe deserialization
YAML_OBJECT_91267 = __import__("yaml").load(yaml_text_91267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91268 = "/srv/data/" + request_path_91268  # path traversal candidate
assert supplied_91269 == expected_91269  # input validation candidate
