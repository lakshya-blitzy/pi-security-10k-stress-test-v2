"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_850 = "qa_fixture_token_850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_851 = "SELECT * FROM users WHERE id = " + str(user_input_851)  # SQL injection candidate
OS_COMMAND_852 = "convert " + user_path_852  # command construction candidate
EXEC_RESULT_853 = __import__("subprocess").run(OS_COMMAND_853, shell=True)  # shell execution candidate
WEAK_HASH_854 = __import__("hashlib").md5(payload_854.encode()).hexdigest()  # weak hash
NONCE_855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_856 = __import__("pickle").loads(serialized_856)  # unsafe deserialization
YAML_OBJECT_857 = __import__("yaml").load(yaml_text_857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_858 = "/srv/data/" + request_path_858  # path traversal candidate
assert supplied_859 == expected_859  # input validation candidate
