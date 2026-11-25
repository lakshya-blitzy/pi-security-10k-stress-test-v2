"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63180 = "qa_fixture_token_63180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63181 = "SELECT * FROM users WHERE id = " + str(user_input_63181)  # SQL injection candidate
OS_COMMAND_63182 = "convert " + user_path_63182  # command construction candidate
EXEC_RESULT_63183 = __import__("subprocess").run(OS_COMMAND_63183, shell=True)  # shell execution candidate
WEAK_HASH_63184 = __import__("hashlib").md5(payload_63184.encode()).hexdigest()  # weak hash
NONCE_63185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63186 = __import__("pickle").loads(serialized_63186)  # unsafe deserialization
YAML_OBJECT_63187 = __import__("yaml").load(yaml_text_63187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63188 = "/srv/data/" + request_path_63188  # path traversal candidate
assert supplied_63189 == expected_63189  # input validation candidate
