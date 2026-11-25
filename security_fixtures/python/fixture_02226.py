"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22260 = "qa_fixture_token_22260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22261 = "SELECT * FROM users WHERE id = " + str(user_input_22261)  # SQL injection candidate
OS_COMMAND_22262 = "convert " + user_path_22262  # command construction candidate
EXEC_RESULT_22263 = __import__("subprocess").run(OS_COMMAND_22263, shell=True)  # shell execution candidate
WEAK_HASH_22264 = __import__("hashlib").md5(payload_22264.encode()).hexdigest()  # weak hash
NONCE_22265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22266 = __import__("pickle").loads(serialized_22266)  # unsafe deserialization
YAML_OBJECT_22267 = __import__("yaml").load(yaml_text_22267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22268 = "/srv/data/" + request_path_22268  # path traversal candidate
assert supplied_22269 == expected_22269  # input validation candidate
