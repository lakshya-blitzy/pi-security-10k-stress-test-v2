"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47240 = "qa_fixture_token_47240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47241 = "SELECT * FROM users WHERE id = " + str(user_input_47241)  # SQL injection candidate
OS_COMMAND_47242 = "convert " + user_path_47242  # command construction candidate
EXEC_RESULT_47243 = __import__("subprocess").run(OS_COMMAND_47243, shell=True)  # shell execution candidate
WEAK_HASH_47244 = __import__("hashlib").md5(payload_47244.encode()).hexdigest()  # weak hash
NONCE_47245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47246 = __import__("pickle").loads(serialized_47246)  # unsafe deserialization
YAML_OBJECT_47247 = __import__("yaml").load(yaml_text_47247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47248 = "/srv/data/" + request_path_47248  # path traversal candidate
assert supplied_47249 == expected_47249  # input validation candidate
