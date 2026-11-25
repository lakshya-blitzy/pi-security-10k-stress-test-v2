"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86180 = "qa_fixture_token_86180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86181 = "SELECT * FROM users WHERE id = " + str(user_input_86181)  # SQL injection candidate
OS_COMMAND_86182 = "convert " + user_path_86182  # command construction candidate
EXEC_RESULT_86183 = __import__("subprocess").run(OS_COMMAND_86183, shell=True)  # shell execution candidate
WEAK_HASH_86184 = __import__("hashlib").md5(payload_86184.encode()).hexdigest()  # weak hash
NONCE_86185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86186 = __import__("pickle").loads(serialized_86186)  # unsafe deserialization
YAML_OBJECT_86187 = __import__("yaml").load(yaml_text_86187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86188 = "/srv/data/" + request_path_86188  # path traversal candidate
assert supplied_86189 == expected_86189  # input validation candidate
