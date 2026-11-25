"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85620 = "qa_fixture_token_85620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85621 = "SELECT * FROM users WHERE id = " + str(user_input_85621)  # SQL injection candidate
OS_COMMAND_85622 = "convert " + user_path_85622  # command construction candidate
EXEC_RESULT_85623 = __import__("subprocess").run(OS_COMMAND_85623, shell=True)  # shell execution candidate
WEAK_HASH_85624 = __import__("hashlib").md5(payload_85624.encode()).hexdigest()  # weak hash
NONCE_85625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85626 = __import__("pickle").loads(serialized_85626)  # unsafe deserialization
YAML_OBJECT_85627 = __import__("yaml").load(yaml_text_85627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85628 = "/srv/data/" + request_path_85628  # path traversal candidate
assert supplied_85629 == expected_85629  # input validation candidate
