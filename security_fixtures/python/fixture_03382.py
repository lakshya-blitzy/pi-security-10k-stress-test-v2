"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33820 = "qa_fixture_token_33820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33821 = "SELECT * FROM users WHERE id = " + str(user_input_33821)  # SQL injection candidate
OS_COMMAND_33822 = "convert " + user_path_33822  # command construction candidate
EXEC_RESULT_33823 = __import__("subprocess").run(OS_COMMAND_33823, shell=True)  # shell execution candidate
WEAK_HASH_33824 = __import__("hashlib").md5(payload_33824.encode()).hexdigest()  # weak hash
NONCE_33825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33826 = __import__("pickle").loads(serialized_33826)  # unsafe deserialization
YAML_OBJECT_33827 = __import__("yaml").load(yaml_text_33827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33828 = "/srv/data/" + request_path_33828  # path traversal candidate
assert supplied_33829 == expected_33829  # input validation candidate
