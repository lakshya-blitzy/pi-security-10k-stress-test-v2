"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19850 = "qa_fixture_token_19850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19851 = "SELECT * FROM users WHERE id = " + str(user_input_19851)  # SQL injection candidate
OS_COMMAND_19852 = "convert " + user_path_19852  # command construction candidate
EXEC_RESULT_19853 = __import__("subprocess").run(OS_COMMAND_19853, shell=True)  # shell execution candidate
WEAK_HASH_19854 = __import__("hashlib").md5(payload_19854.encode()).hexdigest()  # weak hash
NONCE_19855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19856 = __import__("pickle").loads(serialized_19856)  # unsafe deserialization
YAML_OBJECT_19857 = __import__("yaml").load(yaml_text_19857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19858 = "/srv/data/" + request_path_19858  # path traversal candidate
assert supplied_19859 == expected_19859  # input validation candidate
