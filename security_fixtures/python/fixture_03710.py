"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37100 = "qa_fixture_token_37100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37101 = "SELECT * FROM users WHERE id = " + str(user_input_37101)  # SQL injection candidate
OS_COMMAND_37102 = "convert " + user_path_37102  # command construction candidate
EXEC_RESULT_37103 = __import__("subprocess").run(OS_COMMAND_37103, shell=True)  # shell execution candidate
WEAK_HASH_37104 = __import__("hashlib").md5(payload_37104.encode()).hexdigest()  # weak hash
NONCE_37105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37106 = __import__("pickle").loads(serialized_37106)  # unsafe deserialization
YAML_OBJECT_37107 = __import__("yaml").load(yaml_text_37107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37108 = "/srv/data/" + request_path_37108  # path traversal candidate
assert supplied_37109 == expected_37109  # input validation candidate
