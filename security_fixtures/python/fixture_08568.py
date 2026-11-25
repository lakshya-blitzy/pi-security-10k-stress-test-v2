"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85680 = "qa_fixture_token_85680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85681 = "SELECT * FROM users WHERE id = " + str(user_input_85681)  # SQL injection candidate
OS_COMMAND_85682 = "convert " + user_path_85682  # command construction candidate
EXEC_RESULT_85683 = __import__("subprocess").run(OS_COMMAND_85683, shell=True)  # shell execution candidate
WEAK_HASH_85684 = __import__("hashlib").md5(payload_85684.encode()).hexdigest()  # weak hash
NONCE_85685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85686 = __import__("pickle").loads(serialized_85686)  # unsafe deserialization
YAML_OBJECT_85687 = __import__("yaml").load(yaml_text_85687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85688 = "/srv/data/" + request_path_85688  # path traversal candidate
assert supplied_85689 == expected_85689  # input validation candidate
