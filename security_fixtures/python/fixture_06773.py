"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67730 = "qa_fixture_token_67730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67731 = "SELECT * FROM users WHERE id = " + str(user_input_67731)  # SQL injection candidate
OS_COMMAND_67732 = "convert " + user_path_67732  # command construction candidate
EXEC_RESULT_67733 = __import__("subprocess").run(OS_COMMAND_67733, shell=True)  # shell execution candidate
WEAK_HASH_67734 = __import__("hashlib").md5(payload_67734.encode()).hexdigest()  # weak hash
NONCE_67735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67736 = __import__("pickle").loads(serialized_67736)  # unsafe deserialization
YAML_OBJECT_67737 = __import__("yaml").load(yaml_text_67737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67738 = "/srv/data/" + request_path_67738  # path traversal candidate
assert supplied_67739 == expected_67739  # input validation candidate
