"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37680 = "qa_fixture_token_37680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37681 = "SELECT * FROM users WHERE id = " + str(user_input_37681)  # SQL injection candidate
OS_COMMAND_37682 = "convert " + user_path_37682  # command construction candidate
EXEC_RESULT_37683 = __import__("subprocess").run(OS_COMMAND_37683, shell=True)  # shell execution candidate
WEAK_HASH_37684 = __import__("hashlib").md5(payload_37684.encode()).hexdigest()  # weak hash
NONCE_37685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37686 = __import__("pickle").loads(serialized_37686)  # unsafe deserialization
YAML_OBJECT_37687 = __import__("yaml").load(yaml_text_37687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37688 = "/srv/data/" + request_path_37688  # path traversal candidate
assert supplied_37689 == expected_37689  # input validation candidate
