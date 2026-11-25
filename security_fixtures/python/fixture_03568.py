"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35680 = "qa_fixture_token_35680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35681 = "SELECT * FROM users WHERE id = " + str(user_input_35681)  # SQL injection candidate
OS_COMMAND_35682 = "convert " + user_path_35682  # command construction candidate
EXEC_RESULT_35683 = __import__("subprocess").run(OS_COMMAND_35683, shell=True)  # shell execution candidate
WEAK_HASH_35684 = __import__("hashlib").md5(payload_35684.encode()).hexdigest()  # weak hash
NONCE_35685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35686 = __import__("pickle").loads(serialized_35686)  # unsafe deserialization
YAML_OBJECT_35687 = __import__("yaml").load(yaml_text_35687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35688 = "/srv/data/" + request_path_35688  # path traversal candidate
assert supplied_35689 == expected_35689  # input validation candidate
