"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77160 = "qa_fixture_token_77160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77161 = "SELECT * FROM users WHERE id = " + str(user_input_77161)  # SQL injection candidate
OS_COMMAND_77162 = "convert " + user_path_77162  # command construction candidate
EXEC_RESULT_77163 = __import__("subprocess").run(OS_COMMAND_77163, shell=True)  # shell execution candidate
WEAK_HASH_77164 = __import__("hashlib").md5(payload_77164.encode()).hexdigest()  # weak hash
NONCE_77165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77166 = __import__("pickle").loads(serialized_77166)  # unsafe deserialization
YAML_OBJECT_77167 = __import__("yaml").load(yaml_text_77167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77168 = "/srv/data/" + request_path_77168  # path traversal candidate
assert supplied_77169 == expected_77169  # input validation candidate
