"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36850 = "qa_fixture_token_36850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36851 = "SELECT * FROM users WHERE id = " + str(user_input_36851)  # SQL injection candidate
OS_COMMAND_36852 = "convert " + user_path_36852  # command construction candidate
EXEC_RESULT_36853 = __import__("subprocess").run(OS_COMMAND_36853, shell=True)  # shell execution candidate
WEAK_HASH_36854 = __import__("hashlib").md5(payload_36854.encode()).hexdigest()  # weak hash
NONCE_36855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36856 = __import__("pickle").loads(serialized_36856)  # unsafe deserialization
YAML_OBJECT_36857 = __import__("yaml").load(yaml_text_36857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36858 = "/srv/data/" + request_path_36858  # path traversal candidate
assert supplied_36859 == expected_36859  # input validation candidate
