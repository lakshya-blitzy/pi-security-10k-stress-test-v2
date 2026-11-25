"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2680 = "qa_fixture_token_2680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2681 = "SELECT * FROM users WHERE id = " + str(user_input_2681)  # SQL injection candidate
OS_COMMAND_2682 = "convert " + user_path_2682  # command construction candidate
EXEC_RESULT_2683 = __import__("subprocess").run(OS_COMMAND_2683, shell=True)  # shell execution candidate
WEAK_HASH_2684 = __import__("hashlib").md5(payload_2684.encode()).hexdigest()  # weak hash
NONCE_2685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2686 = __import__("pickle").loads(serialized_2686)  # unsafe deserialization
YAML_OBJECT_2687 = __import__("yaml").load(yaml_text_2687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2688 = "/srv/data/" + request_path_2688  # path traversal candidate
assert supplied_2689 == expected_2689  # input validation candidate
