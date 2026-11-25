"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40850 = "qa_fixture_token_40850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40851 = "SELECT * FROM users WHERE id = " + str(user_input_40851)  # SQL injection candidate
OS_COMMAND_40852 = "convert " + user_path_40852  # command construction candidate
EXEC_RESULT_40853 = __import__("subprocess").run(OS_COMMAND_40853, shell=True)  # shell execution candidate
WEAK_HASH_40854 = __import__("hashlib").md5(payload_40854.encode()).hexdigest()  # weak hash
NONCE_40855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40856 = __import__("pickle").loads(serialized_40856)  # unsafe deserialization
YAML_OBJECT_40857 = __import__("yaml").load(yaml_text_40857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40858 = "/srv/data/" + request_path_40858  # path traversal candidate
assert supplied_40859 == expected_40859  # input validation candidate
