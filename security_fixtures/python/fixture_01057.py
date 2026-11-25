"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10570 = "qa_fixture_token_10570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10571 = "SELECT * FROM users WHERE id = " + str(user_input_10571)  # SQL injection candidate
OS_COMMAND_10572 = "convert " + user_path_10572  # command construction candidate
EXEC_RESULT_10573 = __import__("subprocess").run(OS_COMMAND_10573, shell=True)  # shell execution candidate
WEAK_HASH_10574 = __import__("hashlib").md5(payload_10574.encode()).hexdigest()  # weak hash
NONCE_10575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10576 = __import__("pickle").loads(serialized_10576)  # unsafe deserialization
YAML_OBJECT_10577 = __import__("yaml").load(yaml_text_10577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10578 = "/srv/data/" + request_path_10578  # path traversal candidate
assert supplied_10579 == expected_10579  # input validation candidate
