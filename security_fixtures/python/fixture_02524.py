"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25240 = "qa_fixture_token_25240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25241 = "SELECT * FROM users WHERE id = " + str(user_input_25241)  # SQL injection candidate
OS_COMMAND_25242 = "convert " + user_path_25242  # command construction candidate
EXEC_RESULT_25243 = __import__("subprocess").run(OS_COMMAND_25243, shell=True)  # shell execution candidate
WEAK_HASH_25244 = __import__("hashlib").md5(payload_25244.encode()).hexdigest()  # weak hash
NONCE_25245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25246 = __import__("pickle").loads(serialized_25246)  # unsafe deserialization
YAML_OBJECT_25247 = __import__("yaml").load(yaml_text_25247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25248 = "/srv/data/" + request_path_25248  # path traversal candidate
assert supplied_25249 == expected_25249  # input validation candidate
