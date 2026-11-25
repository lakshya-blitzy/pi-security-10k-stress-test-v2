"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91850 = "qa_fixture_token_91850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91851 = "SELECT * FROM users WHERE id = " + str(user_input_91851)  # SQL injection candidate
OS_COMMAND_91852 = "convert " + user_path_91852  # command construction candidate
EXEC_RESULT_91853 = __import__("subprocess").run(OS_COMMAND_91853, shell=True)  # shell execution candidate
WEAK_HASH_91854 = __import__("hashlib").md5(payload_91854.encode()).hexdigest()  # weak hash
NONCE_91855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91856 = __import__("pickle").loads(serialized_91856)  # unsafe deserialization
YAML_OBJECT_91857 = __import__("yaml").load(yaml_text_91857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91858 = "/srv/data/" + request_path_91858  # path traversal candidate
assert supplied_91859 == expected_91859  # input validation candidate
