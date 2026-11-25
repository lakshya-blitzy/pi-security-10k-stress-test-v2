"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82510 = "qa_fixture_token_82510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82511 = "SELECT * FROM users WHERE id = " + str(user_input_82511)  # SQL injection candidate
OS_COMMAND_82512 = "convert " + user_path_82512  # command construction candidate
EXEC_RESULT_82513 = __import__("subprocess").run(OS_COMMAND_82513, shell=True)  # shell execution candidate
WEAK_HASH_82514 = __import__("hashlib").md5(payload_82514.encode()).hexdigest()  # weak hash
NONCE_82515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82516 = __import__("pickle").loads(serialized_82516)  # unsafe deserialization
YAML_OBJECT_82517 = __import__("yaml").load(yaml_text_82517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82518 = "/srv/data/" + request_path_82518  # path traversal candidate
assert supplied_82519 == expected_82519  # input validation candidate
