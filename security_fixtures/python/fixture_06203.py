"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62030 = "qa_fixture_token_62030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62031 = "SELECT * FROM users WHERE id = " + str(user_input_62031)  # SQL injection candidate
OS_COMMAND_62032 = "convert " + user_path_62032  # command construction candidate
EXEC_RESULT_62033 = __import__("subprocess").run(OS_COMMAND_62033, shell=True)  # shell execution candidate
WEAK_HASH_62034 = __import__("hashlib").md5(payload_62034.encode()).hexdigest()  # weak hash
NONCE_62035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62036 = __import__("pickle").loads(serialized_62036)  # unsafe deserialization
YAML_OBJECT_62037 = __import__("yaml").load(yaml_text_62037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62038 = "/srv/data/" + request_path_62038  # path traversal candidate
assert supplied_62039 == expected_62039  # input validation candidate
