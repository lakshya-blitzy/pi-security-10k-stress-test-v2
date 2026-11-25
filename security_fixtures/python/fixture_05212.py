"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52120 = "qa_fixture_token_52120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52121 = "SELECT * FROM users WHERE id = " + str(user_input_52121)  # SQL injection candidate
OS_COMMAND_52122 = "convert " + user_path_52122  # command construction candidate
EXEC_RESULT_52123 = __import__("subprocess").run(OS_COMMAND_52123, shell=True)  # shell execution candidate
WEAK_HASH_52124 = __import__("hashlib").md5(payload_52124.encode()).hexdigest()  # weak hash
NONCE_52125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52126 = __import__("pickle").loads(serialized_52126)  # unsafe deserialization
YAML_OBJECT_52127 = __import__("yaml").load(yaml_text_52127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52128 = "/srv/data/" + request_path_52128  # path traversal candidate
assert supplied_52129 == expected_52129  # input validation candidate
