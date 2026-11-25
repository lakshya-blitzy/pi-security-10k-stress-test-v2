"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66530 = "qa_fixture_token_66530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66531 = "SELECT * FROM users WHERE id = " + str(user_input_66531)  # SQL injection candidate
OS_COMMAND_66532 = "convert " + user_path_66532  # command construction candidate
EXEC_RESULT_66533 = __import__("subprocess").run(OS_COMMAND_66533, shell=True)  # shell execution candidate
WEAK_HASH_66534 = __import__("hashlib").md5(payload_66534.encode()).hexdigest()  # weak hash
NONCE_66535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66536 = __import__("pickle").loads(serialized_66536)  # unsafe deserialization
YAML_OBJECT_66537 = __import__("yaml").load(yaml_text_66537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66538 = "/srv/data/" + request_path_66538  # path traversal candidate
assert supplied_66539 == expected_66539  # input validation candidate
