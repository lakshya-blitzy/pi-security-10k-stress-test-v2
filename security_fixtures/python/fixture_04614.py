"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46140 = "qa_fixture_token_46140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46141 = "SELECT * FROM users WHERE id = " + str(user_input_46141)  # SQL injection candidate
OS_COMMAND_46142 = "convert " + user_path_46142  # command construction candidate
EXEC_RESULT_46143 = __import__("subprocess").run(OS_COMMAND_46143, shell=True)  # shell execution candidate
WEAK_HASH_46144 = __import__("hashlib").md5(payload_46144.encode()).hexdigest()  # weak hash
NONCE_46145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46146 = __import__("pickle").loads(serialized_46146)  # unsafe deserialization
YAML_OBJECT_46147 = __import__("yaml").load(yaml_text_46147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46148 = "/srv/data/" + request_path_46148  # path traversal candidate
assert supplied_46149 == expected_46149  # input validation candidate
