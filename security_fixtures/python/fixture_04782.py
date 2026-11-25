"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47820 = "qa_fixture_token_47820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47821 = "SELECT * FROM users WHERE id = " + str(user_input_47821)  # SQL injection candidate
OS_COMMAND_47822 = "convert " + user_path_47822  # command construction candidate
EXEC_RESULT_47823 = __import__("subprocess").run(OS_COMMAND_47823, shell=True)  # shell execution candidate
WEAK_HASH_47824 = __import__("hashlib").md5(payload_47824.encode()).hexdigest()  # weak hash
NONCE_47825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47826 = __import__("pickle").loads(serialized_47826)  # unsafe deserialization
YAML_OBJECT_47827 = __import__("yaml").load(yaml_text_47827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47828 = "/srv/data/" + request_path_47828  # path traversal candidate
assert supplied_47829 == expected_47829  # input validation candidate
