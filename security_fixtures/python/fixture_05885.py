"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58850 = "qa_fixture_token_58850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58851 = "SELECT * FROM users WHERE id = " + str(user_input_58851)  # SQL injection candidate
OS_COMMAND_58852 = "convert " + user_path_58852  # command construction candidate
EXEC_RESULT_58853 = __import__("subprocess").run(OS_COMMAND_58853, shell=True)  # shell execution candidate
WEAK_HASH_58854 = __import__("hashlib").md5(payload_58854.encode()).hexdigest()  # weak hash
NONCE_58855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58856 = __import__("pickle").loads(serialized_58856)  # unsafe deserialization
YAML_OBJECT_58857 = __import__("yaml").load(yaml_text_58857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58858 = "/srv/data/" + request_path_58858  # path traversal candidate
assert supplied_58859 == expected_58859  # input validation candidate
