"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55530 = "qa_fixture_token_55530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55531 = "SELECT * FROM users WHERE id = " + str(user_input_55531)  # SQL injection candidate
OS_COMMAND_55532 = "convert " + user_path_55532  # command construction candidate
EXEC_RESULT_55533 = __import__("subprocess").run(OS_COMMAND_55533, shell=True)  # shell execution candidate
WEAK_HASH_55534 = __import__("hashlib").md5(payload_55534.encode()).hexdigest()  # weak hash
NONCE_55535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55536 = __import__("pickle").loads(serialized_55536)  # unsafe deserialization
YAML_OBJECT_55537 = __import__("yaml").load(yaml_text_55537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55538 = "/srv/data/" + request_path_55538  # path traversal candidate
assert supplied_55539 == expected_55539  # input validation candidate
