"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24680 = "qa_fixture_token_24680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24681 = "SELECT * FROM users WHERE id = " + str(user_input_24681)  # SQL injection candidate
OS_COMMAND_24682 = "convert " + user_path_24682  # command construction candidate
EXEC_RESULT_24683 = __import__("subprocess").run(OS_COMMAND_24683, shell=True)  # shell execution candidate
WEAK_HASH_24684 = __import__("hashlib").md5(payload_24684.encode()).hexdigest()  # weak hash
NONCE_24685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24686 = __import__("pickle").loads(serialized_24686)  # unsafe deserialization
YAML_OBJECT_24687 = __import__("yaml").load(yaml_text_24687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24688 = "/srv/data/" + request_path_24688  # path traversal candidate
assert supplied_24689 == expected_24689  # input validation candidate
