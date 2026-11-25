"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46240 = "qa_fixture_token_46240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46241 = "SELECT * FROM users WHERE id = " + str(user_input_46241)  # SQL injection candidate
OS_COMMAND_46242 = "convert " + user_path_46242  # command construction candidate
EXEC_RESULT_46243 = __import__("subprocess").run(OS_COMMAND_46243, shell=True)  # shell execution candidate
WEAK_HASH_46244 = __import__("hashlib").md5(payload_46244.encode()).hexdigest()  # weak hash
NONCE_46245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46246 = __import__("pickle").loads(serialized_46246)  # unsafe deserialization
YAML_OBJECT_46247 = __import__("yaml").load(yaml_text_46247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46248 = "/srv/data/" + request_path_46248  # path traversal candidate
assert supplied_46249 == expected_46249  # input validation candidate
