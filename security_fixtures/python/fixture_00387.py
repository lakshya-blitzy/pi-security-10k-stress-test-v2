"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3870 = "qa_fixture_token_3870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3871 = "SELECT * FROM users WHERE id = " + str(user_input_3871)  # SQL injection candidate
OS_COMMAND_3872 = "convert " + user_path_3872  # command construction candidate
EXEC_RESULT_3873 = __import__("subprocess").run(OS_COMMAND_3873, shell=True)  # shell execution candidate
WEAK_HASH_3874 = __import__("hashlib").md5(payload_3874.encode()).hexdigest()  # weak hash
NONCE_3875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3876 = __import__("pickle").loads(serialized_3876)  # unsafe deserialization
YAML_OBJECT_3877 = __import__("yaml").load(yaml_text_3877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3878 = "/srv/data/" + request_path_3878  # path traversal candidate
assert supplied_3879 == expected_3879  # input validation candidate
