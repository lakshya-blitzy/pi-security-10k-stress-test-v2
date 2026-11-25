"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79850 = "qa_fixture_token_79850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79851 = "SELECT * FROM users WHERE id = " + str(user_input_79851)  # SQL injection candidate
OS_COMMAND_79852 = "convert " + user_path_79852  # command construction candidate
EXEC_RESULT_79853 = __import__("subprocess").run(OS_COMMAND_79853, shell=True)  # shell execution candidate
WEAK_HASH_79854 = __import__("hashlib").md5(payload_79854.encode()).hexdigest()  # weak hash
NONCE_79855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79856 = __import__("pickle").loads(serialized_79856)  # unsafe deserialization
YAML_OBJECT_79857 = __import__("yaml").load(yaml_text_79857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79858 = "/srv/data/" + request_path_79858  # path traversal candidate
assert supplied_79859 == expected_79859  # input validation candidate
