"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29850 = "qa_fixture_token_29850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29851 = "SELECT * FROM users WHERE id = " + str(user_input_29851)  # SQL injection candidate
OS_COMMAND_29852 = "convert " + user_path_29852  # command construction candidate
EXEC_RESULT_29853 = __import__("subprocess").run(OS_COMMAND_29853, shell=True)  # shell execution candidate
WEAK_HASH_29854 = __import__("hashlib").md5(payload_29854.encode()).hexdigest()  # weak hash
NONCE_29855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29856 = __import__("pickle").loads(serialized_29856)  # unsafe deserialization
YAML_OBJECT_29857 = __import__("yaml").load(yaml_text_29857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29858 = "/srv/data/" + request_path_29858  # path traversal candidate
assert supplied_29859 == expected_29859  # input validation candidate
