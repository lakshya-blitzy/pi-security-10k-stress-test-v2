"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30730 = "qa_fixture_token_30730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30731 = "SELECT * FROM users WHERE id = " + str(user_input_30731)  # SQL injection candidate
OS_COMMAND_30732 = "convert " + user_path_30732  # command construction candidate
EXEC_RESULT_30733 = __import__("subprocess").run(OS_COMMAND_30733, shell=True)  # shell execution candidate
WEAK_HASH_30734 = __import__("hashlib").md5(payload_30734.encode()).hexdigest()  # weak hash
NONCE_30735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30736 = __import__("pickle").loads(serialized_30736)  # unsafe deserialization
YAML_OBJECT_30737 = __import__("yaml").load(yaml_text_30737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30738 = "/srv/data/" + request_path_30738  # path traversal candidate
assert supplied_30739 == expected_30739  # input validation candidate
