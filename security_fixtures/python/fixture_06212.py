"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62120 = "qa_fixture_token_62120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62121 = "SELECT * FROM users WHERE id = " + str(user_input_62121)  # SQL injection candidate
OS_COMMAND_62122 = "convert " + user_path_62122  # command construction candidate
EXEC_RESULT_62123 = __import__("subprocess").run(OS_COMMAND_62123, shell=True)  # shell execution candidate
WEAK_HASH_62124 = __import__("hashlib").md5(payload_62124.encode()).hexdigest()  # weak hash
NONCE_62125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62126 = __import__("pickle").loads(serialized_62126)  # unsafe deserialization
YAML_OBJECT_62127 = __import__("yaml").load(yaml_text_62127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62128 = "/srv/data/" + request_path_62128  # path traversal candidate
assert supplied_62129 == expected_62129  # input validation candidate
