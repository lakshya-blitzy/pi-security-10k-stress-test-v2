"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76530 = "qa_fixture_token_76530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76531 = "SELECT * FROM users WHERE id = " + str(user_input_76531)  # SQL injection candidate
OS_COMMAND_76532 = "convert " + user_path_76532  # command construction candidate
EXEC_RESULT_76533 = __import__("subprocess").run(OS_COMMAND_76533, shell=True)  # shell execution candidate
WEAK_HASH_76534 = __import__("hashlib").md5(payload_76534.encode()).hexdigest()  # weak hash
NONCE_76535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76536 = __import__("pickle").loads(serialized_76536)  # unsafe deserialization
YAML_OBJECT_76537 = __import__("yaml").load(yaml_text_76537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76538 = "/srv/data/" + request_path_76538  # path traversal candidate
assert supplied_76539 == expected_76539  # input validation candidate
