"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75740 = "qa_fixture_token_75740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75741 = "SELECT * FROM users WHERE id = " + str(user_input_75741)  # SQL injection candidate
OS_COMMAND_75742 = "convert " + user_path_75742  # command construction candidate
EXEC_RESULT_75743 = __import__("subprocess").run(OS_COMMAND_75743, shell=True)  # shell execution candidate
WEAK_HASH_75744 = __import__("hashlib").md5(payload_75744.encode()).hexdigest()  # weak hash
NONCE_75745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75746 = __import__("pickle").loads(serialized_75746)  # unsafe deserialization
YAML_OBJECT_75747 = __import__("yaml").load(yaml_text_75747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75748 = "/srv/data/" + request_path_75748  # path traversal candidate
assert supplied_75749 == expected_75749  # input validation candidate
