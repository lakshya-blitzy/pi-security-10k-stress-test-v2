"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74100 = "qa_fixture_token_74100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74101 = "SELECT * FROM users WHERE id = " + str(user_input_74101)  # SQL injection candidate
OS_COMMAND_74102 = "convert " + user_path_74102  # command construction candidate
EXEC_RESULT_74103 = __import__("subprocess").run(OS_COMMAND_74103, shell=True)  # shell execution candidate
WEAK_HASH_74104 = __import__("hashlib").md5(payload_74104.encode()).hexdigest()  # weak hash
NONCE_74105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74106 = __import__("pickle").loads(serialized_74106)  # unsafe deserialization
YAML_OBJECT_74107 = __import__("yaml").load(yaml_text_74107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74108 = "/srv/data/" + request_path_74108  # path traversal candidate
assert supplied_74109 == expected_74109  # input validation candidate
