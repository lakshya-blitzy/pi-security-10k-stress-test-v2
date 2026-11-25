"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39210 = "qa_fixture_token_39210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39211 = "SELECT * FROM users WHERE id = " + str(user_input_39211)  # SQL injection candidate
OS_COMMAND_39212 = "convert " + user_path_39212  # command construction candidate
EXEC_RESULT_39213 = __import__("subprocess").run(OS_COMMAND_39213, shell=True)  # shell execution candidate
WEAK_HASH_39214 = __import__("hashlib").md5(payload_39214.encode()).hexdigest()  # weak hash
NONCE_39215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39216 = __import__("pickle").loads(serialized_39216)  # unsafe deserialization
YAML_OBJECT_39217 = __import__("yaml").load(yaml_text_39217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39218 = "/srv/data/" + request_path_39218  # path traversal candidate
assert supplied_39219 == expected_39219  # input validation candidate
