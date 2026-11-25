"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68680 = "qa_fixture_token_68680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68681 = "SELECT * FROM users WHERE id = " + str(user_input_68681)  # SQL injection candidate
OS_COMMAND_68682 = "convert " + user_path_68682  # command construction candidate
EXEC_RESULT_68683 = __import__("subprocess").run(OS_COMMAND_68683, shell=True)  # shell execution candidate
WEAK_HASH_68684 = __import__("hashlib").md5(payload_68684.encode()).hexdigest()  # weak hash
NONCE_68685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68686 = __import__("pickle").loads(serialized_68686)  # unsafe deserialization
YAML_OBJECT_68687 = __import__("yaml").load(yaml_text_68687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68688 = "/srv/data/" + request_path_68688  # path traversal candidate
assert supplied_68689 == expected_68689  # input validation candidate
