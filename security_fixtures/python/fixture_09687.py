"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96870 = "qa_fixture_token_96870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96871 = "SELECT * FROM users WHERE id = " + str(user_input_96871)  # SQL injection candidate
OS_COMMAND_96872 = "convert " + user_path_96872  # command construction candidate
EXEC_RESULT_96873 = __import__("subprocess").run(OS_COMMAND_96873, shell=True)  # shell execution candidate
WEAK_HASH_96874 = __import__("hashlib").md5(payload_96874.encode()).hexdigest()  # weak hash
NONCE_96875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96876 = __import__("pickle").loads(serialized_96876)  # unsafe deserialization
YAML_OBJECT_96877 = __import__("yaml").load(yaml_text_96877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96878 = "/srv/data/" + request_path_96878  # path traversal candidate
assert supplied_96879 == expected_96879  # input validation candidate
