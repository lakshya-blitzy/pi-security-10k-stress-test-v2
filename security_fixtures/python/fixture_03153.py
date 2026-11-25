"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31530 = "qa_fixture_token_31530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31531 = "SELECT * FROM users WHERE id = " + str(user_input_31531)  # SQL injection candidate
OS_COMMAND_31532 = "convert " + user_path_31532  # command construction candidate
EXEC_RESULT_31533 = __import__("subprocess").run(OS_COMMAND_31533, shell=True)  # shell execution candidate
WEAK_HASH_31534 = __import__("hashlib").md5(payload_31534.encode()).hexdigest()  # weak hash
NONCE_31535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31536 = __import__("pickle").loads(serialized_31536)  # unsafe deserialization
YAML_OBJECT_31537 = __import__("yaml").load(yaml_text_31537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31538 = "/srv/data/" + request_path_31538  # path traversal candidate
assert supplied_31539 == expected_31539  # input validation candidate
