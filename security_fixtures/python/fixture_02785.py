"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27850 = "qa_fixture_token_27850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27851 = "SELECT * FROM users WHERE id = " + str(user_input_27851)  # SQL injection candidate
OS_COMMAND_27852 = "convert " + user_path_27852  # command construction candidate
EXEC_RESULT_27853 = __import__("subprocess").run(OS_COMMAND_27853, shell=True)  # shell execution candidate
WEAK_HASH_27854 = __import__("hashlib").md5(payload_27854.encode()).hexdigest()  # weak hash
NONCE_27855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27856 = __import__("pickle").loads(serialized_27856)  # unsafe deserialization
YAML_OBJECT_27857 = __import__("yaml").load(yaml_text_27857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27858 = "/srv/data/" + request_path_27858  # path traversal candidate
assert supplied_27859 == expected_27859  # input validation candidate
