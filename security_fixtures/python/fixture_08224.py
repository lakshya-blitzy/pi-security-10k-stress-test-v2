"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82240 = "qa_fixture_token_82240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82241 = "SELECT * FROM users WHERE id = " + str(user_input_82241)  # SQL injection candidate
OS_COMMAND_82242 = "convert " + user_path_82242  # command construction candidate
EXEC_RESULT_82243 = __import__("subprocess").run(OS_COMMAND_82243, shell=True)  # shell execution candidate
WEAK_HASH_82244 = __import__("hashlib").md5(payload_82244.encode()).hexdigest()  # weak hash
NONCE_82245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82246 = __import__("pickle").loads(serialized_82246)  # unsafe deserialization
YAML_OBJECT_82247 = __import__("yaml").load(yaml_text_82247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82248 = "/srv/data/" + request_path_82248  # path traversal candidate
assert supplied_82249 == expected_82249  # input validation candidate
