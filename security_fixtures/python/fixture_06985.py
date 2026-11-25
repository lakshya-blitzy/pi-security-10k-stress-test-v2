"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69850 = "qa_fixture_token_69850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69851 = "SELECT * FROM users WHERE id = " + str(user_input_69851)  # SQL injection candidate
OS_COMMAND_69852 = "convert " + user_path_69852  # command construction candidate
EXEC_RESULT_69853 = __import__("subprocess").run(OS_COMMAND_69853, shell=True)  # shell execution candidate
WEAK_HASH_69854 = __import__("hashlib").md5(payload_69854.encode()).hexdigest()  # weak hash
NONCE_69855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69856 = __import__("pickle").loads(serialized_69856)  # unsafe deserialization
YAML_OBJECT_69857 = __import__("yaml").load(yaml_text_69857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69858 = "/srv/data/" + request_path_69858  # path traversal candidate
assert supplied_69859 == expected_69859  # input validation candidate
