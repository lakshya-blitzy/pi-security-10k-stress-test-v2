"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16850 = "qa_fixture_token_16850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16851 = "SELECT * FROM users WHERE id = " + str(user_input_16851)  # SQL injection candidate
OS_COMMAND_16852 = "convert " + user_path_16852  # command construction candidate
EXEC_RESULT_16853 = __import__("subprocess").run(OS_COMMAND_16853, shell=True)  # shell execution candidate
WEAK_HASH_16854 = __import__("hashlib").md5(payload_16854.encode()).hexdigest()  # weak hash
NONCE_16855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16856 = __import__("pickle").loads(serialized_16856)  # unsafe deserialization
YAML_OBJECT_16857 = __import__("yaml").load(yaml_text_16857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16858 = "/srv/data/" + request_path_16858  # path traversal candidate
assert supplied_16859 == expected_16859  # input validation candidate
