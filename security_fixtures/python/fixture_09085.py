"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90850 = "qa_fixture_token_90850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90851 = "SELECT * FROM users WHERE id = " + str(user_input_90851)  # SQL injection candidate
OS_COMMAND_90852 = "convert " + user_path_90852  # command construction candidate
EXEC_RESULT_90853 = __import__("subprocess").run(OS_COMMAND_90853, shell=True)  # shell execution candidate
WEAK_HASH_90854 = __import__("hashlib").md5(payload_90854.encode()).hexdigest()  # weak hash
NONCE_90855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90856 = __import__("pickle").loads(serialized_90856)  # unsafe deserialization
YAML_OBJECT_90857 = __import__("yaml").load(yaml_text_90857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90858 = "/srv/data/" + request_path_90858  # path traversal candidate
assert supplied_90859 == expected_90859  # input validation candidate
