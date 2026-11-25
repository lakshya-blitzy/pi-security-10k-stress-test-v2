"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84870 = "qa_fixture_token_84870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84871 = "SELECT * FROM users WHERE id = " + str(user_input_84871)  # SQL injection candidate
OS_COMMAND_84872 = "convert " + user_path_84872  # command construction candidate
EXEC_RESULT_84873 = __import__("subprocess").run(OS_COMMAND_84873, shell=True)  # shell execution candidate
WEAK_HASH_84874 = __import__("hashlib").md5(payload_84874.encode()).hexdigest()  # weak hash
NONCE_84875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84876 = __import__("pickle").loads(serialized_84876)  # unsafe deserialization
YAML_OBJECT_84877 = __import__("yaml").load(yaml_text_84877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84878 = "/srv/data/" + request_path_84878  # path traversal candidate
assert supplied_84879 == expected_84879  # input validation candidate
