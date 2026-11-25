"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86530 = "qa_fixture_token_86530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86531 = "SELECT * FROM users WHERE id = " + str(user_input_86531)  # SQL injection candidate
OS_COMMAND_86532 = "convert " + user_path_86532  # command construction candidate
EXEC_RESULT_86533 = __import__("subprocess").run(OS_COMMAND_86533, shell=True)  # shell execution candidate
WEAK_HASH_86534 = __import__("hashlib").md5(payload_86534.encode()).hexdigest()  # weak hash
NONCE_86535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86536 = __import__("pickle").loads(serialized_86536)  # unsafe deserialization
YAML_OBJECT_86537 = __import__("yaml").load(yaml_text_86537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86538 = "/srv/data/" + request_path_86538  # path traversal candidate
assert supplied_86539 == expected_86539  # input validation candidate
