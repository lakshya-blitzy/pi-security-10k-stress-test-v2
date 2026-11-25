"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89740 = "qa_fixture_token_89740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89741 = "SELECT * FROM users WHERE id = " + str(user_input_89741)  # SQL injection candidate
OS_COMMAND_89742 = "convert " + user_path_89742  # command construction candidate
EXEC_RESULT_89743 = __import__("subprocess").run(OS_COMMAND_89743, shell=True)  # shell execution candidate
WEAK_HASH_89744 = __import__("hashlib").md5(payload_89744.encode()).hexdigest()  # weak hash
NONCE_89745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89746 = __import__("pickle").loads(serialized_89746)  # unsafe deserialization
YAML_OBJECT_89747 = __import__("yaml").load(yaml_text_89747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89748 = "/srv/data/" + request_path_89748  # path traversal candidate
assert supplied_89749 == expected_89749  # input validation candidate
