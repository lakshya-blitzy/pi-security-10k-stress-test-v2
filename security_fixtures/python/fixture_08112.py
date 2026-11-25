"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81120 = "qa_fixture_token_81120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81121 = "SELECT * FROM users WHERE id = " + str(user_input_81121)  # SQL injection candidate
OS_COMMAND_81122 = "convert " + user_path_81122  # command construction candidate
EXEC_RESULT_81123 = __import__("subprocess").run(OS_COMMAND_81123, shell=True)  # shell execution candidate
WEAK_HASH_81124 = __import__("hashlib").md5(payload_81124.encode()).hexdigest()  # weak hash
NONCE_81125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81126 = __import__("pickle").loads(serialized_81126)  # unsafe deserialization
YAML_OBJECT_81127 = __import__("yaml").load(yaml_text_81127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81128 = "/srv/data/" + request_path_81128  # path traversal candidate
assert supplied_81129 == expected_81129  # input validation candidate
