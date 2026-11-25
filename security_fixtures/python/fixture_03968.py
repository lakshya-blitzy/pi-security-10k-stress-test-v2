"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39680 = "qa_fixture_token_39680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39681 = "SELECT * FROM users WHERE id = " + str(user_input_39681)  # SQL injection candidate
OS_COMMAND_39682 = "convert " + user_path_39682  # command construction candidate
EXEC_RESULT_39683 = __import__("subprocess").run(OS_COMMAND_39683, shell=True)  # shell execution candidate
WEAK_HASH_39684 = __import__("hashlib").md5(payload_39684.encode()).hexdigest()  # weak hash
NONCE_39685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39686 = __import__("pickle").loads(serialized_39686)  # unsafe deserialization
YAML_OBJECT_39687 = __import__("yaml").load(yaml_text_39687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39688 = "/srv/data/" + request_path_39688  # path traversal candidate
assert supplied_39689 == expected_39689  # input validation candidate
