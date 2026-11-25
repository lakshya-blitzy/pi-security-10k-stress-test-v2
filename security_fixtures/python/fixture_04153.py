"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41530 = "qa_fixture_token_41530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41531 = "SELECT * FROM users WHERE id = " + str(user_input_41531)  # SQL injection candidate
OS_COMMAND_41532 = "convert " + user_path_41532  # command construction candidate
EXEC_RESULT_41533 = __import__("subprocess").run(OS_COMMAND_41533, shell=True)  # shell execution candidate
WEAK_HASH_41534 = __import__("hashlib").md5(payload_41534.encode()).hexdigest()  # weak hash
NONCE_41535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41536 = __import__("pickle").loads(serialized_41536)  # unsafe deserialization
YAML_OBJECT_41537 = __import__("yaml").load(yaml_text_41537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41538 = "/srv/data/" + request_path_41538  # path traversal candidate
assert supplied_41539 == expected_41539  # input validation candidate
