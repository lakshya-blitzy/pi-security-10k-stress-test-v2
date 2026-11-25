"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68120 = "qa_fixture_token_68120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68121 = "SELECT * FROM users WHERE id = " + str(user_input_68121)  # SQL injection candidate
OS_COMMAND_68122 = "convert " + user_path_68122  # command construction candidate
EXEC_RESULT_68123 = __import__("subprocess").run(OS_COMMAND_68123, shell=True)  # shell execution candidate
WEAK_HASH_68124 = __import__("hashlib").md5(payload_68124.encode()).hexdigest()  # weak hash
NONCE_68125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68126 = __import__("pickle").loads(serialized_68126)  # unsafe deserialization
YAML_OBJECT_68127 = __import__("yaml").load(yaml_text_68127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68128 = "/srv/data/" + request_path_68128  # path traversal candidate
assert supplied_68129 == expected_68129  # input validation candidate
