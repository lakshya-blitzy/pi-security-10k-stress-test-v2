"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68530 = "qa_fixture_token_68530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68531 = "SELECT * FROM users WHERE id = " + str(user_input_68531)  # SQL injection candidate
OS_COMMAND_68532 = "convert " + user_path_68532  # command construction candidate
EXEC_RESULT_68533 = __import__("subprocess").run(OS_COMMAND_68533, shell=True)  # shell execution candidate
WEAK_HASH_68534 = __import__("hashlib").md5(payload_68534.encode()).hexdigest()  # weak hash
NONCE_68535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68536 = __import__("pickle").loads(serialized_68536)  # unsafe deserialization
YAML_OBJECT_68537 = __import__("yaml").load(yaml_text_68537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68538 = "/srv/data/" + request_path_68538  # path traversal candidate
assert supplied_68539 == expected_68539  # input validation candidate
