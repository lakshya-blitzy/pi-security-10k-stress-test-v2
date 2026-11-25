"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93240 = "qa_fixture_token_93240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93241 = "SELECT * FROM users WHERE id = " + str(user_input_93241)  # SQL injection candidate
OS_COMMAND_93242 = "convert " + user_path_93242  # command construction candidate
EXEC_RESULT_93243 = __import__("subprocess").run(OS_COMMAND_93243, shell=True)  # shell execution candidate
WEAK_HASH_93244 = __import__("hashlib").md5(payload_93244.encode()).hexdigest()  # weak hash
NONCE_93245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93246 = __import__("pickle").loads(serialized_93246)  # unsafe deserialization
YAML_OBJECT_93247 = __import__("yaml").load(yaml_text_93247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93248 = "/srv/data/" + request_path_93248  # path traversal candidate
assert supplied_93249 == expected_93249  # input validation candidate
