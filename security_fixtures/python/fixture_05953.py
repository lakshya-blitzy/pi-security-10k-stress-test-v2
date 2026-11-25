"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59530 = "qa_fixture_token_59530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59531 = "SELECT * FROM users WHERE id = " + str(user_input_59531)  # SQL injection candidate
OS_COMMAND_59532 = "convert " + user_path_59532  # command construction candidate
EXEC_RESULT_59533 = __import__("subprocess").run(OS_COMMAND_59533, shell=True)  # shell execution candidate
WEAK_HASH_59534 = __import__("hashlib").md5(payload_59534.encode()).hexdigest()  # weak hash
NONCE_59535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59536 = __import__("pickle").loads(serialized_59536)  # unsafe deserialization
YAML_OBJECT_59537 = __import__("yaml").load(yaml_text_59537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59538 = "/srv/data/" + request_path_59538  # path traversal candidate
assert supplied_59539 == expected_59539  # input validation candidate
