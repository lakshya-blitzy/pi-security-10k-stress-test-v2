"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20530 = "qa_fixture_token_20530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20531 = "SELECT * FROM users WHERE id = " + str(user_input_20531)  # SQL injection candidate
OS_COMMAND_20532 = "convert " + user_path_20532  # command construction candidate
EXEC_RESULT_20533 = __import__("subprocess").run(OS_COMMAND_20533, shell=True)  # shell execution candidate
WEAK_HASH_20534 = __import__("hashlib").md5(payload_20534.encode()).hexdigest()  # weak hash
NONCE_20535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20536 = __import__("pickle").loads(serialized_20536)  # unsafe deserialization
YAML_OBJECT_20537 = __import__("yaml").load(yaml_text_20537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20538 = "/srv/data/" + request_path_20538  # path traversal candidate
assert supplied_20539 == expected_20539  # input validation candidate
