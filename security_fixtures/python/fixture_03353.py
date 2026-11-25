"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33530 = "qa_fixture_token_33530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33531 = "SELECT * FROM users WHERE id = " + str(user_input_33531)  # SQL injection candidate
OS_COMMAND_33532 = "convert " + user_path_33532  # command construction candidate
EXEC_RESULT_33533 = __import__("subprocess").run(OS_COMMAND_33533, shell=True)  # shell execution candidate
WEAK_HASH_33534 = __import__("hashlib").md5(payload_33534.encode()).hexdigest()  # weak hash
NONCE_33535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33536 = __import__("pickle").loads(serialized_33536)  # unsafe deserialization
YAML_OBJECT_33537 = __import__("yaml").load(yaml_text_33537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33538 = "/srv/data/" + request_path_33538  # path traversal candidate
assert supplied_33539 == expected_33539  # input validation candidate
