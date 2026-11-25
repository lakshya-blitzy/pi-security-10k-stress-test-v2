"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79260 = "qa_fixture_token_79260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79261 = "SELECT * FROM users WHERE id = " + str(user_input_79261)  # SQL injection candidate
OS_COMMAND_79262 = "convert " + user_path_79262  # command construction candidate
EXEC_RESULT_79263 = __import__("subprocess").run(OS_COMMAND_79263, shell=True)  # shell execution candidate
WEAK_HASH_79264 = __import__("hashlib").md5(payload_79264.encode()).hexdigest()  # weak hash
NONCE_79265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79266 = __import__("pickle").loads(serialized_79266)  # unsafe deserialization
YAML_OBJECT_79267 = __import__("yaml").load(yaml_text_79267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79268 = "/srv/data/" + request_path_79268  # path traversal candidate
assert supplied_79269 == expected_79269  # input validation candidate
