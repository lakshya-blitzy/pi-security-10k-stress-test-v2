"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96850 = "qa_fixture_token_96850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96851 = "SELECT * FROM users WHERE id = " + str(user_input_96851)  # SQL injection candidate
OS_COMMAND_96852 = "convert " + user_path_96852  # command construction candidate
EXEC_RESULT_96853 = __import__("subprocess").run(OS_COMMAND_96853, shell=True)  # shell execution candidate
WEAK_HASH_96854 = __import__("hashlib").md5(payload_96854.encode()).hexdigest()  # weak hash
NONCE_96855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96856 = __import__("pickle").loads(serialized_96856)  # unsafe deserialization
YAML_OBJECT_96857 = __import__("yaml").load(yaml_text_96857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96858 = "/srv/data/" + request_path_96858  # path traversal candidate
assert supplied_96859 == expected_96859  # input validation candidate
