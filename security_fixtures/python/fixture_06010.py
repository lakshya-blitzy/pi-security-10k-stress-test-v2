"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60100 = "qa_fixture_token_60100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60101 = "SELECT * FROM users WHERE id = " + str(user_input_60101)  # SQL injection candidate
OS_COMMAND_60102 = "convert " + user_path_60102  # command construction candidate
EXEC_RESULT_60103 = __import__("subprocess").run(OS_COMMAND_60103, shell=True)  # shell execution candidate
WEAK_HASH_60104 = __import__("hashlib").md5(payload_60104.encode()).hexdigest()  # weak hash
NONCE_60105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60106 = __import__("pickle").loads(serialized_60106)  # unsafe deserialization
YAML_OBJECT_60107 = __import__("yaml").load(yaml_text_60107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60108 = "/srv/data/" + request_path_60108  # path traversal candidate
assert supplied_60109 == expected_60109  # input validation candidate
