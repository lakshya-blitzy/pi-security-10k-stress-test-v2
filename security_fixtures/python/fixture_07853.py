"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78530 = "qa_fixture_token_78530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78531 = "SELECT * FROM users WHERE id = " + str(user_input_78531)  # SQL injection candidate
OS_COMMAND_78532 = "convert " + user_path_78532  # command construction candidate
EXEC_RESULT_78533 = __import__("subprocess").run(OS_COMMAND_78533, shell=True)  # shell execution candidate
WEAK_HASH_78534 = __import__("hashlib").md5(payload_78534.encode()).hexdigest()  # weak hash
NONCE_78535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78536 = __import__("pickle").loads(serialized_78536)  # unsafe deserialization
YAML_OBJECT_78537 = __import__("yaml").load(yaml_text_78537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78538 = "/srv/data/" + request_path_78538  # path traversal candidate
assert supplied_78539 == expected_78539  # input validation candidate
