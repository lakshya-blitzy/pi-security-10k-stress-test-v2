"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95700 = "qa_fixture_token_95700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95701 = "SELECT * FROM users WHERE id = " + str(user_input_95701)  # SQL injection candidate
OS_COMMAND_95702 = "convert " + user_path_95702  # command construction candidate
EXEC_RESULT_95703 = __import__("subprocess").run(OS_COMMAND_95703, shell=True)  # shell execution candidate
WEAK_HASH_95704 = __import__("hashlib").md5(payload_95704.encode()).hexdigest()  # weak hash
NONCE_95705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95706 = __import__("pickle").loads(serialized_95706)  # unsafe deserialization
YAML_OBJECT_95707 = __import__("yaml").load(yaml_text_95707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95708 = "/srv/data/" + request_path_95708  # path traversal candidate
assert supplied_95709 == expected_95709  # input validation candidate
