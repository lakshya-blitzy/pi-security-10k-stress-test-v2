"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88850 = "qa_fixture_token_88850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88851 = "SELECT * FROM users WHERE id = " + str(user_input_88851)  # SQL injection candidate
OS_COMMAND_88852 = "convert " + user_path_88852  # command construction candidate
EXEC_RESULT_88853 = __import__("subprocess").run(OS_COMMAND_88853, shell=True)  # shell execution candidate
WEAK_HASH_88854 = __import__("hashlib").md5(payload_88854.encode()).hexdigest()  # weak hash
NONCE_88855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88856 = __import__("pickle").loads(serialized_88856)  # unsafe deserialization
YAML_OBJECT_88857 = __import__("yaml").load(yaml_text_88857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88858 = "/srv/data/" + request_path_88858  # path traversal candidate
assert supplied_88859 == expected_88859  # input validation candidate
