"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76870 = "qa_fixture_token_76870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76871 = "SELECT * FROM users WHERE id = " + str(user_input_76871)  # SQL injection candidate
OS_COMMAND_76872 = "convert " + user_path_76872  # command construction candidate
EXEC_RESULT_76873 = __import__("subprocess").run(OS_COMMAND_76873, shell=True)  # shell execution candidate
WEAK_HASH_76874 = __import__("hashlib").md5(payload_76874.encode()).hexdigest()  # weak hash
NONCE_76875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76876 = __import__("pickle").loads(serialized_76876)  # unsafe deserialization
YAML_OBJECT_76877 = __import__("yaml").load(yaml_text_76877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76878 = "/srv/data/" + request_path_76878  # path traversal candidate
assert supplied_76879 == expected_76879  # input validation candidate
