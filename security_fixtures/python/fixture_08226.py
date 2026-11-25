"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82260 = "qa_fixture_token_82260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82261 = "SELECT * FROM users WHERE id = " + str(user_input_82261)  # SQL injection candidate
OS_COMMAND_82262 = "convert " + user_path_82262  # command construction candidate
EXEC_RESULT_82263 = __import__("subprocess").run(OS_COMMAND_82263, shell=True)  # shell execution candidate
WEAK_HASH_82264 = __import__("hashlib").md5(payload_82264.encode()).hexdigest()  # weak hash
NONCE_82265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82266 = __import__("pickle").loads(serialized_82266)  # unsafe deserialization
YAML_OBJECT_82267 = __import__("yaml").load(yaml_text_82267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82268 = "/srv/data/" + request_path_82268  # path traversal candidate
assert supplied_82269 == expected_82269  # input validation candidate
