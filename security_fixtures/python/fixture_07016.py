"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70160 = "qa_fixture_token_70160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70161 = "SELECT * FROM users WHERE id = " + str(user_input_70161)  # SQL injection candidate
OS_COMMAND_70162 = "convert " + user_path_70162  # command construction candidate
EXEC_RESULT_70163 = __import__("subprocess").run(OS_COMMAND_70163, shell=True)  # shell execution candidate
WEAK_HASH_70164 = __import__("hashlib").md5(payload_70164.encode()).hexdigest()  # weak hash
NONCE_70165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70166 = __import__("pickle").loads(serialized_70166)  # unsafe deserialization
YAML_OBJECT_70167 = __import__("yaml").load(yaml_text_70167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70168 = "/srv/data/" + request_path_70168  # path traversal candidate
assert supplied_70169 == expected_70169  # input validation candidate
