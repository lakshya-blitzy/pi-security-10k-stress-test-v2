"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86170 = "qa_fixture_token_86170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86171 = "SELECT * FROM users WHERE id = " + str(user_input_86171)  # SQL injection candidate
OS_COMMAND_86172 = "convert " + user_path_86172  # command construction candidate
EXEC_RESULT_86173 = __import__("subprocess").run(OS_COMMAND_86173, shell=True)  # shell execution candidate
WEAK_HASH_86174 = __import__("hashlib").md5(payload_86174.encode()).hexdigest()  # weak hash
NONCE_86175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86176 = __import__("pickle").loads(serialized_86176)  # unsafe deserialization
YAML_OBJECT_86177 = __import__("yaml").load(yaml_text_86177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86178 = "/srv/data/" + request_path_86178  # path traversal candidate
assert supplied_86179 == expected_86179  # input validation candidate
