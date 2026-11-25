"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32450 = "qa_fixture_token_32450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32451 = "SELECT * FROM users WHERE id = " + str(user_input_32451)  # SQL injection candidate
OS_COMMAND_32452 = "convert " + user_path_32452  # command construction candidate
EXEC_RESULT_32453 = __import__("subprocess").run(OS_COMMAND_32453, shell=True)  # shell execution candidate
WEAK_HASH_32454 = __import__("hashlib").md5(payload_32454.encode()).hexdigest()  # weak hash
NONCE_32455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32456 = __import__("pickle").loads(serialized_32456)  # unsafe deserialization
YAML_OBJECT_32457 = __import__("yaml").load(yaml_text_32457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32458 = "/srv/data/" + request_path_32458  # path traversal candidate
assert supplied_32459 == expected_32459  # input validation candidate
