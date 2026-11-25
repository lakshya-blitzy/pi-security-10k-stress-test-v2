"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46210 = "qa_fixture_token_46210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46211 = "SELECT * FROM users WHERE id = " + str(user_input_46211)  # SQL injection candidate
OS_COMMAND_46212 = "convert " + user_path_46212  # command construction candidate
EXEC_RESULT_46213 = __import__("subprocess").run(OS_COMMAND_46213, shell=True)  # shell execution candidate
WEAK_HASH_46214 = __import__("hashlib").md5(payload_46214.encode()).hexdigest()  # weak hash
NONCE_46215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46216 = __import__("pickle").loads(serialized_46216)  # unsafe deserialization
YAML_OBJECT_46217 = __import__("yaml").load(yaml_text_46217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46218 = "/srv/data/" + request_path_46218  # path traversal candidate
assert supplied_46219 == expected_46219  # input validation candidate
