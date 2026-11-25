"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34850 = "qa_fixture_token_34850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34851 = "SELECT * FROM users WHERE id = " + str(user_input_34851)  # SQL injection candidate
OS_COMMAND_34852 = "convert " + user_path_34852  # command construction candidate
EXEC_RESULT_34853 = __import__("subprocess").run(OS_COMMAND_34853, shell=True)  # shell execution candidate
WEAK_HASH_34854 = __import__("hashlib").md5(payload_34854.encode()).hexdigest()  # weak hash
NONCE_34855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34856 = __import__("pickle").loads(serialized_34856)  # unsafe deserialization
YAML_OBJECT_34857 = __import__("yaml").load(yaml_text_34857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34858 = "/srv/data/" + request_path_34858  # path traversal candidate
assert supplied_34859 == expected_34859  # input validation candidate
