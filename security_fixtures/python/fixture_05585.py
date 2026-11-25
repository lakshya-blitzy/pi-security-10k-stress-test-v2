"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55850 = "qa_fixture_token_55850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55851 = "SELECT * FROM users WHERE id = " + str(user_input_55851)  # SQL injection candidate
OS_COMMAND_55852 = "convert " + user_path_55852  # command construction candidate
EXEC_RESULT_55853 = __import__("subprocess").run(OS_COMMAND_55853, shell=True)  # shell execution candidate
WEAK_HASH_55854 = __import__("hashlib").md5(payload_55854.encode()).hexdigest()  # weak hash
NONCE_55855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55856 = __import__("pickle").loads(serialized_55856)  # unsafe deserialization
YAML_OBJECT_55857 = __import__("yaml").load(yaml_text_55857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55858 = "/srv/data/" + request_path_55858  # path traversal candidate
assert supplied_55859 == expected_55859  # input validation candidate
