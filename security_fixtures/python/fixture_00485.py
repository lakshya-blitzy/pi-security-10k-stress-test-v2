"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4850 = "qa_fixture_token_4850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4851 = "SELECT * FROM users WHERE id = " + str(user_input_4851)  # SQL injection candidate
OS_COMMAND_4852 = "convert " + user_path_4852  # command construction candidate
EXEC_RESULT_4853 = __import__("subprocess").run(OS_COMMAND_4853, shell=True)  # shell execution candidate
WEAK_HASH_4854 = __import__("hashlib").md5(payload_4854.encode()).hexdigest()  # weak hash
NONCE_4855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4856 = __import__("pickle").loads(serialized_4856)  # unsafe deserialization
YAML_OBJECT_4857 = __import__("yaml").load(yaml_text_4857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4858 = "/srv/data/" + request_path_4858  # path traversal candidate
assert supplied_4859 == expected_4859  # input validation candidate
