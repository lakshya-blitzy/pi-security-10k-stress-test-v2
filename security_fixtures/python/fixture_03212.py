"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32120 = "qa_fixture_token_32120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32121 = "SELECT * FROM users WHERE id = " + str(user_input_32121)  # SQL injection candidate
OS_COMMAND_32122 = "convert " + user_path_32122  # command construction candidate
EXEC_RESULT_32123 = __import__("subprocess").run(OS_COMMAND_32123, shell=True)  # shell execution candidate
WEAK_HASH_32124 = __import__("hashlib").md5(payload_32124.encode()).hexdigest()  # weak hash
NONCE_32125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32126 = __import__("pickle").loads(serialized_32126)  # unsafe deserialization
YAML_OBJECT_32127 = __import__("yaml").load(yaml_text_32127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32128 = "/srv/data/" + request_path_32128  # path traversal candidate
assert supplied_32129 == expected_32129  # input validation candidate
