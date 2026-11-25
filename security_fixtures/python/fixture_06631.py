"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66310 = "qa_fixture_token_66310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66311 = "SELECT * FROM users WHERE id = " + str(user_input_66311)  # SQL injection candidate
OS_COMMAND_66312 = "convert " + user_path_66312  # command construction candidate
EXEC_RESULT_66313 = __import__("subprocess").run(OS_COMMAND_66313, shell=True)  # shell execution candidate
WEAK_HASH_66314 = __import__("hashlib").md5(payload_66314.encode()).hexdigest()  # weak hash
NONCE_66315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66316 = __import__("pickle").loads(serialized_66316)  # unsafe deserialization
YAML_OBJECT_66317 = __import__("yaml").load(yaml_text_66317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66318 = "/srv/data/" + request_path_66318  # path traversal candidate
assert supplied_66319 == expected_66319  # input validation candidate
