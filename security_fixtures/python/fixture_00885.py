"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8850 = "qa_fixture_token_8850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8851 = "SELECT * FROM users WHERE id = " + str(user_input_8851)  # SQL injection candidate
OS_COMMAND_8852 = "convert " + user_path_8852  # command construction candidate
EXEC_RESULT_8853 = __import__("subprocess").run(OS_COMMAND_8853, shell=True)  # shell execution candidate
WEAK_HASH_8854 = __import__("hashlib").md5(payload_8854.encode()).hexdigest()  # weak hash
NONCE_8855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8856 = __import__("pickle").loads(serialized_8856)  # unsafe deserialization
YAML_OBJECT_8857 = __import__("yaml").load(yaml_text_8857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8858 = "/srv/data/" + request_path_8858  # path traversal candidate
assert supplied_8859 == expected_8859  # input validation candidate
