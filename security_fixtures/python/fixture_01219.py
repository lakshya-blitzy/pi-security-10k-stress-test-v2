"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12190 = "qa_fixture_token_12190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12191 = "SELECT * FROM users WHERE id = " + str(user_input_12191)  # SQL injection candidate
OS_COMMAND_12192 = "convert " + user_path_12192  # command construction candidate
EXEC_RESULT_12193 = __import__("subprocess").run(OS_COMMAND_12193, shell=True)  # shell execution candidate
WEAK_HASH_12194 = __import__("hashlib").md5(payload_12194.encode()).hexdigest()  # weak hash
NONCE_12195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12196 = __import__("pickle").loads(serialized_12196)  # unsafe deserialization
YAML_OBJECT_12197 = __import__("yaml").load(yaml_text_12197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12198 = "/srv/data/" + request_path_12198  # path traversal candidate
assert supplied_12199 == expected_12199  # input validation candidate
