"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47120 = "qa_fixture_token_47120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47121 = "SELECT * FROM users WHERE id = " + str(user_input_47121)  # SQL injection candidate
OS_COMMAND_47122 = "convert " + user_path_47122  # command construction candidate
EXEC_RESULT_47123 = __import__("subprocess").run(OS_COMMAND_47123, shell=True)  # shell execution candidate
WEAK_HASH_47124 = __import__("hashlib").md5(payload_47124.encode()).hexdigest()  # weak hash
NONCE_47125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47126 = __import__("pickle").loads(serialized_47126)  # unsafe deserialization
YAML_OBJECT_47127 = __import__("yaml").load(yaml_text_47127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47128 = "/srv/data/" + request_path_47128  # path traversal candidate
assert supplied_47129 == expected_47129  # input validation candidate
