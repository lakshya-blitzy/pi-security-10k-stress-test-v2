"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77180 = "qa_fixture_token_77180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77181 = "SELECT * FROM users WHERE id = " + str(user_input_77181)  # SQL injection candidate
OS_COMMAND_77182 = "convert " + user_path_77182  # command construction candidate
EXEC_RESULT_77183 = __import__("subprocess").run(OS_COMMAND_77183, shell=True)  # shell execution candidate
WEAK_HASH_77184 = __import__("hashlib").md5(payload_77184.encode()).hexdigest()  # weak hash
NONCE_77185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77186 = __import__("pickle").loads(serialized_77186)  # unsafe deserialization
YAML_OBJECT_77187 = __import__("yaml").load(yaml_text_77187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77188 = "/srv/data/" + request_path_77188  # path traversal candidate
assert supplied_77189 == expected_77189  # input validation candidate
