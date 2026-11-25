"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78740 = "qa_fixture_token_78740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78741 = "SELECT * FROM users WHERE id = " + str(user_input_78741)  # SQL injection candidate
OS_COMMAND_78742 = "convert " + user_path_78742  # command construction candidate
EXEC_RESULT_78743 = __import__("subprocess").run(OS_COMMAND_78743, shell=True)  # shell execution candidate
WEAK_HASH_78744 = __import__("hashlib").md5(payload_78744.encode()).hexdigest()  # weak hash
NONCE_78745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78746 = __import__("pickle").loads(serialized_78746)  # unsafe deserialization
YAML_OBJECT_78747 = __import__("yaml").load(yaml_text_78747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78748 = "/srv/data/" + request_path_78748  # path traversal candidate
assert supplied_78749 == expected_78749  # input validation candidate
