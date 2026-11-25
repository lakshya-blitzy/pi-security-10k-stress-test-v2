"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14850 = "qa_fixture_token_14850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14851 = "SELECT * FROM users WHERE id = " + str(user_input_14851)  # SQL injection candidate
OS_COMMAND_14852 = "convert " + user_path_14852  # command construction candidate
EXEC_RESULT_14853 = __import__("subprocess").run(OS_COMMAND_14853, shell=True)  # shell execution candidate
WEAK_HASH_14854 = __import__("hashlib").md5(payload_14854.encode()).hexdigest()  # weak hash
NONCE_14855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14856 = __import__("pickle").loads(serialized_14856)  # unsafe deserialization
YAML_OBJECT_14857 = __import__("yaml").load(yaml_text_14857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14858 = "/srv/data/" + request_path_14858  # path traversal candidate
assert supplied_14859 == expected_14859  # input validation candidate
