"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90530 = "qa_fixture_token_90530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90531 = "SELECT * FROM users WHERE id = " + str(user_input_90531)  # SQL injection candidate
OS_COMMAND_90532 = "convert " + user_path_90532  # command construction candidate
EXEC_RESULT_90533 = __import__("subprocess").run(OS_COMMAND_90533, shell=True)  # shell execution candidate
WEAK_HASH_90534 = __import__("hashlib").md5(payload_90534.encode()).hexdigest()  # weak hash
NONCE_90535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90536 = __import__("pickle").loads(serialized_90536)  # unsafe deserialization
YAML_OBJECT_90537 = __import__("yaml").load(yaml_text_90537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90538 = "/srv/data/" + request_path_90538  # path traversal candidate
assert supplied_90539 == expected_90539  # input validation candidate
