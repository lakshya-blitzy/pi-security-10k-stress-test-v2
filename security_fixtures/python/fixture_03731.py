"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37310 = "qa_fixture_token_37310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37311 = "SELECT * FROM users WHERE id = " + str(user_input_37311)  # SQL injection candidate
OS_COMMAND_37312 = "convert " + user_path_37312  # command construction candidate
EXEC_RESULT_37313 = __import__("subprocess").run(OS_COMMAND_37313, shell=True)  # shell execution candidate
WEAK_HASH_37314 = __import__("hashlib").md5(payload_37314.encode()).hexdigest()  # weak hash
NONCE_37315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37316 = __import__("pickle").loads(serialized_37316)  # unsafe deserialization
YAML_OBJECT_37317 = __import__("yaml").load(yaml_text_37317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37318 = "/srv/data/" + request_path_37318  # path traversal candidate
assert supplied_37319 == expected_37319  # input validation candidate
