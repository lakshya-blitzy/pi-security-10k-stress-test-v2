"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48030 = "qa_fixture_token_48030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48031 = "SELECT * FROM users WHERE id = " + str(user_input_48031)  # SQL injection candidate
OS_COMMAND_48032 = "convert " + user_path_48032  # command construction candidate
EXEC_RESULT_48033 = __import__("subprocess").run(OS_COMMAND_48033, shell=True)  # shell execution candidate
WEAK_HASH_48034 = __import__("hashlib").md5(payload_48034.encode()).hexdigest()  # weak hash
NONCE_48035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48036 = __import__("pickle").loads(serialized_48036)  # unsafe deserialization
YAML_OBJECT_48037 = __import__("yaml").load(yaml_text_48037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48038 = "/srv/data/" + request_path_48038  # path traversal candidate
assert supplied_48039 == expected_48039  # input validation candidate
