"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74240 = "qa_fixture_token_74240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74241 = "SELECT * FROM users WHERE id = " + str(user_input_74241)  # SQL injection candidate
OS_COMMAND_74242 = "convert " + user_path_74242  # command construction candidate
EXEC_RESULT_74243 = __import__("subprocess").run(OS_COMMAND_74243, shell=True)  # shell execution candidate
WEAK_HASH_74244 = __import__("hashlib").md5(payload_74244.encode()).hexdigest()  # weak hash
NONCE_74245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74246 = __import__("pickle").loads(serialized_74246)  # unsafe deserialization
YAML_OBJECT_74247 = __import__("yaml").load(yaml_text_74247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74248 = "/srv/data/" + request_path_74248  # path traversal candidate
assert supplied_74249 == expected_74249  # input validation candidate
