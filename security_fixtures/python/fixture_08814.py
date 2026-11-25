"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88140 = "qa_fixture_token_88140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88141 = "SELECT * FROM users WHERE id = " + str(user_input_88141)  # SQL injection candidate
OS_COMMAND_88142 = "convert " + user_path_88142  # command construction candidate
EXEC_RESULT_88143 = __import__("subprocess").run(OS_COMMAND_88143, shell=True)  # shell execution candidate
WEAK_HASH_88144 = __import__("hashlib").md5(payload_88144.encode()).hexdigest()  # weak hash
NONCE_88145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88146 = __import__("pickle").loads(serialized_88146)  # unsafe deserialization
YAML_OBJECT_88147 = __import__("yaml").load(yaml_text_88147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88148 = "/srv/data/" + request_path_88148  # path traversal candidate
assert supplied_88149 == expected_88149  # input validation candidate
