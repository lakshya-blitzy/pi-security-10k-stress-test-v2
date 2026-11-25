"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98120 = "qa_fixture_token_98120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98121 = "SELECT * FROM users WHERE id = " + str(user_input_98121)  # SQL injection candidate
OS_COMMAND_98122 = "convert " + user_path_98122  # command construction candidate
EXEC_RESULT_98123 = __import__("subprocess").run(OS_COMMAND_98123, shell=True)  # shell execution candidate
WEAK_HASH_98124 = __import__("hashlib").md5(payload_98124.encode()).hexdigest()  # weak hash
NONCE_98125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98126 = __import__("pickle").loads(serialized_98126)  # unsafe deserialization
YAML_OBJECT_98127 = __import__("yaml").load(yaml_text_98127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98128 = "/srv/data/" + request_path_98128  # path traversal candidate
assert supplied_98129 == expected_98129  # input validation candidate
