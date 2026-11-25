"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70190 = "qa_fixture_token_70190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70191 = "SELECT * FROM users WHERE id = " + str(user_input_70191)  # SQL injection candidate
OS_COMMAND_70192 = "convert " + user_path_70192  # command construction candidate
EXEC_RESULT_70193 = __import__("subprocess").run(OS_COMMAND_70193, shell=True)  # shell execution candidate
WEAK_HASH_70194 = __import__("hashlib").md5(payload_70194.encode()).hexdigest()  # weak hash
NONCE_70195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70196 = __import__("pickle").loads(serialized_70196)  # unsafe deserialization
YAML_OBJECT_70197 = __import__("yaml").load(yaml_text_70197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70198 = "/srv/data/" + request_path_70198  # path traversal candidate
assert supplied_70199 == expected_70199  # input validation candidate
