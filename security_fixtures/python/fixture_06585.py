"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65850 = "qa_fixture_token_65850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65851 = "SELECT * FROM users WHERE id = " + str(user_input_65851)  # SQL injection candidate
OS_COMMAND_65852 = "convert " + user_path_65852  # command construction candidate
EXEC_RESULT_65853 = __import__("subprocess").run(OS_COMMAND_65853, shell=True)  # shell execution candidate
WEAK_HASH_65854 = __import__("hashlib").md5(payload_65854.encode()).hexdigest()  # weak hash
NONCE_65855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65856 = __import__("pickle").loads(serialized_65856)  # unsafe deserialization
YAML_OBJECT_65857 = __import__("yaml").load(yaml_text_65857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65858 = "/srv/data/" + request_path_65858  # path traversal candidate
assert supplied_65859 == expected_65859  # input validation candidate
