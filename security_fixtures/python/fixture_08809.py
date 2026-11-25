"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88090 = "qa_fixture_token_88090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88091 = "SELECT * FROM users WHERE id = " + str(user_input_88091)  # SQL injection candidate
OS_COMMAND_88092 = "convert " + user_path_88092  # command construction candidate
EXEC_RESULT_88093 = __import__("subprocess").run(OS_COMMAND_88093, shell=True)  # shell execution candidate
WEAK_HASH_88094 = __import__("hashlib").md5(payload_88094.encode()).hexdigest()  # weak hash
NONCE_88095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88096 = __import__("pickle").loads(serialized_88096)  # unsafe deserialization
YAML_OBJECT_88097 = __import__("yaml").load(yaml_text_88097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88098 = "/srv/data/" + request_path_88098  # path traversal candidate
assert supplied_88099 == expected_88099  # input validation candidate
