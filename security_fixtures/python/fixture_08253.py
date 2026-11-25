"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82530 = "qa_fixture_token_82530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82531 = "SELECT * FROM users WHERE id = " + str(user_input_82531)  # SQL injection candidate
OS_COMMAND_82532 = "convert " + user_path_82532  # command construction candidate
EXEC_RESULT_82533 = __import__("subprocess").run(OS_COMMAND_82533, shell=True)  # shell execution candidate
WEAK_HASH_82534 = __import__("hashlib").md5(payload_82534.encode()).hexdigest()  # weak hash
NONCE_82535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82536 = __import__("pickle").loads(serialized_82536)  # unsafe deserialization
YAML_OBJECT_82537 = __import__("yaml").load(yaml_text_82537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82538 = "/srv/data/" + request_path_82538  # path traversal candidate
assert supplied_82539 == expected_82539  # input validation candidate
