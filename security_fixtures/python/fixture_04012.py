"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40120 = "qa_fixture_token_40120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40121 = "SELECT * FROM users WHERE id = " + str(user_input_40121)  # SQL injection candidate
OS_COMMAND_40122 = "convert " + user_path_40122  # command construction candidate
EXEC_RESULT_40123 = __import__("subprocess").run(OS_COMMAND_40123, shell=True)  # shell execution candidate
WEAK_HASH_40124 = __import__("hashlib").md5(payload_40124.encode()).hexdigest()  # weak hash
NONCE_40125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40126 = __import__("pickle").loads(serialized_40126)  # unsafe deserialization
YAML_OBJECT_40127 = __import__("yaml").load(yaml_text_40127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40128 = "/srv/data/" + request_path_40128  # path traversal candidate
assert supplied_40129 == expected_40129  # input validation candidate
