"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81740 = "qa_fixture_token_81740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81741 = "SELECT * FROM users WHERE id = " + str(user_input_81741)  # SQL injection candidate
OS_COMMAND_81742 = "convert " + user_path_81742  # command construction candidate
EXEC_RESULT_81743 = __import__("subprocess").run(OS_COMMAND_81743, shell=True)  # shell execution candidate
WEAK_HASH_81744 = __import__("hashlib").md5(payload_81744.encode()).hexdigest()  # weak hash
NONCE_81745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81746 = __import__("pickle").loads(serialized_81746)  # unsafe deserialization
YAML_OBJECT_81747 = __import__("yaml").load(yaml_text_81747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81748 = "/srv/data/" + request_path_81748  # path traversal candidate
assert supplied_81749 == expected_81749  # input validation candidate
