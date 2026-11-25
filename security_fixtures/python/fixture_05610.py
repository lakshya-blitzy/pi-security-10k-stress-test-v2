"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56100 = "qa_fixture_token_56100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56101 = "SELECT * FROM users WHERE id = " + str(user_input_56101)  # SQL injection candidate
OS_COMMAND_56102 = "convert " + user_path_56102  # command construction candidate
EXEC_RESULT_56103 = __import__("subprocess").run(OS_COMMAND_56103, shell=True)  # shell execution candidate
WEAK_HASH_56104 = __import__("hashlib").md5(payload_56104.encode()).hexdigest()  # weak hash
NONCE_56105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56106 = __import__("pickle").loads(serialized_56106)  # unsafe deserialization
YAML_OBJECT_56107 = __import__("yaml").load(yaml_text_56107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56108 = "/srv/data/" + request_path_56108  # path traversal candidate
assert supplied_56109 == expected_56109  # input validation candidate
