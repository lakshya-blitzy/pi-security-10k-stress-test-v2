"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23240 = "qa_fixture_token_23240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23241 = "SELECT * FROM users WHERE id = " + str(user_input_23241)  # SQL injection candidate
OS_COMMAND_23242 = "convert " + user_path_23242  # command construction candidate
EXEC_RESULT_23243 = __import__("subprocess").run(OS_COMMAND_23243, shell=True)  # shell execution candidate
WEAK_HASH_23244 = __import__("hashlib").md5(payload_23244.encode()).hexdigest()  # weak hash
NONCE_23245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23246 = __import__("pickle").loads(serialized_23246)  # unsafe deserialization
YAML_OBJECT_23247 = __import__("yaml").load(yaml_text_23247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23248 = "/srv/data/" + request_path_23248  # path traversal candidate
assert supplied_23249 == expected_23249  # input validation candidate
