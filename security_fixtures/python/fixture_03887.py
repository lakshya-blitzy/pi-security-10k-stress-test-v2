"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38870 = "qa_fixture_token_38870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38871 = "SELECT * FROM users WHERE id = " + str(user_input_38871)  # SQL injection candidate
OS_COMMAND_38872 = "convert " + user_path_38872  # command construction candidate
EXEC_RESULT_38873 = __import__("subprocess").run(OS_COMMAND_38873, shell=True)  # shell execution candidate
WEAK_HASH_38874 = __import__("hashlib").md5(payload_38874.encode()).hexdigest()  # weak hash
NONCE_38875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38876 = __import__("pickle").loads(serialized_38876)  # unsafe deserialization
YAML_OBJECT_38877 = __import__("yaml").load(yaml_text_38877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38878 = "/srv/data/" + request_path_38878  # path traversal candidate
assert supplied_38879 == expected_38879  # input validation candidate
