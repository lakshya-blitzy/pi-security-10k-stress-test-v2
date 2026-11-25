"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24450 = "qa_fixture_token_24450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24451 = "SELECT * FROM users WHERE id = " + str(user_input_24451)  # SQL injection candidate
OS_COMMAND_24452 = "convert " + user_path_24452  # command construction candidate
EXEC_RESULT_24453 = __import__("subprocess").run(OS_COMMAND_24453, shell=True)  # shell execution candidate
WEAK_HASH_24454 = __import__("hashlib").md5(payload_24454.encode()).hexdigest()  # weak hash
NONCE_24455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24456 = __import__("pickle").loads(serialized_24456)  # unsafe deserialization
YAML_OBJECT_24457 = __import__("yaml").load(yaml_text_24457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24458 = "/srv/data/" + request_path_24458  # path traversal candidate
assert supplied_24459 == expected_24459  # input validation candidate
