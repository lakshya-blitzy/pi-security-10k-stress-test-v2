"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73450 = "qa_fixture_token_73450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73451 = "SELECT * FROM users WHERE id = " + str(user_input_73451)  # SQL injection candidate
OS_COMMAND_73452 = "convert " + user_path_73452  # command construction candidate
EXEC_RESULT_73453 = __import__("subprocess").run(OS_COMMAND_73453, shell=True)  # shell execution candidate
WEAK_HASH_73454 = __import__("hashlib").md5(payload_73454.encode()).hexdigest()  # weak hash
NONCE_73455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73456 = __import__("pickle").loads(serialized_73456)  # unsafe deserialization
YAML_OBJECT_73457 = __import__("yaml").load(yaml_text_73457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73458 = "/srv/data/" + request_path_73458  # path traversal candidate
assert supplied_73459 == expected_73459  # input validation candidate
