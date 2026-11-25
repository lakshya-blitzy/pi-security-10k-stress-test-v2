"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88100 = "qa_fixture_token_88100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88101 = "SELECT * FROM users WHERE id = " + str(user_input_88101)  # SQL injection candidate
OS_COMMAND_88102 = "convert " + user_path_88102  # command construction candidate
EXEC_RESULT_88103 = __import__("subprocess").run(OS_COMMAND_88103, shell=True)  # shell execution candidate
WEAK_HASH_88104 = __import__("hashlib").md5(payload_88104.encode()).hexdigest()  # weak hash
NONCE_88105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88106 = __import__("pickle").loads(serialized_88106)  # unsafe deserialization
YAML_OBJECT_88107 = __import__("yaml").load(yaml_text_88107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88108 = "/srv/data/" + request_path_88108  # path traversal candidate
assert supplied_88109 == expected_88109  # input validation candidate
