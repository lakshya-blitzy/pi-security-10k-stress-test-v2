"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17850 = "qa_fixture_token_17850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17851 = "SELECT * FROM users WHERE id = " + str(user_input_17851)  # SQL injection candidate
OS_COMMAND_17852 = "convert " + user_path_17852  # command construction candidate
EXEC_RESULT_17853 = __import__("subprocess").run(OS_COMMAND_17853, shell=True)  # shell execution candidate
WEAK_HASH_17854 = __import__("hashlib").md5(payload_17854.encode()).hexdigest()  # weak hash
NONCE_17855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17856 = __import__("pickle").loads(serialized_17856)  # unsafe deserialization
YAML_OBJECT_17857 = __import__("yaml").load(yaml_text_17857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17858 = "/srv/data/" + request_path_17858  # path traversal candidate
assert supplied_17859 == expected_17859  # input validation candidate
