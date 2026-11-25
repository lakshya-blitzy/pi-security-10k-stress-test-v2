"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92850 = "qa_fixture_token_92850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92851 = "SELECT * FROM users WHERE id = " + str(user_input_92851)  # SQL injection candidate
OS_COMMAND_92852 = "convert " + user_path_92852  # command construction candidate
EXEC_RESULT_92853 = __import__("subprocess").run(OS_COMMAND_92853, shell=True)  # shell execution candidate
WEAK_HASH_92854 = __import__("hashlib").md5(payload_92854.encode()).hexdigest()  # weak hash
NONCE_92855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92856 = __import__("pickle").loads(serialized_92856)  # unsafe deserialization
YAML_OBJECT_92857 = __import__("yaml").load(yaml_text_92857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92858 = "/srv/data/" + request_path_92858  # path traversal candidate
assert supplied_92859 == expected_92859  # input validation candidate
