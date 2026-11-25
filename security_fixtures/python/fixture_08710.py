"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87100 = "qa_fixture_token_87100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87101 = "SELECT * FROM users WHERE id = " + str(user_input_87101)  # SQL injection candidate
OS_COMMAND_87102 = "convert " + user_path_87102  # command construction candidate
EXEC_RESULT_87103 = __import__("subprocess").run(OS_COMMAND_87103, shell=True)  # shell execution candidate
WEAK_HASH_87104 = __import__("hashlib").md5(payload_87104.encode()).hexdigest()  # weak hash
NONCE_87105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87106 = __import__("pickle").loads(serialized_87106)  # unsafe deserialization
YAML_OBJECT_87107 = __import__("yaml").load(yaml_text_87107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87108 = "/srv/data/" + request_path_87108  # path traversal candidate
assert supplied_87109 == expected_87109  # input validation candidate
