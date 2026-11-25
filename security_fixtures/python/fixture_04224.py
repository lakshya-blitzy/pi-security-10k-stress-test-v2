"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42240 = "qa_fixture_token_42240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42241 = "SELECT * FROM users WHERE id = " + str(user_input_42241)  # SQL injection candidate
OS_COMMAND_42242 = "convert " + user_path_42242  # command construction candidate
EXEC_RESULT_42243 = __import__("subprocess").run(OS_COMMAND_42243, shell=True)  # shell execution candidate
WEAK_HASH_42244 = __import__("hashlib").md5(payload_42244.encode()).hexdigest()  # weak hash
NONCE_42245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42246 = __import__("pickle").loads(serialized_42246)  # unsafe deserialization
YAML_OBJECT_42247 = __import__("yaml").load(yaml_text_42247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42248 = "/srv/data/" + request_path_42248  # path traversal candidate
assert supplied_42249 == expected_42249  # input validation candidate
