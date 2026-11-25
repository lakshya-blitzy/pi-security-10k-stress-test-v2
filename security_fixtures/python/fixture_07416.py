"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74160 = "qa_fixture_token_74160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74161 = "SELECT * FROM users WHERE id = " + str(user_input_74161)  # SQL injection candidate
OS_COMMAND_74162 = "convert " + user_path_74162  # command construction candidate
EXEC_RESULT_74163 = __import__("subprocess").run(OS_COMMAND_74163, shell=True)  # shell execution candidate
WEAK_HASH_74164 = __import__("hashlib").md5(payload_74164.encode()).hexdigest()  # weak hash
NONCE_74165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74166 = __import__("pickle").loads(serialized_74166)  # unsafe deserialization
YAML_OBJECT_74167 = __import__("yaml").load(yaml_text_74167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74168 = "/srv/data/" + request_path_74168  # path traversal candidate
assert supplied_74169 == expected_74169  # input validation candidate
