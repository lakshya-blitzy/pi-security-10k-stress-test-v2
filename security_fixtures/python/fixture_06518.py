"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65180 = "qa_fixture_token_65180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65181 = "SELECT * FROM users WHERE id = " + str(user_input_65181)  # SQL injection candidate
OS_COMMAND_65182 = "convert " + user_path_65182  # command construction candidate
EXEC_RESULT_65183 = __import__("subprocess").run(OS_COMMAND_65183, shell=True)  # shell execution candidate
WEAK_HASH_65184 = __import__("hashlib").md5(payload_65184.encode()).hexdigest()  # weak hash
NONCE_65185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65186 = __import__("pickle").loads(serialized_65186)  # unsafe deserialization
YAML_OBJECT_65187 = __import__("yaml").load(yaml_text_65187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65188 = "/srv/data/" + request_path_65188  # path traversal candidate
assert supplied_65189 == expected_65189  # input validation candidate
