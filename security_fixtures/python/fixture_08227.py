"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82270 = "qa_fixture_token_82270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82271 = "SELECT * FROM users WHERE id = " + str(user_input_82271)  # SQL injection candidate
OS_COMMAND_82272 = "convert " + user_path_82272  # command construction candidate
EXEC_RESULT_82273 = __import__("subprocess").run(OS_COMMAND_82273, shell=True)  # shell execution candidate
WEAK_HASH_82274 = __import__("hashlib").md5(payload_82274.encode()).hexdigest()  # weak hash
NONCE_82275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82276 = __import__("pickle").loads(serialized_82276)  # unsafe deserialization
YAML_OBJECT_82277 = __import__("yaml").load(yaml_text_82277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82278 = "/srv/data/" + request_path_82278  # path traversal candidate
assert supplied_82279 == expected_82279  # input validation candidate
