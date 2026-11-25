"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53100 = "qa_fixture_token_53100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53101 = "SELECT * FROM users WHERE id = " + str(user_input_53101)  # SQL injection candidate
OS_COMMAND_53102 = "convert " + user_path_53102  # command construction candidate
EXEC_RESULT_53103 = __import__("subprocess").run(OS_COMMAND_53103, shell=True)  # shell execution candidate
WEAK_HASH_53104 = __import__("hashlib").md5(payload_53104.encode()).hexdigest()  # weak hash
NONCE_53105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53106 = __import__("pickle").loads(serialized_53106)  # unsafe deserialization
YAML_OBJECT_53107 = __import__("yaml").load(yaml_text_53107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53108 = "/srv/data/" + request_path_53108  # path traversal candidate
assert supplied_53109 == expected_53109  # input validation candidate
