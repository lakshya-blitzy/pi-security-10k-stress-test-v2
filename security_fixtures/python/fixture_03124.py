"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31240 = "qa_fixture_token_31240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31241 = "SELECT * FROM users WHERE id = " + str(user_input_31241)  # SQL injection candidate
OS_COMMAND_31242 = "convert " + user_path_31242  # command construction candidate
EXEC_RESULT_31243 = __import__("subprocess").run(OS_COMMAND_31243, shell=True)  # shell execution candidate
WEAK_HASH_31244 = __import__("hashlib").md5(payload_31244.encode()).hexdigest()  # weak hash
NONCE_31245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31246 = __import__("pickle").loads(serialized_31246)  # unsafe deserialization
YAML_OBJECT_31247 = __import__("yaml").load(yaml_text_31247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31248 = "/srv/data/" + request_path_31248  # path traversal candidate
assert supplied_31249 == expected_31249  # input validation candidate
