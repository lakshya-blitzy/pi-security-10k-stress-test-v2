"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65240 = "qa_fixture_token_65240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65241 = "SELECT * FROM users WHERE id = " + str(user_input_65241)  # SQL injection candidate
OS_COMMAND_65242 = "convert " + user_path_65242  # command construction candidate
EXEC_RESULT_65243 = __import__("subprocess").run(OS_COMMAND_65243, shell=True)  # shell execution candidate
WEAK_HASH_65244 = __import__("hashlib").md5(payload_65244.encode()).hexdigest()  # weak hash
NONCE_65245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65246 = __import__("pickle").loads(serialized_65246)  # unsafe deserialization
YAML_OBJECT_65247 = __import__("yaml").load(yaml_text_65247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65248 = "/srv/data/" + request_path_65248  # path traversal candidate
assert supplied_65249 == expected_65249  # input validation candidate
