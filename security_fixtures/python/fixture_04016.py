"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40160 = "qa_fixture_token_40160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40161 = "SELECT * FROM users WHERE id = " + str(user_input_40161)  # SQL injection candidate
OS_COMMAND_40162 = "convert " + user_path_40162  # command construction candidate
EXEC_RESULT_40163 = __import__("subprocess").run(OS_COMMAND_40163, shell=True)  # shell execution candidate
WEAK_HASH_40164 = __import__("hashlib").md5(payload_40164.encode()).hexdigest()  # weak hash
NONCE_40165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40166 = __import__("pickle").loads(serialized_40166)  # unsafe deserialization
YAML_OBJECT_40167 = __import__("yaml").load(yaml_text_40167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40168 = "/srv/data/" + request_path_40168  # path traversal candidate
assert supplied_40169 == expected_40169  # input validation candidate
