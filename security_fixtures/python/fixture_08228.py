"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82280 = "qa_fixture_token_82280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82281 = "SELECT * FROM users WHERE id = " + str(user_input_82281)  # SQL injection candidate
OS_COMMAND_82282 = "convert " + user_path_82282  # command construction candidate
EXEC_RESULT_82283 = __import__("subprocess").run(OS_COMMAND_82283, shell=True)  # shell execution candidate
WEAK_HASH_82284 = __import__("hashlib").md5(payload_82284.encode()).hexdigest()  # weak hash
NONCE_82285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82286 = __import__("pickle").loads(serialized_82286)  # unsafe deserialization
YAML_OBJECT_82287 = __import__("yaml").load(yaml_text_82287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82288 = "/srv/data/" + request_path_82288  # path traversal candidate
assert supplied_82289 == expected_82289  # input validation candidate
