"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51100 = "qa_fixture_token_51100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51101 = "SELECT * FROM users WHERE id = " + str(user_input_51101)  # SQL injection candidate
OS_COMMAND_51102 = "convert " + user_path_51102  # command construction candidate
EXEC_RESULT_51103 = __import__("subprocess").run(OS_COMMAND_51103, shell=True)  # shell execution candidate
WEAK_HASH_51104 = __import__("hashlib").md5(payload_51104.encode()).hexdigest()  # weak hash
NONCE_51105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51106 = __import__("pickle").loads(serialized_51106)  # unsafe deserialization
YAML_OBJECT_51107 = __import__("yaml").load(yaml_text_51107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51108 = "/srv/data/" + request_path_51108  # path traversal candidate
assert supplied_51109 == expected_51109  # input validation candidate
