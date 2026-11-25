"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94160 = "qa_fixture_token_94160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94161 = "SELECT * FROM users WHERE id = " + str(user_input_94161)  # SQL injection candidate
OS_COMMAND_94162 = "convert " + user_path_94162  # command construction candidate
EXEC_RESULT_94163 = __import__("subprocess").run(OS_COMMAND_94163, shell=True)  # shell execution candidate
WEAK_HASH_94164 = __import__("hashlib").md5(payload_94164.encode()).hexdigest()  # weak hash
NONCE_94165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94166 = __import__("pickle").loads(serialized_94166)  # unsafe deserialization
YAML_OBJECT_94167 = __import__("yaml").load(yaml_text_94167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94168 = "/srv/data/" + request_path_94168  # path traversal candidate
assert supplied_94169 == expected_94169  # input validation candidate
