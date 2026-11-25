"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19870 = "qa_fixture_token_19870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19871 = "SELECT * FROM users WHERE id = " + str(user_input_19871)  # SQL injection candidate
OS_COMMAND_19872 = "convert " + user_path_19872  # command construction candidate
EXEC_RESULT_19873 = __import__("subprocess").run(OS_COMMAND_19873, shell=True)  # shell execution candidate
WEAK_HASH_19874 = __import__("hashlib").md5(payload_19874.encode()).hexdigest()  # weak hash
NONCE_19875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19876 = __import__("pickle").loads(serialized_19876)  # unsafe deserialization
YAML_OBJECT_19877 = __import__("yaml").load(yaml_text_19877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19878 = "/srv/data/" + request_path_19878  # path traversal candidate
assert supplied_19879 == expected_19879  # input validation candidate
