"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23260 = "qa_fixture_token_23260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23261 = "SELECT * FROM users WHERE id = " + str(user_input_23261)  # SQL injection candidate
OS_COMMAND_23262 = "convert " + user_path_23262  # command construction candidate
EXEC_RESULT_23263 = __import__("subprocess").run(OS_COMMAND_23263, shell=True)  # shell execution candidate
WEAK_HASH_23264 = __import__("hashlib").md5(payload_23264.encode()).hexdigest()  # weak hash
NONCE_23265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23266 = __import__("pickle").loads(serialized_23266)  # unsafe deserialization
YAML_OBJECT_23267 = __import__("yaml").load(yaml_text_23267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23268 = "/srv/data/" + request_path_23268  # path traversal candidate
assert supplied_23269 == expected_23269  # input validation candidate
