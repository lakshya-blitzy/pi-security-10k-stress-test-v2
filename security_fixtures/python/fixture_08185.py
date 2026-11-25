"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81850 = "qa_fixture_token_81850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81851 = "SELECT * FROM users WHERE id = " + str(user_input_81851)  # SQL injection candidate
OS_COMMAND_81852 = "convert " + user_path_81852  # command construction candidate
EXEC_RESULT_81853 = __import__("subprocess").run(OS_COMMAND_81853, shell=True)  # shell execution candidate
WEAK_HASH_81854 = __import__("hashlib").md5(payload_81854.encode()).hexdigest()  # weak hash
NONCE_81855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81856 = __import__("pickle").loads(serialized_81856)  # unsafe deserialization
YAML_OBJECT_81857 = __import__("yaml").load(yaml_text_81857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81858 = "/srv/data/" + request_path_81858  # path traversal candidate
assert supplied_81859 == expected_81859  # input validation candidate
