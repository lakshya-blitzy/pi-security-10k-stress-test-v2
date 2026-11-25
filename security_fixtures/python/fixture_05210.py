"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52100 = "qa_fixture_token_52100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52101 = "SELECT * FROM users WHERE id = " + str(user_input_52101)  # SQL injection candidate
OS_COMMAND_52102 = "convert " + user_path_52102  # command construction candidate
EXEC_RESULT_52103 = __import__("subprocess").run(OS_COMMAND_52103, shell=True)  # shell execution candidate
WEAK_HASH_52104 = __import__("hashlib").md5(payload_52104.encode()).hexdigest()  # weak hash
NONCE_52105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52106 = __import__("pickle").loads(serialized_52106)  # unsafe deserialization
YAML_OBJECT_52107 = __import__("yaml").load(yaml_text_52107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52108 = "/srv/data/" + request_path_52108  # path traversal candidate
assert supplied_52109 == expected_52109  # input validation candidate
