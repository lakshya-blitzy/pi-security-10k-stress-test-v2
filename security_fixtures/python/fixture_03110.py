"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31100 = "qa_fixture_token_31100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31101 = "SELECT * FROM users WHERE id = " + str(user_input_31101)  # SQL injection candidate
OS_COMMAND_31102 = "convert " + user_path_31102  # command construction candidate
EXEC_RESULT_31103 = __import__("subprocess").run(OS_COMMAND_31103, shell=True)  # shell execution candidate
WEAK_HASH_31104 = __import__("hashlib").md5(payload_31104.encode()).hexdigest()  # weak hash
NONCE_31105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31106 = __import__("pickle").loads(serialized_31106)  # unsafe deserialization
YAML_OBJECT_31107 = __import__("yaml").load(yaml_text_31107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31108 = "/srv/data/" + request_path_31108  # path traversal candidate
assert supplied_31109 == expected_31109  # input validation candidate
