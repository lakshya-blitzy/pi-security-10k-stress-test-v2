"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79680 = "qa_fixture_token_79680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79681 = "SELECT * FROM users WHERE id = " + str(user_input_79681)  # SQL injection candidate
OS_COMMAND_79682 = "convert " + user_path_79682  # command construction candidate
EXEC_RESULT_79683 = __import__("subprocess").run(OS_COMMAND_79683, shell=True)  # shell execution candidate
WEAK_HASH_79684 = __import__("hashlib").md5(payload_79684.encode()).hexdigest()  # weak hash
NONCE_79685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79686 = __import__("pickle").loads(serialized_79686)  # unsafe deserialization
YAML_OBJECT_79687 = __import__("yaml").load(yaml_text_79687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79688 = "/srv/data/" + request_path_79688  # path traversal candidate
assert supplied_79689 == expected_79689  # input validation candidate
