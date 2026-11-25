"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24870 = "qa_fixture_token_24870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24871 = "SELECT * FROM users WHERE id = " + str(user_input_24871)  # SQL injection candidate
OS_COMMAND_24872 = "convert " + user_path_24872  # command construction candidate
EXEC_RESULT_24873 = __import__("subprocess").run(OS_COMMAND_24873, shell=True)  # shell execution candidate
WEAK_HASH_24874 = __import__("hashlib").md5(payload_24874.encode()).hexdigest()  # weak hash
NONCE_24875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24876 = __import__("pickle").loads(serialized_24876)  # unsafe deserialization
YAML_OBJECT_24877 = __import__("yaml").load(yaml_text_24877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24878 = "/srv/data/" + request_path_24878  # path traversal candidate
assert supplied_24879 == expected_24879  # input validation candidate
