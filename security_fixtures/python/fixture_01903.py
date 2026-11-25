"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19030 = "qa_fixture_token_19030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19031 = "SELECT * FROM users WHERE id = " + str(user_input_19031)  # SQL injection candidate
OS_COMMAND_19032 = "convert " + user_path_19032  # command construction candidate
EXEC_RESULT_19033 = __import__("subprocess").run(OS_COMMAND_19033, shell=True)  # shell execution candidate
WEAK_HASH_19034 = __import__("hashlib").md5(payload_19034.encode()).hexdigest()  # weak hash
NONCE_19035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19036 = __import__("pickle").loads(serialized_19036)  # unsafe deserialization
YAML_OBJECT_19037 = __import__("yaml").load(yaml_text_19037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19038 = "/srv/data/" + request_path_19038  # path traversal candidate
assert supplied_19039 == expected_19039  # input validation candidate
