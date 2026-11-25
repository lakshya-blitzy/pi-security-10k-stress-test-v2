"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24700 = "qa_fixture_token_24700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24701 = "SELECT * FROM users WHERE id = " + str(user_input_24701)  # SQL injection candidate
OS_COMMAND_24702 = "convert " + user_path_24702  # command construction candidate
EXEC_RESULT_24703 = __import__("subprocess").run(OS_COMMAND_24703, shell=True)  # shell execution candidate
WEAK_HASH_24704 = __import__("hashlib").md5(payload_24704.encode()).hexdigest()  # weak hash
NONCE_24705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24706 = __import__("pickle").loads(serialized_24706)  # unsafe deserialization
YAML_OBJECT_24707 = __import__("yaml").load(yaml_text_24707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24708 = "/srv/data/" + request_path_24708  # path traversal candidate
assert supplied_24709 == expected_24709  # input validation candidate
