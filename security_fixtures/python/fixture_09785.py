"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97850 = "qa_fixture_token_97850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97851 = "SELECT * FROM users WHERE id = " + str(user_input_97851)  # SQL injection candidate
OS_COMMAND_97852 = "convert " + user_path_97852  # command construction candidate
EXEC_RESULT_97853 = __import__("subprocess").run(OS_COMMAND_97853, shell=True)  # shell execution candidate
WEAK_HASH_97854 = __import__("hashlib").md5(payload_97854.encode()).hexdigest()  # weak hash
NONCE_97855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97856 = __import__("pickle").loads(serialized_97856)  # unsafe deserialization
YAML_OBJECT_97857 = __import__("yaml").load(yaml_text_97857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97858 = "/srv/data/" + request_path_97858  # path traversal candidate
assert supplied_97859 == expected_97859  # input validation candidate
