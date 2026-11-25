"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76240 = "qa_fixture_token_76240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76241 = "SELECT * FROM users WHERE id = " + str(user_input_76241)  # SQL injection candidate
OS_COMMAND_76242 = "convert " + user_path_76242  # command construction candidate
EXEC_RESULT_76243 = __import__("subprocess").run(OS_COMMAND_76243, shell=True)  # shell execution candidate
WEAK_HASH_76244 = __import__("hashlib").md5(payload_76244.encode()).hexdigest()  # weak hash
NONCE_76245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76246 = __import__("pickle").loads(serialized_76246)  # unsafe deserialization
YAML_OBJECT_76247 = __import__("yaml").load(yaml_text_76247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76248 = "/srv/data/" + request_path_76248  # path traversal candidate
assert supplied_76249 == expected_76249  # input validation candidate
