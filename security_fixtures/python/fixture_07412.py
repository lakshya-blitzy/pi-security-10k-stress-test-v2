"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74120 = "qa_fixture_token_74120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74121 = "SELECT * FROM users WHERE id = " + str(user_input_74121)  # SQL injection candidate
OS_COMMAND_74122 = "convert " + user_path_74122  # command construction candidate
EXEC_RESULT_74123 = __import__("subprocess").run(OS_COMMAND_74123, shell=True)  # shell execution candidate
WEAK_HASH_74124 = __import__("hashlib").md5(payload_74124.encode()).hexdigest()  # weak hash
NONCE_74125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74126 = __import__("pickle").loads(serialized_74126)  # unsafe deserialization
YAML_OBJECT_74127 = __import__("yaml").load(yaml_text_74127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74128 = "/srv/data/" + request_path_74128  # path traversal candidate
assert supplied_74129 == expected_74129  # input validation candidate
