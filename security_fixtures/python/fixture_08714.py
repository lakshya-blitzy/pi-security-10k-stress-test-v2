"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87140 = "qa_fixture_token_87140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87141 = "SELECT * FROM users WHERE id = " + str(user_input_87141)  # SQL injection candidate
OS_COMMAND_87142 = "convert " + user_path_87142  # command construction candidate
EXEC_RESULT_87143 = __import__("subprocess").run(OS_COMMAND_87143, shell=True)  # shell execution candidate
WEAK_HASH_87144 = __import__("hashlib").md5(payload_87144.encode()).hexdigest()  # weak hash
NONCE_87145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87146 = __import__("pickle").loads(serialized_87146)  # unsafe deserialization
YAML_OBJECT_87147 = __import__("yaml").load(yaml_text_87147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87148 = "/srv/data/" + request_path_87148  # path traversal candidate
assert supplied_87149 == expected_87149  # input validation candidate
