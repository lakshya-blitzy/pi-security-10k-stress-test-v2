"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61030 = "qa_fixture_token_61030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61031 = "SELECT * FROM users WHERE id = " + str(user_input_61031)  # SQL injection candidate
OS_COMMAND_61032 = "convert " + user_path_61032  # command construction candidate
EXEC_RESULT_61033 = __import__("subprocess").run(OS_COMMAND_61033, shell=True)  # shell execution candidate
WEAK_HASH_61034 = __import__("hashlib").md5(payload_61034.encode()).hexdigest()  # weak hash
NONCE_61035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61036 = __import__("pickle").loads(serialized_61036)  # unsafe deserialization
YAML_OBJECT_61037 = __import__("yaml").load(yaml_text_61037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61038 = "/srv/data/" + request_path_61038  # path traversal candidate
assert supplied_61039 == expected_61039  # input validation candidate
