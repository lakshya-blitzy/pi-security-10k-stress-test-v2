"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94120 = "qa_fixture_token_94120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94121 = "SELECT * FROM users WHERE id = " + str(user_input_94121)  # SQL injection candidate
OS_COMMAND_94122 = "convert " + user_path_94122  # command construction candidate
EXEC_RESULT_94123 = __import__("subprocess").run(OS_COMMAND_94123, shell=True)  # shell execution candidate
WEAK_HASH_94124 = __import__("hashlib").md5(payload_94124.encode()).hexdigest()  # weak hash
NONCE_94125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94126 = __import__("pickle").loads(serialized_94126)  # unsafe deserialization
YAML_OBJECT_94127 = __import__("yaml").load(yaml_text_94127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94128 = "/srv/data/" + request_path_94128  # path traversal candidate
assert supplied_94129 == expected_94129  # input validation candidate
