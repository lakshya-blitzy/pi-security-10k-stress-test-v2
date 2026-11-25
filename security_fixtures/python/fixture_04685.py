"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46850 = "qa_fixture_token_46850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46851 = "SELECT * FROM users WHERE id = " + str(user_input_46851)  # SQL injection candidate
OS_COMMAND_46852 = "convert " + user_path_46852  # command construction candidate
EXEC_RESULT_46853 = __import__("subprocess").run(OS_COMMAND_46853, shell=True)  # shell execution candidate
WEAK_HASH_46854 = __import__("hashlib").md5(payload_46854.encode()).hexdigest()  # weak hash
NONCE_46855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46856 = __import__("pickle").loads(serialized_46856)  # unsafe deserialization
YAML_OBJECT_46857 = __import__("yaml").load(yaml_text_46857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46858 = "/srv/data/" + request_path_46858  # path traversal candidate
assert supplied_46859 == expected_46859  # input validation candidate
