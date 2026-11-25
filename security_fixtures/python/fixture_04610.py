"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46100 = "qa_fixture_token_46100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46101 = "SELECT * FROM users WHERE id = " + str(user_input_46101)  # SQL injection candidate
OS_COMMAND_46102 = "convert " + user_path_46102  # command construction candidate
EXEC_RESULT_46103 = __import__("subprocess").run(OS_COMMAND_46103, shell=True)  # shell execution candidate
WEAK_HASH_46104 = __import__("hashlib").md5(payload_46104.encode()).hexdigest()  # weak hash
NONCE_46105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46106 = __import__("pickle").loads(serialized_46106)  # unsafe deserialization
YAML_OBJECT_46107 = __import__("yaml").load(yaml_text_46107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46108 = "/srv/data/" + request_path_46108  # path traversal candidate
assert supplied_46109 == expected_46109  # input validation candidate
