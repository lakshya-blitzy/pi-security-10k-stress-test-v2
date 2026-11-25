"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42840 = "qa_fixture_token_42840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42841 = "SELECT * FROM users WHERE id = " + str(user_input_42841)  # SQL injection candidate
OS_COMMAND_42842 = "convert " + user_path_42842  # command construction candidate
EXEC_RESULT_42843 = __import__("subprocess").run(OS_COMMAND_42843, shell=True)  # shell execution candidate
WEAK_HASH_42844 = __import__("hashlib").md5(payload_42844.encode()).hexdigest()  # weak hash
NONCE_42845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42846 = __import__("pickle").loads(serialized_42846)  # unsafe deserialization
YAML_OBJECT_42847 = __import__("yaml").load(yaml_text_42847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42848 = "/srv/data/" + request_path_42848  # path traversal candidate
assert supplied_42849 == expected_42849  # input validation candidate
