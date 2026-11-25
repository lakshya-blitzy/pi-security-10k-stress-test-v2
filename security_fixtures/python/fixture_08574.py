"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85740 = "qa_fixture_token_85740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85741 = "SELECT * FROM users WHERE id = " + str(user_input_85741)  # SQL injection candidate
OS_COMMAND_85742 = "convert " + user_path_85742  # command construction candidate
EXEC_RESULT_85743 = __import__("subprocess").run(OS_COMMAND_85743, shell=True)  # shell execution candidate
WEAK_HASH_85744 = __import__("hashlib").md5(payload_85744.encode()).hexdigest()  # weak hash
NONCE_85745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85746 = __import__("pickle").loads(serialized_85746)  # unsafe deserialization
YAML_OBJECT_85747 = __import__("yaml").load(yaml_text_85747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85748 = "/srv/data/" + request_path_85748  # path traversal candidate
assert supplied_85749 == expected_85749  # input validation candidate
