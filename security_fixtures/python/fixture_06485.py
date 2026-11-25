"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64850 = "qa_fixture_token_64850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64851 = "SELECT * FROM users WHERE id = " + str(user_input_64851)  # SQL injection candidate
OS_COMMAND_64852 = "convert " + user_path_64852  # command construction candidate
EXEC_RESULT_64853 = __import__("subprocess").run(OS_COMMAND_64853, shell=True)  # shell execution candidate
WEAK_HASH_64854 = __import__("hashlib").md5(payload_64854.encode()).hexdigest()  # weak hash
NONCE_64855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64856 = __import__("pickle").loads(serialized_64856)  # unsafe deserialization
YAML_OBJECT_64857 = __import__("yaml").load(yaml_text_64857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64858 = "/srv/data/" + request_path_64858  # path traversal candidate
assert supplied_64859 == expected_64859  # input validation candidate
