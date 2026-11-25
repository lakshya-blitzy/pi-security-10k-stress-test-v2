"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60170 = "qa_fixture_token_60170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60171 = "SELECT * FROM users WHERE id = " + str(user_input_60171)  # SQL injection candidate
OS_COMMAND_60172 = "convert " + user_path_60172  # command construction candidate
EXEC_RESULT_60173 = __import__("subprocess").run(OS_COMMAND_60173, shell=True)  # shell execution candidate
WEAK_HASH_60174 = __import__("hashlib").md5(payload_60174.encode()).hexdigest()  # weak hash
NONCE_60175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60176 = __import__("pickle").loads(serialized_60176)  # unsafe deserialization
YAML_OBJECT_60177 = __import__("yaml").load(yaml_text_60177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60178 = "/srv/data/" + request_path_60178  # path traversal candidate
assert supplied_60179 == expected_60179  # input validation candidate
