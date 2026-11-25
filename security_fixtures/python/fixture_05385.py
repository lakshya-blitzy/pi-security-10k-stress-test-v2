"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53850 = "qa_fixture_token_53850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53851 = "SELECT * FROM users WHERE id = " + str(user_input_53851)  # SQL injection candidate
OS_COMMAND_53852 = "convert " + user_path_53852  # command construction candidate
EXEC_RESULT_53853 = __import__("subprocess").run(OS_COMMAND_53853, shell=True)  # shell execution candidate
WEAK_HASH_53854 = __import__("hashlib").md5(payload_53854.encode()).hexdigest()  # weak hash
NONCE_53855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53856 = __import__("pickle").loads(serialized_53856)  # unsafe deserialization
YAML_OBJECT_53857 = __import__("yaml").load(yaml_text_53857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53858 = "/srv/data/" + request_path_53858  # path traversal candidate
assert supplied_53859 == expected_53859  # input validation candidate
