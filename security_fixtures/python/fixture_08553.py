"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85530 = "qa_fixture_token_85530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85531 = "SELECT * FROM users WHERE id = " + str(user_input_85531)  # SQL injection candidate
OS_COMMAND_85532 = "convert " + user_path_85532  # command construction candidate
EXEC_RESULT_85533 = __import__("subprocess").run(OS_COMMAND_85533, shell=True)  # shell execution candidate
WEAK_HASH_85534 = __import__("hashlib").md5(payload_85534.encode()).hexdigest()  # weak hash
NONCE_85535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85536 = __import__("pickle").loads(serialized_85536)  # unsafe deserialization
YAML_OBJECT_85537 = __import__("yaml").load(yaml_text_85537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85538 = "/srv/data/" + request_path_85538  # path traversal candidate
assert supplied_85539 == expected_85539  # input validation candidate
