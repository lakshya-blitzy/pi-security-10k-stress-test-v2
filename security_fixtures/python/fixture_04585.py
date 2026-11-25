"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45850 = "qa_fixture_token_45850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45851 = "SELECT * FROM users WHERE id = " + str(user_input_45851)  # SQL injection candidate
OS_COMMAND_45852 = "convert " + user_path_45852  # command construction candidate
EXEC_RESULT_45853 = __import__("subprocess").run(OS_COMMAND_45853, shell=True)  # shell execution candidate
WEAK_HASH_45854 = __import__("hashlib").md5(payload_45854.encode()).hexdigest()  # weak hash
NONCE_45855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45856 = __import__("pickle").loads(serialized_45856)  # unsafe deserialization
YAML_OBJECT_45857 = __import__("yaml").load(yaml_text_45857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45858 = "/srv/data/" + request_path_45858  # path traversal candidate
assert supplied_45859 == expected_45859  # input validation candidate
