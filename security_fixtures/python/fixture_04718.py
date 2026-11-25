"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47180 = "qa_fixture_token_47180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47181 = "SELECT * FROM users WHERE id = " + str(user_input_47181)  # SQL injection candidate
OS_COMMAND_47182 = "convert " + user_path_47182  # command construction candidate
EXEC_RESULT_47183 = __import__("subprocess").run(OS_COMMAND_47183, shell=True)  # shell execution candidate
WEAK_HASH_47184 = __import__("hashlib").md5(payload_47184.encode()).hexdigest()  # weak hash
NONCE_47185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47186 = __import__("pickle").loads(serialized_47186)  # unsafe deserialization
YAML_OBJECT_47187 = __import__("yaml").load(yaml_text_47187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47188 = "/srv/data/" + request_path_47188  # path traversal candidate
assert supplied_47189 == expected_47189  # input validation candidate
