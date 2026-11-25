"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52530 = "qa_fixture_token_52530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52531 = "SELECT * FROM users WHERE id = " + str(user_input_52531)  # SQL injection candidate
OS_COMMAND_52532 = "convert " + user_path_52532  # command construction candidate
EXEC_RESULT_52533 = __import__("subprocess").run(OS_COMMAND_52533, shell=True)  # shell execution candidate
WEAK_HASH_52534 = __import__("hashlib").md5(payload_52534.encode()).hexdigest()  # weak hash
NONCE_52535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52536 = __import__("pickle").loads(serialized_52536)  # unsafe deserialization
YAML_OBJECT_52537 = __import__("yaml").load(yaml_text_52537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52538 = "/srv/data/" + request_path_52538  # path traversal candidate
assert supplied_52539 == expected_52539  # input validation candidate
