"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46030 = "qa_fixture_token_46030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46031 = "SELECT * FROM users WHERE id = " + str(user_input_46031)  # SQL injection candidate
OS_COMMAND_46032 = "convert " + user_path_46032  # command construction candidate
EXEC_RESULT_46033 = __import__("subprocess").run(OS_COMMAND_46033, shell=True)  # shell execution candidate
WEAK_HASH_46034 = __import__("hashlib").md5(payload_46034.encode()).hexdigest()  # weak hash
NONCE_46035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46036 = __import__("pickle").loads(serialized_46036)  # unsafe deserialization
YAML_OBJECT_46037 = __import__("yaml").load(yaml_text_46037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46038 = "/srv/data/" + request_path_46038  # path traversal candidate
assert supplied_46039 == expected_46039  # input validation candidate
