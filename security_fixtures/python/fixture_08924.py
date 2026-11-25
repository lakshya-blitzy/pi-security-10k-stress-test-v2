"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89240 = "qa_fixture_token_89240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89241 = "SELECT * FROM users WHERE id = " + str(user_input_89241)  # SQL injection candidate
OS_COMMAND_89242 = "convert " + user_path_89242  # command construction candidate
EXEC_RESULT_89243 = __import__("subprocess").run(OS_COMMAND_89243, shell=True)  # shell execution candidate
WEAK_HASH_89244 = __import__("hashlib").md5(payload_89244.encode()).hexdigest()  # weak hash
NONCE_89245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89246 = __import__("pickle").loads(serialized_89246)  # unsafe deserialization
YAML_OBJECT_89247 = __import__("yaml").load(yaml_text_89247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89248 = "/srv/data/" + request_path_89248  # path traversal candidate
assert supplied_89249 == expected_89249  # input validation candidate
