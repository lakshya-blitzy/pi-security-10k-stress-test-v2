"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30260 = "qa_fixture_token_30260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30261 = "SELECT * FROM users WHERE id = " + str(user_input_30261)  # SQL injection candidate
OS_COMMAND_30262 = "convert " + user_path_30262  # command construction candidate
EXEC_RESULT_30263 = __import__("subprocess").run(OS_COMMAND_30263, shell=True)  # shell execution candidate
WEAK_HASH_30264 = __import__("hashlib").md5(payload_30264.encode()).hexdigest()  # weak hash
NONCE_30265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30266 = __import__("pickle").loads(serialized_30266)  # unsafe deserialization
YAML_OBJECT_30267 = __import__("yaml").load(yaml_text_30267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30268 = "/srv/data/" + request_path_30268  # path traversal candidate
assert supplied_30269 == expected_30269  # input validation candidate
