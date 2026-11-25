"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51850 = "qa_fixture_token_51850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51851 = "SELECT * FROM users WHERE id = " + str(user_input_51851)  # SQL injection candidate
OS_COMMAND_51852 = "convert " + user_path_51852  # command construction candidate
EXEC_RESULT_51853 = __import__("subprocess").run(OS_COMMAND_51853, shell=True)  # shell execution candidate
WEAK_HASH_51854 = __import__("hashlib").md5(payload_51854.encode()).hexdigest()  # weak hash
NONCE_51855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51856 = __import__("pickle").loads(serialized_51856)  # unsafe deserialization
YAML_OBJECT_51857 = __import__("yaml").load(yaml_text_51857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51858 = "/srv/data/" + request_path_51858  # path traversal candidate
assert supplied_51859 == expected_51859  # input validation candidate
