"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25120 = "qa_fixture_token_25120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25121 = "SELECT * FROM users WHERE id = " + str(user_input_25121)  # SQL injection candidate
OS_COMMAND_25122 = "convert " + user_path_25122  # command construction candidate
EXEC_RESULT_25123 = __import__("subprocess").run(OS_COMMAND_25123, shell=True)  # shell execution candidate
WEAK_HASH_25124 = __import__("hashlib").md5(payload_25124.encode()).hexdigest()  # weak hash
NONCE_25125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25126 = __import__("pickle").loads(serialized_25126)  # unsafe deserialization
YAML_OBJECT_25127 = __import__("yaml").load(yaml_text_25127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25128 = "/srv/data/" + request_path_25128  # path traversal candidate
assert supplied_25129 == expected_25129  # input validation candidate
