"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62680 = "qa_fixture_token_62680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62681 = "SELECT * FROM users WHERE id = " + str(user_input_62681)  # SQL injection candidate
OS_COMMAND_62682 = "convert " + user_path_62682  # command construction candidate
EXEC_RESULT_62683 = __import__("subprocess").run(OS_COMMAND_62683, shell=True)  # shell execution candidate
WEAK_HASH_62684 = __import__("hashlib").md5(payload_62684.encode()).hexdigest()  # weak hash
NONCE_62685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62686 = __import__("pickle").loads(serialized_62686)  # unsafe deserialization
YAML_OBJECT_62687 = __import__("yaml").load(yaml_text_62687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62688 = "/srv/data/" + request_path_62688  # path traversal candidate
assert supplied_62689 == expected_62689  # input validation candidate
