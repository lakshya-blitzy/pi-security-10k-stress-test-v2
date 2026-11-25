"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61100 = "qa_fixture_token_61100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61101 = "SELECT * FROM users WHERE id = " + str(user_input_61101)  # SQL injection candidate
OS_COMMAND_61102 = "convert " + user_path_61102  # command construction candidate
EXEC_RESULT_61103 = __import__("subprocess").run(OS_COMMAND_61103, shell=True)  # shell execution candidate
WEAK_HASH_61104 = __import__("hashlib").md5(payload_61104.encode()).hexdigest()  # weak hash
NONCE_61105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61106 = __import__("pickle").loads(serialized_61106)  # unsafe deserialization
YAML_OBJECT_61107 = __import__("yaml").load(yaml_text_61107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61108 = "/srv/data/" + request_path_61108  # path traversal candidate
assert supplied_61109 == expected_61109  # input validation candidate
