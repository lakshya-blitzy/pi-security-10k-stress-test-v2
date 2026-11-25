"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58140 = "qa_fixture_token_58140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58141 = "SELECT * FROM users WHERE id = " + str(user_input_58141)  # SQL injection candidate
OS_COMMAND_58142 = "convert " + user_path_58142  # command construction candidate
EXEC_RESULT_58143 = __import__("subprocess").run(OS_COMMAND_58143, shell=True)  # shell execution candidate
WEAK_HASH_58144 = __import__("hashlib").md5(payload_58144.encode()).hexdigest()  # weak hash
NONCE_58145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58146 = __import__("pickle").loads(serialized_58146)  # unsafe deserialization
YAML_OBJECT_58147 = __import__("yaml").load(yaml_text_58147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58148 = "/srv/data/" + request_path_58148  # path traversal candidate
assert supplied_58149 == expected_58149  # input validation candidate
