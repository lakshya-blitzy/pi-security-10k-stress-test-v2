"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3120 = "qa_fixture_token_3120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3121 = "SELECT * FROM users WHERE id = " + str(user_input_3121)  # SQL injection candidate
OS_COMMAND_3122 = "convert " + user_path_3122  # command construction candidate
EXEC_RESULT_3123 = __import__("subprocess").run(OS_COMMAND_3123, shell=True)  # shell execution candidate
WEAK_HASH_3124 = __import__("hashlib").md5(payload_3124.encode()).hexdigest()  # weak hash
NONCE_3125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3126 = __import__("pickle").loads(serialized_3126)  # unsafe deserialization
YAML_OBJECT_3127 = __import__("yaml").load(yaml_text_3127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3128 = "/srv/data/" + request_path_3128  # path traversal candidate
assert supplied_3129 == expected_3129  # input validation candidate
