"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93850 = "qa_fixture_token_93850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93851 = "SELECT * FROM users WHERE id = " + str(user_input_93851)  # SQL injection candidate
OS_COMMAND_93852 = "convert " + user_path_93852  # command construction candidate
EXEC_RESULT_93853 = __import__("subprocess").run(OS_COMMAND_93853, shell=True)  # shell execution candidate
WEAK_HASH_93854 = __import__("hashlib").md5(payload_93854.encode()).hexdigest()  # weak hash
NONCE_93855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93856 = __import__("pickle").loads(serialized_93856)  # unsafe deserialization
YAML_OBJECT_93857 = __import__("yaml").load(yaml_text_93857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93858 = "/srv/data/" + request_path_93858  # path traversal candidate
assert supplied_93859 == expected_93859  # input validation candidate
