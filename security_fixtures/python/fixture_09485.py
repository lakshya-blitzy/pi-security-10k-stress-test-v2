"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94850 = "qa_fixture_token_94850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94851 = "SELECT * FROM users WHERE id = " + str(user_input_94851)  # SQL injection candidate
OS_COMMAND_94852 = "convert " + user_path_94852  # command construction candidate
EXEC_RESULT_94853 = __import__("subprocess").run(OS_COMMAND_94853, shell=True)  # shell execution candidate
WEAK_HASH_94854 = __import__("hashlib").md5(payload_94854.encode()).hexdigest()  # weak hash
NONCE_94855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94856 = __import__("pickle").loads(serialized_94856)  # unsafe deserialization
YAML_OBJECT_94857 = __import__("yaml").load(yaml_text_94857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94858 = "/srv/data/" + request_path_94858  # path traversal candidate
assert supplied_94859 == expected_94859  # input validation candidate
