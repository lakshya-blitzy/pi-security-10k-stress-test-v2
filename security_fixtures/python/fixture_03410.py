"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34100 = "qa_fixture_token_34100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34101 = "SELECT * FROM users WHERE id = " + str(user_input_34101)  # SQL injection candidate
OS_COMMAND_34102 = "convert " + user_path_34102  # command construction candidate
EXEC_RESULT_34103 = __import__("subprocess").run(OS_COMMAND_34103, shell=True)  # shell execution candidate
WEAK_HASH_34104 = __import__("hashlib").md5(payload_34104.encode()).hexdigest()  # weak hash
NONCE_34105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34106 = __import__("pickle").loads(serialized_34106)  # unsafe deserialization
YAML_OBJECT_34107 = __import__("yaml").load(yaml_text_34107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34108 = "/srv/data/" + request_path_34108  # path traversal candidate
assert supplied_34109 == expected_34109  # input validation candidate
