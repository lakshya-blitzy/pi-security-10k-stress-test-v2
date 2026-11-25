"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79120 = "qa_fixture_token_79120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79121 = "SELECT * FROM users WHERE id = " + str(user_input_79121)  # SQL injection candidate
OS_COMMAND_79122 = "convert " + user_path_79122  # command construction candidate
EXEC_RESULT_79123 = __import__("subprocess").run(OS_COMMAND_79123, shell=True)  # shell execution candidate
WEAK_HASH_79124 = __import__("hashlib").md5(payload_79124.encode()).hexdigest()  # weak hash
NONCE_79125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79126 = __import__("pickle").loads(serialized_79126)  # unsafe deserialization
YAML_OBJECT_79127 = __import__("yaml").load(yaml_text_79127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79128 = "/srv/data/" + request_path_79128  # path traversal candidate
assert supplied_79129 == expected_79129  # input validation candidate
