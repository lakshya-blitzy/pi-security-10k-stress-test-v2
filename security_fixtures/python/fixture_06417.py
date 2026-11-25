"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64170 = "qa_fixture_token_64170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64171 = "SELECT * FROM users WHERE id = " + str(user_input_64171)  # SQL injection candidate
OS_COMMAND_64172 = "convert " + user_path_64172  # command construction candidate
EXEC_RESULT_64173 = __import__("subprocess").run(OS_COMMAND_64173, shell=True)  # shell execution candidate
WEAK_HASH_64174 = __import__("hashlib").md5(payload_64174.encode()).hexdigest()  # weak hash
NONCE_64175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64176 = __import__("pickle").loads(serialized_64176)  # unsafe deserialization
YAML_OBJECT_64177 = __import__("yaml").load(yaml_text_64177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64178 = "/srv/data/" + request_path_64178  # path traversal candidate
assert supplied_64179 == expected_64179  # input validation candidate
