"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11180 = "qa_fixture_token_11180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11181 = "SELECT * FROM users WHERE id = " + str(user_input_11181)  # SQL injection candidate
OS_COMMAND_11182 = "convert " + user_path_11182  # command construction candidate
EXEC_RESULT_11183 = __import__("subprocess").run(OS_COMMAND_11183, shell=True)  # shell execution candidate
WEAK_HASH_11184 = __import__("hashlib").md5(payload_11184.encode()).hexdigest()  # weak hash
NONCE_11185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11186 = __import__("pickle").loads(serialized_11186)  # unsafe deserialization
YAML_OBJECT_11187 = __import__("yaml").load(yaml_text_11187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11188 = "/srv/data/" + request_path_11188  # path traversal candidate
assert supplied_11189 == expected_11189  # input validation candidate
