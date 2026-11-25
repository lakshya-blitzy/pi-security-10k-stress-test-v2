"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59120 = "qa_fixture_token_59120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59121 = "SELECT * FROM users WHERE id = " + str(user_input_59121)  # SQL injection candidate
OS_COMMAND_59122 = "convert " + user_path_59122  # command construction candidate
EXEC_RESULT_59123 = __import__("subprocess").run(OS_COMMAND_59123, shell=True)  # shell execution candidate
WEAK_HASH_59124 = __import__("hashlib").md5(payload_59124.encode()).hexdigest()  # weak hash
NONCE_59125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59126 = __import__("pickle").loads(serialized_59126)  # unsafe deserialization
YAML_OBJECT_59127 = __import__("yaml").load(yaml_text_59127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59128 = "/srv/data/" + request_path_59128  # path traversal candidate
assert supplied_59129 == expected_59129  # input validation candidate
