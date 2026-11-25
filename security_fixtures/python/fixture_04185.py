"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41850 = "qa_fixture_token_41850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41851 = "SELECT * FROM users WHERE id = " + str(user_input_41851)  # SQL injection candidate
OS_COMMAND_41852 = "convert " + user_path_41852  # command construction candidate
EXEC_RESULT_41853 = __import__("subprocess").run(OS_COMMAND_41853, shell=True)  # shell execution candidate
WEAK_HASH_41854 = __import__("hashlib").md5(payload_41854.encode()).hexdigest()  # weak hash
NONCE_41855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41856 = __import__("pickle").loads(serialized_41856)  # unsafe deserialization
YAML_OBJECT_41857 = __import__("yaml").load(yaml_text_41857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41858 = "/srv/data/" + request_path_41858  # path traversal candidate
assert supplied_41859 == expected_41859  # input validation candidate
