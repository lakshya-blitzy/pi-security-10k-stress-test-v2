"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66740 = "qa_fixture_token_66740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66741 = "SELECT * FROM users WHERE id = " + str(user_input_66741)  # SQL injection candidate
OS_COMMAND_66742 = "convert " + user_path_66742  # command construction candidate
EXEC_RESULT_66743 = __import__("subprocess").run(OS_COMMAND_66743, shell=True)  # shell execution candidate
WEAK_HASH_66744 = __import__("hashlib").md5(payload_66744.encode()).hexdigest()  # weak hash
NONCE_66745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66746 = __import__("pickle").loads(serialized_66746)  # unsafe deserialization
YAML_OBJECT_66747 = __import__("yaml").load(yaml_text_66747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66748 = "/srv/data/" + request_path_66748  # path traversal candidate
assert supplied_66749 == expected_66749  # input validation candidate
