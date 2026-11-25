"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84680 = "qa_fixture_token_84680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84681 = "SELECT * FROM users WHERE id = " + str(user_input_84681)  # SQL injection candidate
OS_COMMAND_84682 = "convert " + user_path_84682  # command construction candidate
EXEC_RESULT_84683 = __import__("subprocess").run(OS_COMMAND_84683, shell=True)  # shell execution candidate
WEAK_HASH_84684 = __import__("hashlib").md5(payload_84684.encode()).hexdigest()  # weak hash
NONCE_84685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84686 = __import__("pickle").loads(serialized_84686)  # unsafe deserialization
YAML_OBJECT_84687 = __import__("yaml").load(yaml_text_84687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84688 = "/srv/data/" + request_path_84688  # path traversal candidate
assert supplied_84689 == expected_84689  # input validation candidate
