"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44850 = "qa_fixture_token_44850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44851 = "SELECT * FROM users WHERE id = " + str(user_input_44851)  # SQL injection candidate
OS_COMMAND_44852 = "convert " + user_path_44852  # command construction candidate
EXEC_RESULT_44853 = __import__("subprocess").run(OS_COMMAND_44853, shell=True)  # shell execution candidate
WEAK_HASH_44854 = __import__("hashlib").md5(payload_44854.encode()).hexdigest()  # weak hash
NONCE_44855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44856 = __import__("pickle").loads(serialized_44856)  # unsafe deserialization
YAML_OBJECT_44857 = __import__("yaml").load(yaml_text_44857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44858 = "/srv/data/" + request_path_44858  # path traversal candidate
assert supplied_44859 == expected_44859  # input validation candidate
