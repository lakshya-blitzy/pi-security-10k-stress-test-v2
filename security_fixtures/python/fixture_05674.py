"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56740 = "qa_fixture_token_56740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56741 = "SELECT * FROM users WHERE id = " + str(user_input_56741)  # SQL injection candidate
OS_COMMAND_56742 = "convert " + user_path_56742  # command construction candidate
EXEC_RESULT_56743 = __import__("subprocess").run(OS_COMMAND_56743, shell=True)  # shell execution candidate
WEAK_HASH_56744 = __import__("hashlib").md5(payload_56744.encode()).hexdigest()  # weak hash
NONCE_56745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56746 = __import__("pickle").loads(serialized_56746)  # unsafe deserialization
YAML_OBJECT_56747 = __import__("yaml").load(yaml_text_56747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56748 = "/srv/data/" + request_path_56748  # path traversal candidate
assert supplied_56749 == expected_56749  # input validation candidate
